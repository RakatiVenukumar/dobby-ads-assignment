const Folder = require('../models/Folder');
const Image = require('../models/Image');
const File = require('../models/File');
const fs = require('fs');
const path = require('path');

// Recursively delete a folder, its subfolders, and images
async function deleteFolderAndContents(folderId, userId) {
  // Delete all images in this folder
  const images = await Image.find({ folderId, userId });
  for (const img of images) {
    // Remove file from uploads
    try {
      fs.unlinkSync(path.join(__dirname, '../', img.filePath));
    } catch (e) {}
    await img.deleteOne();
  }
  // Delete all files in this folder
  const files = await File.find({ folderId, userId });
  for (const file of files) {
    try {
      fs.unlinkSync(path.join(__dirname, '../', file.filePath));
    } catch (e) {}
    await file.deleteOne();
  }
  // Find and delete all subfolders recursively
  const subfolders = await Folder.find({ parentFolderId: folderId, userId });
  for (const sub of subfolders) {
    await deleteFolderAndContents(sub._id, userId);
  }
  // Delete the folder itself
  await Folder.deleteOne({ _id: folderId, userId });
}

exports.deleteFolder = async (req, res) => {
  try {
    const { folderId } = req.params;
    const folder = await Folder.findOne({ _id: folderId, userId: req.user.id });
    if (!folder) {
      return res.status(404).json({ message: 'Folder not found' });
    }
    await deleteFolderAndContents(folderId, req.user.id);
    res.json({ message: 'Folder and contents deleted' });
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};

exports.deleteImage = async (req, res) => {
  try {
    const { imageId } = req.params;
    const image = await Image.findOne({ _id: imageId, userId: req.user.id });
    if (!image) return res.status(404).json({ message: 'Image not found' });
    try {
      fs.unlinkSync(path.join(__dirname, '../', image.filePath));
    } catch (e) {}
    await image.deleteOne();
    res.json({ message: 'Image deleted' });
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};

exports.deleteFile = async (req, res) => {
  try {
    const { fileId } = req.params;
    const file = await File.findOne({ _id: fileId, userId: req.user.id });
    if (!file) return res.status(404).json({ message: 'File not found' });
    try {
      fs.unlinkSync(path.join(__dirname, '../', file.filePath));
    } catch (e) {}
    await file.deleteOne();
    res.json({ message: 'File deleted' });
  } catch (err) {
    res.status(500).json({ message: 'Server error', error: err.message });
  }
};
