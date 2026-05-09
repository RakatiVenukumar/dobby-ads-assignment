const File = require('../models/File');
const Folder = require('../models/Folder');
const path = require('path');

// Upload file
exports.uploadFile = async (req, res) => {
  try {
    const { folderId } = req.body;
    if (!req.file) {
      return res.status(400).json({ message: 'No file uploaded' });
    }
    if (!folderId) {
      return res.status(400).json({ message: 'Folder ID is required' });
    }
    const folder = await Folder.findOne({ _id: folderId, userId: req.user.id });
    if (!folder) {
      return res.status(404).json({ message: 'Folder not found' });
    }
    const file = new File({
      name: req.file.originalname,
      filePath: path.relative(path.join(__dirname, '../'), req.file.path),
      size: req.file.size,
      folderId,
      userId: req.user.id
    });
    await file.save();
    res.status(201).json(file);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};

// Get files by folder
exports.getFilesByFolder = async (req, res) => {
  try {
    const { folderId } = req.params;
    const files = await File.find({ folderId, userId: req.user.id }).sort({ createdAt: -1 });
    res.json(files);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};

// Get all files for the authenticated user
exports.getFilesForUser = async (req, res) => {
  try {
    const files = await File.find({ userId: req.user.id }).sort({ createdAt: -1 });
    res.json(files);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};
