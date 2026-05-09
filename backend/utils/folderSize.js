const Folder = require('../models/Folder');
const Image = require('../models/Image');
const File = require('../models/File');

// Recursively calculate the total size of a folder and its subfolders
async function getFolderSize(folderId, userId) {
  let totalSize = 0;
  // Get all images in this folder
  const images = await Image.find({ folderId, userId });
  totalSize += images.reduce((sum, img) => sum + img.size, 0);
  // Get all files in this folder
  const files = await File.find({ folderId, userId });
  totalSize += files.reduce((sum, file) => sum + file.size, 0);
  // Get all subfolders
  const subfolders = await Folder.find({ parentFolderId: folderId, userId });
  for (const subfolder of subfolders) {
    totalSize += await getFolderSize(subfolder._id, userId);
  }
  return totalSize;
}

module.exports = getFolderSize;
