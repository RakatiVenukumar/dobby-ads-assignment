const express = require('express');
const { deleteFolder, deleteImage } = require('../controllers/deleteController');
const auth = require('../middleware/authMiddleware');

const router = express.Router();

// Delete folder and its contents
router.delete('/folder/:folderId', auth, deleteFolder);

// Delete image
router.delete('/image/:imageId', auth, deleteImage);

module.exports = router;
