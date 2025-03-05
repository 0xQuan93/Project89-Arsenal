import React from 'react';

const GlitchCard = ({ glitch, isSelected, onSelect, onToggle }) => {
  return (
    <div 
      className={`p-3 border rounded-md cursor-pointer transition 
        ${isSelected ? 'border-blue-400 bg-blue-900/40' : 'border-blue-800 hover:border-blue-600'}
        ${glitch.active ? 'opacity-100' : 'opacity-50'}`}
      onClick={() => onSelect(glitch)}
    >
      <div className="flex justify-between items-center">
        <div className="font-bold">{glitch.id} <span className="text-xs ml-2 text-blue-400">{glitch.type}</span></div>
        <div>
          <button 
            className={`px-2 py-1 rounded text-xs ${glitch.active ? 'bg-green-700 text-green-200' : 'bg-red-900 text-red-200'}`}
            onClick={(e) => {
              e.stopPropagation();
              onToggle(glitch.id);
            }}
          >
            {glitch.active ? 'ACTIVE' : 'INACTIVE'}
          </button>
        </div>
      </div>
      <div className="mt-2 flex items-center text-sm">
        <div className="mr-4">
          <span className="text-blue-400">Intensity:</span> {(glitch.intensity * 100).toFixed(0)}%
        </div>
        <div>
          <span className="text-blue-400">Stability:</span> {(glitch.stability * 100).toFixed(0)}%
        </div>
      </div>
    </div>
  );
};

export default GlitchCard; 