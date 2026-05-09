import React, { useEffect, useState } from 'react';
import api from '../services/api';
import FolderTree from '../components/FolderTree';
import ImageGallery from '../components/ImageGallery';
import UploadSection from '../components/UploadSection';
import CreateFolder from '../components/CreateFolder';

const Dashboard = () => {
  const [folders, setFolders] = useState([]);
  const [images, setImages] = useState([]);
  const [allImages, setAllImages] = useState([]);
  const [allFiles, setAllFiles] = useState([]);
  const [selectedFolder, setSelectedFolder] = useState(() => localStorage.getItem('selectedFolderId'));
  const [foldersLoaded, setFoldersLoaded] = useState(false);

  const selectedFolderValid = selectedFolder && folders.some((folder) => folder._id === selectedFolder);

  const fetchFolders = async () => {
    try {
      const res = await api.get('/folders');
      setFolders(res.data);
      setFoldersLoaded(true);
    } catch (err) {
      console.error('Error fetching folders:', err);
      setFoldersLoaded(true);
    }
  };
  const fetchImages = async (folderId) => {
    if (!folderId) return setImages([]);
    try {
      const res = await api.get(`/images/${folderId}`);
      setImages(res.data);
    } catch (err) {
      console.error('Error fetching images:', err);
    }
  };

  const fetchAllImages = async () => {
    try {
      const res = await api.get('/images');
      setAllImages(res.data);
    } catch (err) {
      console.error('Error fetching all images:', err);
    }
  };

  const fetchAllFiles = async () => {
    try {
      const res = await api.get('/files');
      setAllFiles(res.data);
    } catch (err) {
      console.error('Error fetching all files:', err);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    window.location.href = '/login';
  };

  useEffect(() => {
    fetchFolders();
    fetchAllImages();
    fetchAllFiles();
  }, []);
  useEffect(() => {
    if (!foldersLoaded) return;
    if (selectedFolderValid) {
      localStorage.setItem('selectedFolderId', selectedFolder);
      fetchImages(selectedFolder);
    } else {
      setSelectedFolder(null);
      localStorage.removeItem('selectedFolderId');
      setImages([]);
    }
  }, [selectedFolder, selectedFolderValid, foldersLoaded]);

  const selectedFolderName = selectedFolderValid
    ? folders.find((folder) => folder._id === selectedFolder)?.name
    : null;

  return (
    <div className="dashboard-container">
      <header className="dashboard-header">
        <h1>Dashboard</h1>
        <button onClick={handleLogout} className="logout-btn">Logout</button>
      </header>
      <div className="dashboard-layout">
        <aside className="sidebar">
          <div className="sidebar-header">
            <h2>Folders</h2>
            {selectedFolderValid && (
              <button type="button" className="ghost-btn" onClick={() => setSelectedFolder(null)}>
                Clear selection
              </button>
            )}
          </div>
          <CreateFolder
            selectedFolderId={selectedFolderValid ? selectedFolder : null}
            onCreate={fetchFolders}
            onImport={() => {
              fetchFolders();
              fetchAllImages();
              fetchAllFiles();
              if (selectedFolderValid) {
                fetchImages(selectedFolder);
              }
            }}
          />
          <FolderTree 
            folders={folders} 
            images={allImages}
            files={allFiles}
            onSelect={setSelectedFolder} 
            selectedId={selectedFolder} 
            onRename={() => {
              fetchFolders();
              fetchAllImages();
              fetchAllFiles();
            }}
          />
        </aside>
        <main className="main-content">
          <h2>Images</h2>
          <div className="upload-meta">
            {selectedFolderName ? (
              <span className="selection-chip">Uploading to: {selectedFolderName}</span>
            ) : (
              <span className="selection-hint">Select a folder to upload images.</span>
            )}
          </div>
          <UploadSection folderId={selectedFolderValid ? selectedFolder : null} onUpload={() => {
            fetchImages(selectedFolder);
            fetchAllImages();
            fetchAllFiles();
          }} />
          <ImageGallery images={images} onDelete={() => {
            fetchImages(selectedFolder);
            fetchAllImages();
          }} />
        </main>
      </div>
    </div>
  );
};

export default Dashboard;
