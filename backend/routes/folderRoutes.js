const express = require('express');
const { createFolder, getFolders } = require('../controllers/folderController');
const auth = require('../middleware/authMiddleware');

const router = express.Router();

// Create folder
router.post('/', auth, createFolder);

// Get all folders for user
router.get('/', auth, getFolders);

module.exports = router;
