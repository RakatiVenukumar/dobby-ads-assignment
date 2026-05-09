const express = require('express');
const { upload, uploadAny } = require('../config/multer');
const { uploadImage, getImagesByFolder, getImagesForUser, importFolderImages } = require('../controllers/imageController');
const auth = require('../middleware/authMiddleware');

const router = express.Router();

// Upload image
router.post('/upload', auth, upload.single('image'), uploadImage);

// Import folder images
router.post('/import', auth, uploadAny.any(), importFolderImages);

// Get all images for user
router.get('/', auth, getImagesForUser);

// Get images by folder
router.get('/:folderId', auth, getImagesByFolder);

module.exports = router;
