const express = require('express');
const upload = require('../config/multer');
const { uploadImage, getImagesByFolder } = require('../controllers/imageController');
const auth = require('../middleware/authMiddleware');

const router = express.Router();

// Upload image
router.post('/upload', auth, upload.single('image'), uploadImage);

// Get images by folder
router.get('/:folderId', auth, getImagesByFolder);

module.exports = router;
