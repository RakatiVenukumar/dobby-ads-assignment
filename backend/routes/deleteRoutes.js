const express = require('express');
const { deleteFolder, deleteImage, deleteFile } = require('../controllers/deleteController');
const auth = require('../middleware/authMiddleware');

const router = express.Router();

// Delete folder and its contents
router.delete('/folder/:folderId', auth, deleteFolder);

// Delete image
router.delete('/image/:imageId', auth, deleteImage);

// Delete file
router.delete('/file/:fileId', auth, deleteFile);

module.exports = router;
