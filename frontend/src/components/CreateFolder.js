import React, { useEffect, useState } from 'react';
import api from '../services/api';

const CreateFolder = ({ selectedFolderId, onCreate, onImport }) => {
  const [name, setName] = useState('');
  const [error, setError] = useState('');
  const [createAsRoot, setCreateAsRoot] = useState(false);
  const fileInputRef = React.useRef(null);

  useEffect(() => {
    if (!selectedFolderId) {
      setCreateAsRoot(true);
    }
  }, [selectedFolderId]);

  const handleCreate = async (e) => {
    e.preventDefault();
    setError('');
    if (!name) return setError('Folder name required');
    const parentFolderId = createAsRoot || !selectedFolderId ? null : selectedFolderId;
    try {
      await api.post('/folders', { name, parentFolderId });
      setName('');
      onCreate();
    } catch (err) {
      setError(err.response?.data?.message || 'Failed to create folder');
    }
  };

  const handleImport = async (e) => {
    const files = Array.from(e.target.files || []);
    if (!files.length) return;
    const parentFolderId = createAsRoot || !selectedFolderId ? null : selectedFolderId;
    const formData = new FormData();
    const rootFolderName = files[0]?.webkitRelativePath?.split('/')?.[0];
    files.forEach((file) => {
      const relativePath = file.webkitRelativePath || file.name;
      formData.append('files', file, relativePath);
    });
    if (parentFolderId) {
      formData.append('parentFolderId', parentFolderId);
    }
    if (rootFolderName) {
      formData.append('rootFolderName', rootFolderName);
    }
    try {
      await api.post('/images/import', formData);
      if (onImport) onImport();
    } catch (err) {
      setError(err.response?.data?.message || 'Import failed');
    } finally {
      e.target.value = '';
    }
  };

  return (
    <form onSubmit={handleCreate} className="create-folder">
      <input type="text" value={name} onChange={e => setName(e.target.value)} placeholder="New Folder Name" />
      <button type="submit">Create Folder</button>
      <button type="button" className="secondary-btn" onClick={() => fileInputRef.current?.click()}>
        Import Folder
      </button>
      <input
        ref={fileInputRef}
        type="file"
        webkitdirectory="true"
        directory=""
        multiple
        onChange={handleImport}
        style={{ display: 'none' }}
      />
      {selectedFolderId && (
        <label className="create-folder-toggle">
          <input
            type="checkbox"
            checked={createAsRoot}
            onChange={(e) => setCreateAsRoot(e.target.checked)}
          />
          Create as root
        </label>
      )}
      {error && <div className="error">{error}</div>}
    </form>
  );
};

export default CreateFolder;
