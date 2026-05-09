import React, { useEffect, useState } from 'react';
import api, { API_BASE_URL } from '../services/api';
import { motion } from 'framer-motion';

const FolderTree = ({ parentId = null, folders, images = [], files = [], onSelect, selectedId, onRename }) => {
  const [renamingId, setRenamingId] = useState(null);
  const [renameValue, setRenameValue] = useState('');
  const [sizes, setSizes] = useState({});
  const [loading, setLoading] = useState({});
  const [error, setError] = useState({});

  const fetchSize = async (folderId) => {
    setLoading((prev) => ({ ...prev, [folderId]: true }));
    setError((prev) => ({ ...prev, [folderId]: null }));
    try {
      const res = await api.get(`/folders/${folderId}/size`);
      setSizes((prev) => ({ ...prev, [folderId]: res.data.formatted }));
    } catch (err) {
      setError((prev) => ({ ...prev, [folderId]: '!' }));
    }
    setLoading((prev) => ({ ...prev, [folderId]: false }));
  };

  useEffect(() => {
    folders.forEach((folder) => {
      if (!sizes[folder._id]) fetchSize(folder._id);
    });
    // eslint-disable-next-line
  }, [folders]);

  const handleRename = async (folderId) => {
    if (!renameValue) return;
    try {
      await api.patch(`/folders/${folderId}/rename`, { name: renameValue });
      setRenamingId(null);
      setRenameValue('');
      if (onRename) onRename();
    } catch (err) {
      alert('Rename failed');
    }
  };

  const handleDelete = async (folderId) => {
    const confirmed = window.confirm('Delete this folder and all contents?');
    if (!confirmed) return;
    try {
      await api.delete(`/delete/folder/${folderId}`);
      if (onRename) onRename();
    } catch (err) {
      alert(err.response?.data?.message || 'Delete failed');
    }
  };

  const renderNode = (folder) => {
    const folderImages = images.filter((img) => String(img.folderId) === String(folder._id));
    const folderFiles = files.filter((file) => String(file.folderId) === String(folder._id));
    return (
    <motion.div key={folder._id} style={{ marginLeft: 20 }} initial={{ opacity: 0, x: -10 }} animate={{ opacity: 1, x: 0 }}>
      <div className={selectedId === folder._id ? 'folder selected' : 'folder'} style={{ display: 'flex', alignItems: 'center' }}>
        <span
          onClick={() => onSelect(selectedId === folder._id ? null : folder._id)}
          style={{ flex: 1, cursor: 'pointer' }}
        >📁 {renamingId === folder._id ? (
          <>
            <input value={renameValue} onChange={e => setRenameValue(e.target.value)} onBlur={() => setRenamingId(null)} autoFocus style={{ width: 80 }} />
            <button onClick={() => handleRename(folder._id)}>Save</button>
          </>
        ) : (
          <span>{folder.name}</span>
        )}</span>
        <span style={{ marginLeft: 8, fontSize: 12, color: '#aaa' }}>
          {loading[folder._id] ? '...' : error[folder._id] ? error[folder._id] : sizes[folder._id]}
        </span>
        <button style={{ marginLeft: 8 }} onClick={(e) => { e.stopPropagation(); setRenamingId(folder._id); setRenameValue(folder.name); }}>✏️</button>
        <button className="danger-btn" style={{ marginLeft: 8 }} onClick={(e) => { e.stopPropagation(); handleDelete(folder._id); }}>🗑️</button>
      </div>
      {!!folderImages.length && (
        <div className="folder-images">
          {folderImages.map((img) => (
            <div key={img._id} className="folder-image-row">
              <img src={`${API_BASE_URL}/${img.filePath.replace(/\\/g, '/')}`} alt={img.name} />
              <span title={img.name}>{img.name}</span>
            </div>
          ))}
        </div>
      )}
      {!!folderFiles.length && (
        <div className="folder-files">
          {folderFiles.map((file) => (
            <div key={file._id} className="folder-file-row">
              <span className="file-icon">📄</span>
              <span title={file.name}>{file.name}</span>
            </div>
          ))}
        </div>
      )}
      {renderChildren(folder._id)}
    </motion.div>
    );
  };

  const renderChildren = (parentIdValue) => {
    const children = folders.filter((f) => String(f.parentFolderId) === String(parentIdValue));
    return children.map((child) => renderNode(child));
  };

  const idSet = new Set(folders.map((folder) => String(folder._id)));
  const roots = folders.filter((folder) => !folder.parentFolderId || !idSet.has(String(folder.parentFolderId)));

  if (!roots.length) {
    return <div className="empty-state">No folders yet.</div>;
  }

  return <div>{roots.map((folder) => renderNode(folder))}</div>;
};

export default FolderTree;
