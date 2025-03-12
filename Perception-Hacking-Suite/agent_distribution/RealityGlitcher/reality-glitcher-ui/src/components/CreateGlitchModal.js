import React, { useState } from 'react';

const CreateGlitchModal = ({ isOpen, onClose, onCreateGlitch }) => {
  const [formData, setFormData] = useState({
    type: 'VISUAL',
    intensity: 0.5,
    complexity: 0.5,
    duration: 1.0,
    persistence: 0.2,
    target: 'Visual Field',
    isAdvanced: false,
    isPersistent: false,
    crossModal: false,
    secondaryTarget: null,
    distortionType: null
  });

  // Basic glitch types
  const basicGlitchTypes = [
    'VISUAL', 'AUDITORY', 'TEMPORAL', 'SPATIAL', 'COGNITIVE', 'SYNCHRONISTIC'
  ];
  
  // Advanced cognitive distortion types
  const cognitiveDistortionTypes = [
    'CONFIRMATION_BIAS', 'CATASTROPHIZING', 'BLACK_WHITE_THINKING', 
    'PERSONALIZATION', 'EMOTIONAL_REASONING', 'FILTERING'
  ];
  
  // Cross-modal options based on primary glitch type
  const getCrossModalOptions = (primaryType) => {
    const allTypes = [...basicGlitchTypes];
    return allTypes.filter(type => type !== primaryType);
  };

  // Target options for basic glitches
  const targetOptions = [
    'Visual Field',
    'Auditory Processing',
    'Temporal Perception',
    'Spatial Awareness',
    'Memory Imprints',
    'Emotional Responses',
    'Cognitive Functions'
  ];
  
  // Advanced cognitive distortion targets
  const cognitiveTargets = [
    'Decision Making',
    'Information Processing',
    'Memory Recall',
    'Pattern Recognition',
    'Belief Systems',
    'Self Perception'
  ];

  const handleChange = (e) => {
    const { name, value } = e.target;
    let parsedValue = value;
    
    if (name === 'isAdvanced' || name === 'isPersistent' || name === 'crossModal') {
      parsedValue = e.target.checked;
    } else if (name !== 'type' && name !== 'target' && name !== 'secondaryTarget' && name !== 'distortionType') {
      parsedValue = parseFloat(value);
    }
    
    // Reset secondary options when changing type
    if (name === 'type') {
      setFormData({
        ...formData,
        [name]: parsedValue,
        secondaryTarget: null,
        distortionType: value === 'COGNITIVE' ? 'CONFIRMATION_BIAS' : null
      });
    } else if (name === 'isAdvanced' && !parsedValue) {
      // Reset advanced options when turning off advanced mode
      setFormData({
        ...formData,
        [name]: parsedValue,
        crossModal: false,
        secondaryTarget: null,
        distortionType: null,
        isPersistent: false
      });
    } else if (name === 'crossModal' && !parsedValue) {
      // Reset cross-modal options when turning off
      setFormData({
        ...formData,
        [name]: parsedValue,
        secondaryTarget: null
      });
    } else {
      setFormData({
        ...formData,
        [name]: parsedValue
      });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Create the glitch object
    const glitchData = {
      ...formData,
      active: false
    };
    
    onCreateGlitch(glitchData);
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center z-50 p-4">
      <div className="bg-blue-900/20 border border-blue-800 cyber-border rounded-lg p-6 max-w-md w-full">
        <h2 className="text-xl font-bold text-blue-300 mb-4 border-b border-blue-800 pb-2">Create New Reality Glitch</h2>
        
        <form onSubmit={handleSubmit}>
          {/* Advanced Mode Toggle */}
          <div className="mb-4">
            <label className="flex items-center gap-2 cursor-pointer">
              <input
                type="checkbox"
                name="isAdvanced"
                checked={formData.isAdvanced}
                onChange={handleChange}
                className="form-checkbox h-4 w-4 text-blue-600 bg-gray-900 border-blue-500 rounded focus:ring-blue-500"
              />
              <span className="text-blue-300">Advanced Glitch Mode</span>
            </label>
          </div>
          
          {/* Basic Fields */}
          <div className="mb-4">
            <label className="block text-sm text-blue-400 mb-1">Glitch Type</label>
            <select
              name="type"
              value={formData.type}
              onChange={handleChange}
              className="w-full bg-blue-950/50 border border-blue-800 rounded py-2 px-3 text-blue-300"
            >
              {basicGlitchTypes.map(type => (
                <option key={type} value={type}>{type}</option>
              ))}
            </select>
          </div>
          
          {/* Advanced Options */}
          {formData.isAdvanced && (
            <>
              {/* Persistent Reality Overlay */}
              <div className="mb-4">
                <label className="flex items-center gap-2 cursor-pointer">
                  <input
                    type="checkbox"
                    name="isPersistent"
                    checked={formData.isPersistent}
                    onChange={handleChange}
                    className="form-checkbox h-4 w-4 text-blue-600 bg-gray-900 border-blue-500 rounded focus:ring-blue-500"
                  />
                  <span className="text-blue-300">Persistent Reality Overlay</span>
                </label>
                {formData.isPersistent && (
                  <p className="text-xs text-blue-500 mt-1">
                    Warning: This glitch will affect the entire interface and persist until manually deactivated.
                  </p>
                )}
              </div>
              
              {/* Cross-Modal Sensory Options */}
              <div className="mb-4">
                <label className="flex items-center gap-2 cursor-pointer">
                  <input
                    type="checkbox"
                    name="crossModal"
                    checked={formData.crossModal}
                    onChange={handleChange}
                    className="form-checkbox h-4 w-4 text-blue-600 bg-gray-900 border-blue-500 rounded focus:ring-blue-500"
                  />
                  <span className="text-blue-300">Cross-Modal Sensory Effect</span>
                </label>
                
                {formData.crossModal && (
                  <div className="mt-2">
                    <label className="block text-sm text-blue-400 mb-1">Secondary Sensory Target</label>
                    <select
                      name="secondaryTarget"
                      value={formData.secondaryTarget || ''}
                      onChange={handleChange}
                      className="w-full bg-blue-950/50 border border-blue-800 rounded py-2 px-3 text-blue-300"
                    >
                      <option value="">Select Secondary Type</option>
                      {getCrossModalOptions(formData.type).map(type => (
                        <option key={type} value={type}>{type}</option>
                      ))}
                    </select>
                  </div>
                )}
              </div>
              
              {/* Cognitive Distortion Options */}
              {formData.type === 'COGNITIVE' && (
                <div className="mb-4">
                  <label className="block text-sm text-blue-400 mb-1">Cognitive Distortion Type</label>
                  <select
                    name="distortionType"
                    value={formData.distortionType || cognitiveDistortionTypes[0]}
                    onChange={handleChange}
                    className="w-full bg-blue-950/50 border border-blue-800 rounded py-2 px-3 text-blue-300"
                  >
                    {cognitiveDistortionTypes.map(type => (
                      <option key={type} value={type}>{type.replace(/_/g, ' ')}</option>
                    ))}
                  </select>
                  
                  <div className="mt-2">
                    <label className="block text-sm text-blue-400 mb-1">Target Cognitive Function</label>
                    <select
                      name="target"
                      value={formData.target}
                      onChange={handleChange}
                      className="w-full bg-blue-950/50 border border-blue-800 rounded py-2 px-3 text-blue-300"
                    >
                      {cognitiveTargets.map(target => (
                        <option key={target} value={target}>{target}</option>
                      ))}
                    </select>
                  </div>
                </div>
              )}
              
              {/* Target for non-cognitive types */}
              {formData.type !== 'COGNITIVE' && (
                <div className="mb-4">
                  <label className="block text-sm text-blue-400 mb-1">Target</label>
                  <select
                    name="target"
                    value={formData.target}
                    onChange={handleChange}
                    className="w-full bg-blue-950/50 border border-blue-800 rounded py-2 px-3 text-blue-300"
                  >
                    {targetOptions.map(target => (
                      <option key={target} value={target}>{target}</option>
                    ))}
                  </select>
                </div>
              )}
            </>
          )}
          
          {/* Basic Fields Continued */}
          {!formData.isAdvanced && (
            <div className="mb-4">
              <label className="block text-sm text-blue-400 mb-1">Target</label>
              <select
                name="target"
                value={formData.target}
                onChange={handleChange}
                className="w-full bg-blue-950/50 border border-blue-800 rounded py-2 px-3 text-blue-300"
              >
                {targetOptions.map(target => (
                  <option key={target} value={target}>{target}</option>
                ))}
              </select>
            </div>
          )}
          
          <div className="mb-4">
            <label className="block text-sm text-blue-400 mb-1">Intensity</label>
            <div className="flex items-center">
              <input
                type="range"
                name="intensity"
                min="0.1"
                max="1.0"
                step="0.1"
                value={formData.intensity}
                onChange={handleChange}
                className="w-full mr-2 cyber-slider"
              />
              <span className="text-blue-300 w-10 text-right">{(formData.intensity * 100).toFixed(0)}%</span>
            </div>
          </div>
          
          <div className="mb-4">
            <label className="block text-sm text-blue-400 mb-1">Complexity</label>
            <div className="flex items-center">
              <input
                type="range"
                name="complexity"
                min="0.1"
                max="1.0"
                step="0.1"
                value={formData.complexity}
                onChange={handleChange}
                className="w-full mr-2 cyber-slider"
              />
              <span className="text-blue-300 w-10 text-right">{(formData.complexity * 100).toFixed(0)}%</span>
            </div>
          </div>
          
          <div className="mb-4">
            <label className="block text-sm text-blue-400 mb-1">Persistence</label>
            <div className="flex items-center">
              <input
                type="range"
                name="persistence"
                min="0.1"
                max="1.0"
                step="0.1"
                value={formData.persistence}
                onChange={handleChange}
                className="w-full mr-2 cyber-slider"
              />
              <span className="text-blue-300 w-10 text-right">{(formData.persistence * 100).toFixed(0)}%</span>
            </div>
          </div>
          
          <div className="flex justify-end space-x-3 mt-6 border-t border-blue-800 pt-4">
            <button
              type="button"
              onClick={onClose}
              className="px-4 py-2 bg-gray-800 text-gray-300 rounded hover:bg-gray-700"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-4 py-2 bg-blue-800 text-blue-200 rounded hover:bg-blue-700"
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