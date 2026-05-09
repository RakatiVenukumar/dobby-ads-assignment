import React from 'react';
import api, { API_BASE_URL } from '../services/api';

const ImageGallery = ({ images, onDelete }) => {
  const handleDelete = async (imageId) => {
    const confirmed = window.confirm('Delete this image?');
    if (!confirmed) return;
    try {
      await api.delete(`/delete/image/${imageId}`);
      if (onDelete) onDelete();
    } catch (err) {
      alert(err.response?.data?.message || 'Delete failed');
    }
  };

  if (!images.length) {
    return <div className="empty-state">No images yet.</div>;
  }

  return (
    <div className="image-gallery">
      {images.map((img) => (
        <div key={img._id} className="image-card">
          <img src={`${API_BASE_URL}/${img.filePath.replace(/\\/g, '/')}`} alt={img.name} />
          <div className="image-meta">
            <div className="image-name">{img.name}</div>
            <button type="button" className="danger-btn" onClick={() => handleDelete(img._id)}>Delete</button>
          </div>
        </div>
      ))}
    </div>
  );
};

export default ImageGallery;
