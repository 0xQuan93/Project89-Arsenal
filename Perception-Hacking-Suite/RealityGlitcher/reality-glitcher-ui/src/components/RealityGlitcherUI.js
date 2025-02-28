import React, { useState, useEffect } from 'react';

const RealityGlitcherUI = () => {
  const [glitches, setGlitches] = useState([
    { id: 'g-001', type: 'VISUAL', intensity: 0.7, stability: 0.65, active: true },
    { id: 'g-002', type: 'AUDITORY', intensity: 0.4, stability: 0.82, active: false },
    { id: 'g-003', type: 'SPATIAL', intensity: 0.55, stability: 0.75, active: true },
  ]);
  
  const [realityStatus, setRealityStatus] = useState({
    stability: 0.73,
    coherence: 'STABLE',
    safetyProtocols: true,
    activeSince: '2025-02-26T21:34:12'
  });
  
  const [selectedGlitch, setSelectedGlitch] = useState(null);
  
  useEffect(() => {
    // Simulate reality fluctuations
    const timer = setInterval(() => {
      setRealityStatus(prev => ({
        ...prev,
        stability: Math.max(0.1, Math.min(0.98, prev.stability + (Math.random() * 0.1 - 0.05))),
      }));
    }, 3000);
    
    return () => clearInterval(timer);
  }, []);
  
  useEffect(() => {
    // Update coherence status based on stability
    setRealityStatus(prev => ({
      ...prev,
      coherence: prev.stability > 0.7 ? 'STABLE' : 
                prev.stability > 0.4 ? 'UNSTABLE' : 'CRITICAL'
    }));
  }, [realityStatus.stability]);
  
  const handleGlitchSelect = (glitch) => {
    setSelectedGlitch(glitch);
  };
  
  const toggleGlitch = (id) => {
    setGlitches(prev => 
      prev.map(g => g.id === id ? {...g, active: !g.active} : g)
    );
  };
  
  return (
    <div className="min-h-screen bg-black text-blue-300 p-6 font-mono">
      {/* Header */}
      <header className="text-center mb-8">
        <h1 className="text-3xl font-bold bg-gradient-to-r from-purple-400 via-blue-500 to-purple-400 bg-clip-text text-transparent">PROJECT89 REALITY GLITCHER</h1>
        <div className="mt-2 text-sm text-blue-400">Perception Manipulation Interface v3.9.1</div>
      </header>
      
      {/* Reality Status Display */}
      <div className="mb-8 p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30">
        <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Reality Status</h2>
        <div className="grid grid-cols-2 gap-2">
          <div>
            <div className="text-sm text-blue-400">Coherence Status:</div>
            <div className={`text-lg font-bold ${
              realityStatus.coherence === 'STABLE' ? 'text-green-400' : 
              realityStatus.coherence === 'UNSTABLE' ? 'text-yellow-400' : 
              'text-red-400 animate-pulse'
            }`}>
              {realityStatus.coherence}
            </div>
          </div>
          <div>
            <div className="text-sm text-blue-400">Stability Index:</div>
            <div className="text-lg font-bold">{(realityStatus.stability * 100).toFixed(1)}%</div>
          </div>
          <div>
            <div className="text-sm text-blue-400">Safety Protocols:</div>
            <div className={`text-lg font-bold ${realityStatus.safetyProtocols ? 'text-green-400' : 'text-red-400'}`}>
              {realityStatus.safetyProtocols ? 'ACTIVE' : 'DISABLED'}
            </div>
          </div>
          <div>
            <div className="text-sm text-blue-400">Session Active Since:</div>
            <div className="text-lg font-bold">{new Date(realityStatus.activeSince).toLocaleTimeString()}</div>
          </div>
        </div>
        
        {/* Stability Visualization */}
        <div className="mt-4">
          <div className="h-2 w-full bg-gray-800 rounded overflow-hidden">
            <div 
              className={`h-full ${
                realityStatus.stability > 0.7 ? 'bg-green-500' : 
                realityStatus.stability > 0.4 ? 'bg-yellow-500' : 
                'bg-red-500'
              }`}
              style={{width: `${realityStatus.stability * 100}%`}}
            />
          </div>
        </div>
      </div>
      
      {/* Main Content Area */}
      <div className="flex flex-col lg:flex-row gap-6">
        {/* Glitch List */}
        <div className="lg:w-1/2 p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30">
          <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Active Glitches</h2>
          <div className="space-y-3">
            {glitches.map(glitch => (
              <div 
                key={glitch.id}
                className={`p-3 border rounded-md cursor-pointer transition 
                  ${selectedGlitch?.id === glitch.id ? 'border-blue-400 bg-blue-900/40' : 'border-blue-800 hover:border-blue-600'}
                  ${glitch.active ? 'opacity-100' : 'opacity-50'}`}
                onClick={() => handleGlitchSelect(glitch)}
              >
                <div className="flex justify-between items-center">
                  <div className="font-bold">{glitch.id} <span className="text-xs ml-2 text-blue-400">{glitch.type}</span></div>
                  <div>
                    <button 
                      className={`px-2 py-1 rounded text-xs ${glitch.active ? 'bg-green-700 text-green-200' : 'bg-red-900 text-red-200'}`}
                      onClick={(e) => {
                        e.stopPropagation();
                        toggleGlitch(glitch.id);
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
            ))}
          </div>
          <div className="mt-4">
            <button className="w-full p-2 border border-blue-600 rounded-md bg-blue-900/50 text-blue-300 hover:bg-blue-800/50 transition">
              ✧ CREATE NEW GLITCH ✧
            </button>
          </div>
        </div>
        
        {/* Glitch Details / Visualization */}
        <div className="lg:w-1/2 p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30">
          <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Glitch Visualization</h2>
          
          {selectedGlitch ? (
            <div>
              <div className="mb-4">
                <h3 className="text-lg font-bold">{selectedGlitch.type} Glitch {selectedGlitch.id}</h3>
                <div className="text-sm text-blue-400">Induced fracture in perception matrix</div>
              </div>
              
              {/* Visualization */}
              <div className="relative h-64 border border-blue-800 rounded bg-black/50 overflow-hidden">
                <div className={`absolute inset-0 flex items-center justify-center ${!selectedGlitch.active && 'opacity-30'}`}>
                  {selectedGlitch.type === 'VISUAL' && (
                    <div className="w-full h-full flex items-center justify-center">
                      <div className="absolute w-32 h-32 rounded-full bg-purple-500/30 animate-pulse"/>
                      <div className="absolute w-48 h-48 rounded-full border border-blue-500/60 animate-spin"/>
                      <div className="absolute w-64 h-64 rounded-full border border-cyan-500/40 animate-pulse"/>
                      <div className="text-center z-10 text-blue-300">
                        <div className="text-xl">Visual Fracture Pattern</div>
                        <div className="text-sm mt-2">Coherence: {(selectedGlitch.stability * 100).toFixed(1)}%</div>
                      </div>
                    </div>
                  )}
                  
                  {selectedGlitch.type === 'AUDITORY' && (
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
                        <div className="text-sm mt-2">Harmonic Disruption Level: {(selectedGlitch.intensity * 100).toFixed(1)}%</div>
                      </div>
                    </div>
                  )}
                  
                  {selectedGlitch.type === 'SPATIAL' && (
                    <div className="w-full h-full flex items-center justify-center perspective-500">
                      <div className="relative w-32 h-32 transform-3d animate-spin-slow">
                        <div className="absolute inset-0 border border-blue-500/60 transform rotate-x-45" />
                        <div className="absolute inset-0 border border-purple-500/60 transform rotate-y-45" />
                        <div className="absolute inset-0 border border-cyan-500/60 transform rotate-z-45" />
                      </div>
                      <div className="absolute inset-0 flex items-center justify-center">
                        <div className="text-center z-10 text-blue-300">
                          <div className="text-xl">Spatial Fracture Pattern</div>
                          <div className="text-sm mt-2">Euclidean Variance: {(selectedGlitch.intensity * 100).toFixed(1)}%</div>
                        </div>
                      </div>
                    </div>
                  )}
                </div>
                
                {!selectedGlitch.active && (
                  <div className="absolute inset-0 flex items-center justify-center bg-black/70 text-red-500 font-bold">
                    INACTIVE
                  </div>
                )}
              </div>
              
              {/* Controls */}
              <div className="mt-4 flex flex-wrap gap-2">
                <button className="px-3 py-1 border border-blue-600 rounded-md bg-blue-900/50 text-blue-300 hover:bg-blue-800/50 transition">
                  Amplify
                </button>
                <button className="px-3 py-1 border border-blue-600 rounded-md bg-blue-900/50 text-blue-300 hover:bg-blue-800/50 transition">
                  Modulate
                </button>
                <button className="px-3 py-1 border border-blue-600 rounded-md bg-blue-900/50 text-blue-300 hover:bg-blue-800/50 transition">
                  Stabilize
                </button>
                <button className="px-3 py-1 border border-red-800 rounded-md bg-red-900/30 text-red-300 hover:bg-red-800/50 transition">
                  Terminate
                </button>
              </div>
            </div>
          ) : (
            <div className="h-64 flex items-center justify-center text-blue-500 border border-blue-900 rounded bg-black/50">
              <div className="text-center">
                <div className="text-xl">Select a glitch to visualize</div>
                <div className="text-sm mt-2">No active visualization</div>
              </div>
            </div>
          )}
        </div>
      </div>
      
      {/* Console Output */}
      <div className="mt-6 p-4 border border-blue-800 rounded-lg bg-black/70 h-32 overflow-y-auto font-mono text-xs">
        <div className="text-green-400">✧ 2025-02-27 13:42:18 ┃ INFO ┃ Reality Glitcher initialized | Session: a32f5c ✧</div>
        <div className="text-blue-400">✧ 2025-02-27 13:42:19 ┃ INFO ┃ Glitch g-001 activated in consensus_reality. Reality fracture detected. ✧</div>
        <div className="text-blue-400">✧ 2025-02-27 13:42:19 ┃ INFO ┃ Stability rating: 0.65 | Safety anchor: ✧anchor_g-001✦ ✧</div>
        <div className="text-yellow-300">✧ 2025-02-27 13:42:20 ┃ WARNING ┃ Potential reality cascade detected, contained at perception boundary ✧</div>
        <div className="text-blue-400">✧ 2025-02-27 13:42:45 ┃ INFO ┃ Glitch g-003 activated in consensus_reality. Reality fracture detected. ✧</div>
        <div className="text-red-400">✧ 2025-02-27 13:43:12 ┃ ERROR ┃ Glitch g-002 deactivated due to stability threshold breach ✧</div>
      </div>
    </div>
  );
};

export default RealityGlitcherUI;