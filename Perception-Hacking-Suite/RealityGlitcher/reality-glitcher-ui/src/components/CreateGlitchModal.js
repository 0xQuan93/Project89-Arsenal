import React, { useState } from 'react';

const CreateGlitchModal = ({ isOpen, onClose, onCreateGlitch }) => {
  const [formData, setFormData] = useState({
    type: 'VISUAL',
    intensity: 0.5,
    complexity: 0.5,
    duration: 1.0,
    persistence: 0.2,
    target: 'consensus_reality'
  });

  const glitchTypes = [
    'VISUAL', 'AUDITORY', 'TEMPORAL', 'SPATIAL', 'COGNITIVE', 'SYNCHRONISTIC'
  ];

  const handleChange = (e) => {
    const { name, value } = e.target;
    let parsedValue = value;
    
    if (name !== 'type' && name !== 'target') {
      parsedValue = parseFloat(value);
    }
    
    setFormData({
      ...formData,
      [name]: parsedValue
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onCreateGlitch(formData);
    onClose();
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70">
      <div className="w-full max-w-md p-6 border border-blue-700 bg-blue-900/20 rounded-lg shadow-lg backdrop-blur-sm">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-bold text-blue-300">Create New Reality Glitch</h2>
          <button 
            onClick={onClose}
            className="text-blue-400 hover:text-blue-200"
          >
            ✕
          </button>
        </div>
        
        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className="block text-blue-400 mb-1">Glitch Type</label>
            <select 
              name="type"
              value={formData.type}
              onChange={handleChange}
              className="w-full p-2 rounded bg-blue-950 border border-blue-700 text-blue-200"
            >
              {glitchTypes.map(type => (
                <option key={type} value={type}>{type}</option>
              ))}
            </select>
          </div>
          
          <div className="mb-4">
            <label className="block text-blue-400 mb-1">Intensity ({(formData.intensity * 100).toFixed(0)}%)</label>
            <input 
              type="range" 
              name="intensity"
              min="0" 
              max="1" 
              step="0.01" 
              value={formData.intensity}
              onChange={handleChange}
              className="w-full"
            />
          </div>
          
          <div className="mb-4">
            <label className="block text-blue-400 mb-1">Complexity ({(formData.complexity * 100).toFixed(0)}%)</label>
            <input 
              type="range" 
              name="complexity"
              min="0" 
              max="1" 
              step="0.01" 
              value={formData.complexity}
              onChange={handleChange}
              className="w-full"
            />
          </div>
          
          <div className="mb-4">
            <label className="block text-blue-400 mb-1">Duration ({formData.duration.toFixed(1)}s)</label>
            <input 
              type="range" 
              name="duration"
              min="0.1" 
              max="10" 
              step="0.1" 
              value={formData.duration}
              onChange={handleChange}
              className="w-full"
            />
          </div>
          
          <div className="mb-4">
            <label className="block text-blue-400 mb-1">Persistence ({(formData.persistence * 100).toFixed(0)}%)</label>
            <input 
              type="range" 
              name="persistence"
              min="0" 
              max="1" 
              step="0.01" 
              value={formData.persistence}
              onChange={handleChange}
              className="w-full"
            />
          </div>
          
          <div className="mb-6">
            <label className="block text-blue-400 mb-1">Target</label>
            <input 
              type="text" 
              name="target"
              value={formData.target}
              onChange={handleChange}
              className="w-full p-2 rounded bg-blue-950 border border-blue-700 text-blue-200"
            />
          </div>
          
          <div className="flex justify-end">
            <button 
              type="button" 
              onClick={onClose}
              className="mr-2 px-4 py-2 border border-blue-700 rounded-md text-blue-300 hover:bg-blue-800/30"
            >
              Cancel
            </button>
            <button 
              type="submit"
              className="px-4 py-2 bg-blue-600/50 border border-blue-500 rounded-md text-blue-100 hover:bg-blue-700/50"
            >
              Create Glitch
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default CreateGlitchModal; 