const express = require("express");
const router = express.Router();

const auth = require("../middleware/authMiddleware");

const {
  createFolder,
  getFolders,
  renameFolder,
  getFolderSize,
} = require("../controllers/folderController");

// Create folder
router.post("/", auth, createFolder);

// Get all folders
router.get("/", auth, getFolders);

// Rename folder
router.patch("/:folderId/rename", auth, renameFolder);

// Get folder size
router.get("/:folderId/size", auth, getFolderSize);

module.exports = router;