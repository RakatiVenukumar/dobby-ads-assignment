
const Folder = require('../models/Folder');
const getFolderSize = require('../utils/folderSize');
// Rename a folder
exports.renameFolder = async (req, res) => {
  try {
    const { folderId } = req.params;
    const { name } = req.body;
    if (!name) return res.status(400).json({ message: 'Folder name is required.' });
    const folder = await Folder.findOneAndUpdate(
      { _id: folderId, userId: req.user.id },
      { name },
      { new: true }
    );
    if (!folder) return res.status(404).json({ message: 'Folder not found' });
    res.json(folder);
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};

// Get recursive folder size
exports.getFolderSize = async (req, res) => {
  try {
    const { folderId } = req.params;
    const size = await getFolderSize(folderId, req.user.id);
    // Format size to KB/MB
    let formatted = size + ' B';
    if (size > 1024 * 1024) formatted = (size / (1024 * 1024)).toFixed(2) + ' MB';
    else if (size > 1024) formatted = (size / 1024).toFixed(2) + ' KB';
    res.json({ size, formatted });
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};

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
