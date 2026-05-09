import React, { useRef, useState } from 'react';
import api from '../services/api';

const UploadSection = ({ folderId, onUpload }) => {
  const imageRef = useRef();
  const fileRef = useRef();
  const [loadingImage, setLoadingImage] = useState(false);
  const [loadingFile, setLoadingFile] = useState(false);

  const handleImageUpload = async (e) => {
    e.preventDefault();
    const file = imageRef.current.files[0];
    if (!file) return alert('Select image');
    if (!folderId) return alert('Select folder');

    setLoadingImage(true);
    const formData = new FormData();
    formData.append('image', file);
    formData.append('folderId', folderId);

    try {
      await api.post('/images/upload', formData);
      imageRef.current.value = '';
      onUpload();
    } catch (err) {
      console.error(err);
      alert(err.response?.data?.message || 'Upload failed');
    } finally {
      setLoadingImage(false);
    }
  };

  const handleFileUpload = async (e) => {
    e.preventDefault();
    const file = fileRef.current.files[0];
    if (!file) return alert('Select file');
    if (!folderId) return alert('Select folder');

    setLoadingFile(true);
    const formData = new FormData();
    formData.append('file', file);
    formData.append('folderId', folderId);

    try {
      await api.post('/files/upload', formData);
      fileRef.current.value = '';
      onUpload();
    } catch (err) {
      console.error(err);
      alert(err.response?.data?.message || 'Upload failed');
    } finally {
      setLoadingFile(false);
    }
  };

  return (
    <div className="upload-stack">
      <form onSubmit={handleImageUpload} className="upload-section">
        <input type="file" ref={imageRef} accept="image/*" required />
        <button type="submit" disabled={loadingImage}>{loadingImage ? 'Uploading...' : 'Upload Image'}</button>
      </form>
      <form onSubmit={handleFileUpload} className="upload-section">
        <input type="file" ref={fileRef} required />
        <button type="submit" className="secondary-btn" disabled={loadingFile}>{loadingFile ? 'Uploading...' : 'Upload File'}</button>
      </form>
    </div>
  );
};

export default UploadSection;
