const Image = require('../models/Image');
const Folder = require('../models/Folder');
const path = require('path');

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
