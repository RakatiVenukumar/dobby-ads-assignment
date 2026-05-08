const express = require('express');
const { createFolder, getFolders, renameFolder, getFolderSize } = require('../controllers/folderController');
// Rename folder
router.patch('/:folderId/rename', auth, renameFolder);

// Get folder size
router.get('/:folderId/size', auth, getFolderSize);
const auth = require('../middleware/authMiddleware');

const router = express.Router();

// Create folder
router.post('/', auth, createFolder);

// Get all folders for user
router.get('/', auth, getFolders);

module.exports = router;
