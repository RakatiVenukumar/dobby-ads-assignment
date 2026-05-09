const express = require('express');
const { uploadAny } = require('../config/multer');
const { uploadFile, getFilesByFolder, getFilesForUser } = require('../controllers/fileController');
const auth = require('../middleware/authMiddleware');

const router = express.Router();

// Upload file
router.post('/upload', auth, uploadAny.single('file'), uploadFile);

// Get all files for user
router.get('/', auth, getFilesForUser);

// Get files by folder
router.get('/:folderId', auth, getFilesByFolder);

module.exports = router;
