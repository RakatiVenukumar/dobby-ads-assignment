

const express = require("express");
const dotenv = require("dotenv");
const cors = require("cors");
const authRoutes = require("./routes/auth");
const folderRoutes = require("./routes/folderRoutes");

const connectDB = require("./config/db");

dotenv.config();

const app = express();

app.use(express.json());
app.use(cors());

// Use auth routes

app.use("/api/auth", authRoutes);
app.use("/api/folders", folderRoutes);

app.get("/", (req, res) => {
  res.send("API Running...");
});



const PORT = process.env.PORT || 5000;

// Connect to MongoDB and then start server
connectDB().then(() => {
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
});