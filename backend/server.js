

const express = require("express");
const dotenv = require("dotenv");
const cors = require("cors");
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");
const path = require("path");
const authRoutes = require("./routes/auth");
const folderRoutes = require("./routes/folderRoutes");
const imageRoutes = require("./routes/imageRoutes");
const fileRoutes = require("./routes/fileRoutes");
const deleteRoutes = require("./routes/deleteRoutes");

const connectDB = require("./config/db");

dotenv.config();

const app = express();

// Security Middlewares
app.use(helmet({
  crossOriginResourcePolicy: false, // Required to serve images to frontend
}));
app.use(cors());
app.use(express.json());

// Serve uploaded images
app.use("/uploads", express.static(path.join(__dirname, "uploads")));

// Rate Limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: process.env.NODE_ENV === 'production' ? 100 : 1000
});
app.use('/api/', limiter);

// Use routes
app.use("/api/auth", authRoutes);
app.use("/api/folders", folderRoutes);
app.use("/api/images", imageRoutes);
app.use("/api/files", fileRoutes);
app.use("/api/delete", deleteRoutes);

app.get("/", (req, res) => {
  res.send("DobbyAds API Running...");
});

// Global error handler (multer, validation, etc.)
app.use((err, req, res, next) => {
  if (err && err.name === "MulterError") {
    return res.status(400).json({ message: err.message });
  }
  if (err) {
    return res.status(400).json({ message: err.message || "Request failed" });
  }
  return next();
});



const PORT = process.env.PORT || 5000;

// Connect to MongoDB and then start server
connectDB().then(() => {
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
});