const Folder = require('../models/Folder');

// Create a new folder
exports.createFolder = async (req, res) => {
  try {
    const { name, parentFolderId } = req.body;
    if (!name) {
      return res.status(400).json({ message: 'Folder name is required.' });
    }
    const folder = new Folder({
      name,
      parentFolderId: parentFolderId || null,
      userId: req.user.id
    });
    await folder.save();
    res.status(201).json(folder);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};

// Get all folders for the authenticated user
exports.getFolders = async (req, res) => {
  try {
    const folders = await Folder.find({ userId: req.user.id }).sort({ createdAt: 1 });
    res.json(folders);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};
