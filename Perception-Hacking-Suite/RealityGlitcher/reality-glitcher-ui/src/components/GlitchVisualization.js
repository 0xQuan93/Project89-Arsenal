import React from 'react';

const GlitchVisualization = ({ glitch }) => {
  if (!glitch) {
    return (
      <div className="h-64 flex items-center justify-center text-blue-500 border border-blue-900 rounded bg-black/50">
        <div className="text-center">
          <div className="text-xl">Select a glitch to visualize</div>
          <div className="text-sm mt-2">No active visualization</div>
        </div>
      </div>
    );
  }

  return (
    <div>
      <div className="mb-4">
        <h3 className="text-lg font-bold">{glitch.type} Glitch {glitch.id}</h3>
        <div className="text-sm text-blue-400">Induced fracture in perception matrix</div>
      </div>
      
      {/* Visualization */}
      <div className="relative h-64 border border-blue-800 rounded bg-black/50 overflow-hidden">
        <div className={`absolute inset-0 flex items-center justify-center ${!glitch.active && 'opacity-30'}`}>
          {glitch.type === 'VISUAL' && (
            <div className="w-full h-full flex items-center justify-center">
              <div className="absolute w-32 h-32 rounded-full bg-purple-500/30 animate-pulse"/>
              <div className="absolute w-48 h-48 rounded-full border border-blue-500/60 animate-spin"/>
              <div className="absolute w-64 h-64 rounded-full border border-cyan-500/40 animate-pulse"/>
              <div className="text-center z-10 text-blue-300">
                <div className="text-xl">Visual Fracture Pattern</div>
                <div className="text-sm mt-2">Coherence: {(glitch.stability * 100).toFixed(1)}%</div>
              </div>
            </div>
          )}
          
          {glitch.type === 'AUDITORY' && (
            <div className="w-full h-full flex items-center justify-center">
              <div className="absolute inset-0">
                {[...Array(20)].map((_, i) => (
                  <div 
                    key={i}
                    className="absolute bottom-0 w-1 bg-blue-500/60"
                    style={{
                      height: `${20 + Math.sin(i * 0.5) * 60}px`,
                      left: `${(i + 1) * 5}%`,
                      opacity: Math.random() * 0.7 + 0.3,
                      animation: `pulse ${Math.random() * 2 + 1}s infinite`
                    }}
                  />
                ))}
              </div>
              <div className="text-center z-10 text-blue-300">
                <div className="text-xl">Auditory Fracture Pattern</div>
                <div className="text-sm mt-2">Harmonic Disruption Level: {(glitch.intensity * 100).toFixed(1)}%</div>
              </div>
            </div>
          )}
          
          {glitch.type === 'SPATIAL' && (
            <div className="w-full h-full flex items-center justify-center perspective-500">
              <div className="relative w-32 h-32 transform-3d animate-spin-slow">
                <div className="absolute inset-0 border border-blue-500/60 transform rotate-x-45" />
                <div className="absolute inset-0 border border-purple-500/60 transform rotate-y-45" />
                <div className="absolute inset-0 border border-cyan-500/60 transform rotate-z-45" />
              </div>
              <div className="absolute inset-0 flex items-center justify-center">
                <div className="text-center z-10 text-blue-300">
                  <div className="text-xl">Spatial Fracture Pattern</div>
                  <div className="text-sm mt-2">Euclidean Variance: {(glitch.intensity * 100).toFixed(1)}%</div>
                </div>
              </div>
            </div>
          )}

          {glitch.type === 'TEMPORAL' && (
            <div className="w-full h-full flex items-center justify-center">
              <div className="absolute inset-0 flex items-center justify-center">
                <div className="w-40 h-40 rounded-full border-4 border-t-cyan-500 border-r-purple-500 border-b-blue-500 border-l-green-500 animate-spin" />
                <div className="absolute w-32 h-32 rounded-full border-2 border-dashed border-blue-400 animate-spin-reverse" />
                <div className="absolute w-24 h-24 rounded-full border border-purple-400 animate-pulse" />
              </div>
              <div className="text-center z-10 text-blue-300">
                <div className="text-xl">Temporal Fracture Pattern</div>
                <div className="text-sm mt-2">Chronological Distortion: {(glitch.intensity * 100).toFixed(1)}%</div>
              </div>
            </div>
          )}

          {glitch.type === 'COGNITIVE' && (
            <div className="w-full h-full flex items-center justify-center">
              <div className="absolute inset-0 flex flex-wrap justify-center items-center">
                {[...Array(15)].map((_, i) => (
                  <div 
                    key={i}
                    className="mx-1 text-blue-400 opacity-70"
                    style={{
                      fontSize: `${12 + Math.random() * 16}px`,
                      animation: `pulse ${Math.random() * 3 + 1}s infinite`,
                      transform: `rotate(${Math.random() * 40 - 20}deg)`
                    }}
                  >
                    思想
                  </div>
                ))}
              </div>
              <div className="text-center z-10 text-blue-300">
                <div className="text-xl">Cognitive Fracture Pattern</div>
                <div className="text-sm mt-2">Neural Disruption: {(glitch.intensity * 100).toFixed(1)}%</div>
              </div>
            </div>
          )}

          {glitch.type === 'SYNCHRONISTIC' && (
            <div className="w-full h-full flex items-center justify-center">
              <div className="absolute inset-0">
                <div className="grid grid-cols-3 grid-rows-3 h-full w-full">
                  {[...Array(9)].map((_, i) => (
                    <div key={i} className="border border-blue-800/30 flex items-center justify-center">
                      <div 
                        className="w-4 h-4 rounded-full bg-blue-500"
                        style={{
                          animation: `pulse ${1 + (i % 3) * 0.5}s infinite alternate`,
                          animationDelay: `${i * 0.1}s`
                        }}
                      />
                    </div>
                  ))}
                </div>
              </div>
              <div className="text-center z-10 text-blue-300">
                <div className="text-xl">Synchronistic Fracture Pattern</div>
                <div className="text-sm mt-2">Coincidence Amplitude: {(glitch.intensity * 100).toFixed(1)}%</div>
              </div>
            </div>
          )}
        </div>
        
        {!glitch.active && (
          <div className="absolute inset-0 flex items-center justify-center bg-black/70 text-red-500 font-bold">
            INACTIVE
          </div>
        )}
      </div>
    </div>
  );
};

export default GlitchVisualization; 