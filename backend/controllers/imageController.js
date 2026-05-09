const Image = require('../models/Image');
const File = require('../models/File');
const Folder = require('../models/Folder');
const path = require('path');
const fs = require('fs');

// Upload image
exports.uploadImage = async (req, res) => {
  try {
    const { folderId } = req.body;
    if (!req.file) {
      return res.status(400).json({ message: 'No file uploaded' });
    }
    if (!folderId) {
      return res.status(400).json({ message: 'Folder ID is required' });
    }
    // Check if folder exists
    const folder = await Folder.findOne({ _id: folderId, userId: req.user.id });
    if (!folder) {
      return res.status(404).json({ message: 'Folder not found' });
    }
    const image = new Image({
      name: req.file.originalname,
      filePath: path.relative(path.join(__dirname, '../'), req.file.path),
      size: req.file.size,
      folderId,
      userId: req.user.id
    });
    await image.save();
    res.status(201).json(image);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};

// Get images by folder
exports.getImagesByFolder = async (req, res) => {
  try {
    const { folderId } = req.params;
    const images = await Image.find({ folderId, userId: req.user.id }).sort({ createdAt: -1 });
    res.json(images);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};

// Get all images for the authenticated user
exports.getImagesForUser = async (req, res) => {
  try {
    const images = await Image.find({ userId: req.user.id }).sort({ createdAt: -1 });
    res.json(images);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};

const getOrCreateFolder = async ({ name, parentFolderId, userId, cache }) => {
  const key = `${parentFolderId || 'root'}::${name}`;
  if (cache[key]) return cache[key];
  let folder = await Folder.findOne({ name, parentFolderId: parentFolderId || null, userId });
  if (!folder) {
    folder = await Folder.create({ name, parentFolderId: parentFolderId || null, userId });
  }
  cache[key] = folder._id;
  return folder._id;
};

// Import images from a local folder selection
exports.importFolderImages = async (req, res) => {
  try {
    const { parentFolderId, rootFolderName } = req.body;
    const files = req.files || [];
    if (!files.length) {
      return res.status(400).json({ message: 'No files uploaded' });
    }

    const cache = {};
    const createdImages = [];
    const createdFiles = [];

    const fallbackRootName = rootFolderName || 'Imported';

    for (const file of files) {
      const relativePath = (file.originalname || file.filename).replace(/\\/g, '/');
      const segments = relativePath.split('/').filter(Boolean);
      const fileName = segments.pop();
      let currentParent = parentFolderId || null;

      for (const segment of segments) {
        currentParent = await getOrCreateFolder({
          name: segment,
          parentFolderId: currentParent,
          userId: req.user.id,
          cache
        });
      }

      if (!currentParent) {
        currentParent = await getOrCreateFolder({
          name: fallbackRootName,
          parentFolderId: null,
          userId: req.user.id,
          cache
        });
      }

      if (file.mimetype && file.mimetype.startsWith('image/')) {
        const image = new Image({
          name: fileName || file.originalname,
          filePath: path.relative(path.join(__dirname, '../'), file.path),
          size: file.size,
          folderId: currentParent,
          userId: req.user.id
        });
        await image.save();
        createdImages.push(image);
      } else {
        const newFile = new File({
          name: fileName || file.originalname,
          filePath: path.relative(path.join(__dirname, '../'), file.path),
          size: file.size,
          folderId: currentParent,
          userId: req.user.id
        });
        await newFile.save();
        createdFiles.push(newFile);
      }
    }

    res.status(201).json({
      message: 'Import completed',
      importedImages: createdImages.length,
      importedFiles: createdFiles.length
    });
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};
