import React, { useState, useEffect, useRef } from 'react';
import { v4 as uuidv4 } from 'uuid';
import '../RealityGlitcher.css';
import IntensitySlider from './ScrollWheel';
import RealTimeData from './RealTimeData';
import GlitchCard from './GlitchCard';
import CreateGlitchModal from './CreateGlitchModal';

// Set a fixed maximum height constant for the control panel
const MAX_CONTROL_PANEL_HEIGHT = 1116;

const RealityGlitcherUI = () => {
  // State for reality status
  const [realityStatus, setRealityStatus] = useState({
    coherence: 'STABLE',
    stability: 0.85,
    safetyProtocols: true,
    activeSince: new Date().getTime()
  });

  // State for glitches
  const [glitches, setGlitches] = useState([
    { 
      id: uuidv4(), 
      type: 'VISUAL', 
      intensity: 0.4, 
      duration: 5, 
      complexity: 0.3, 
      persistence: 0.5, 
      active: true, 
      target: 'Visual Field',
      source: 'Manual Creation' 
    },
    { 
      id: uuidv4(), 
      type: 'AUDITORY', 
      intensity: 0.3, 
      duration: 3, 
      complexity: 0.2, 
      persistence: 0.3, 
      active: false, 
      target: 'Auditory Processing',
      source: 'Manual Creation'
    }
  ]);
  
  // State for selected glitch
  const [selectedGlitch, setSelectedGlitch] = useState(null);
  
  // State for modal
  const [modalOpen, setModalOpen] = useState(false);
  
  // State for console messages
  const [consoleMessages, setConsoleMessages] = useState([
    { text: 'Reality Glitcher initialized', timestamp: new Date().getTime(), type: 'info' },
    { text: 'Safety protocols active', timestamp: new Date().getTime(), type: 'success' },
    { text: 'Ready to manipulate perception', timestamp: new Date().getTime(), type: 'info' }
  ]);

  // Mind Mirror Integration State
  const [mindMirrorIntegrated, setMindMirrorIntegrated] = useState(false);
  const [mindMirrorStatus, setMindMirrorStatus] = useState({
    connected: false,
    nodeCount: 0,
    connectionCount: 0,
    lastSyncTime: null
  });

  // Refs for containers
  const glitchListRef = useRef(null);
  const controlPanelRef = useRef(null);
  const resizeObserverRef = useRef(null);
  
  // State to track if glitch list is scrollable
  const [isGlitchListScrollable, setIsGlitchListScrollable] = useState(false);
  
  // State to store the control panel's height
  const [controlPanelHeight, setControlPanelHeight] = useState(MAX_CONTROL_PANEL_HEIGHT);

  // Refs
  const consoleRef = useRef(null);
  
  // Function to add console message
  const addConsoleMessage = (text, type = 'info') => {
    const newMessage = {
      text,
      timestamp: new Date().getTime(),
      type
    };
    setConsoleMessages(prev => [...prev, newMessage]);
  };
  
  // Scroll console to bottom when messages change
  useEffect(() => {
    if (consoleRef.current) {
      consoleRef.current.scrollTop = consoleRef.current.scrollHeight;
    }
  }, [consoleMessages]);
  
  // Function to toggle safety protocols
  const toggleSafetyProtocols = () => {
    setRealityStatus(prev => ({
      ...prev,
      safetyProtocols: !prev.safetyProtocols
    }));
    
    addConsoleMessage(
      `Safety protocols ${realityStatus.safetyProtocols ? 'deactivated' : 'activated'}`,
      realityStatus.safetyProtocols ? 'warning' : 'success'
    );
    
    // If turning off safety, reduce stability
    if (realityStatus.safetyProtocols) {
      setRealityStatus(prev => ({
        ...prev,
        stability: Math.max(0.3, prev.stability - 0.2),
        coherence: 'FLUCTUATING'
      }));
      addConsoleMessage('WARNING: Reality stability compromised', 'warning');
    }
  };
  
  // Function to create a new glitch
  const createGlitch = (glitchData) => {
    const newGlitch = {
      id: uuidv4(),
      ...glitchData,
      active: false,
      source: 'Manual Creation'
    };
    
    setGlitches(prev => [...prev, newGlitch]);
    addConsoleMessage(`New ${newGlitch.type} glitch created`, 'success');
    setModalOpen(false);
  };
  
  // Function to toggle glitch active state
  const toggleGlitch = (id) => {
    setGlitches(prev => 
      prev.map(glitch => 
        glitch.id === id 
          ? { ...glitch, active: !glitch.active } 
          : glitch
      )
    );
    
    const glitch = glitches.find(g => g.id === id);
    if (glitch) {
      addConsoleMessage(
        `Glitch ${glitch.id.substring(0, 8)} ${glitch.active ? 'deactivated' : 'activated'}`,
        'info'
      );
      
      // Update reality status based on active glitches
      updateRealityStatus();
    }
  };
  
  // Function to adjust glitch intensity
  const adjustIntensity = (id, newIntensity) => {
    setGlitches(prev => 
      prev.map(glitch => 
        glitch.id === id 
          ? { ...glitch, intensity: newIntensity } 
          : glitch
      )
    );
    
    // Update reality status based on glitch intensity
    updateRealityStatus();
  };
  
  // Function to amplify glitch (increase intensity by 10%)
  const amplifyGlitch = (id) => {
    setGlitches(prev => 
      prev.map(glitch => 
        glitch.id === id 
          ? { ...glitch, intensity: Math.min(1, glitch.intensity + 0.1) } 
          : glitch
      )
    );
    
    addConsoleMessage(`Amplifying glitch intensity`, 'info');
    updateRealityStatus();
  };
  
  // Function to update reality status based on active glitches
  const updateRealityStatus = () => {
    const activeGlitches = glitches.filter(g => g.active);
    const totalIntensity = activeGlitches.reduce((sum, g) => sum + g.intensity, 0);
    
    let newStability = 0.95 - (totalIntensity * 0.15);
    let newCoherence = 'STABLE';
    
    if (!realityStatus.safetyProtocols) {
      newStability -= 0.2;
    }
    
    if (newStability < 0.4) {
      newCoherence = 'UNSTABLE';
    } else if (newStability < 0.7) {
      newCoherence = 'FLUCTUATING';
    }
    
    setRealityStatus(prev => ({
      ...prev,
      stability: Math.max(0.1, newStability),
      coherence: newCoherence
    }));
  };
  
  // Function to integrate with Mind Mirror
  const integrateWithMindMirror = () => {
    // If already integrated, do nothing
    if (mindMirrorIntegrated) return;
    
    addConsoleMessage('Attempting to connect to Mind Mirror...', 'info');
    
    // Simulate connection process
    setMindMirrorStatus({
      connected: false,
      nodeCount: 0,
      connectionCount: 0,
      lastSyncTime: null
    });
    
    // Simulate async connection process
    setTimeout(() => {
      // Random chance of connection failure (20%)
      const connectionSuccessful = Math.random() > 0.2;
      
      if (connectionSuccessful) {
        // Update Mind Mirror status
        const nodeCount = Math.floor(Math.random() * 50) + 100; // 100-150 nodes
        const connectionCount = Math.floor(nodeCount * (Math.random() * 0.4 + 0.6)); // 60-100% of nodes
        
        setMindMirrorStatus({
          connected: true,
          nodeCount,
          connectionCount,
          lastSyncTime: new Date().getTime()
        });
        
        setMindMirrorIntegrated(true);
        addConsoleMessage('Mind Mirror successfully connected', 'success');
        addConsoleMessage(`Detected ${nodeCount} neural nodes and ${connectionCount} connections`, 'info');
        
        // Generate glitches based on mind mirror data
        const mindMirrorGlitchCount = Math.floor(Math.random() * 3) + 1; // 1-3 glitches
        
        const newGlitches = [];
        const glitchTypes = ['VISUAL', 'AUDITORY', 'COGNITIVE', 'TEMPORAL', 'SPATIAL'];
        const targets = [
          'Visual Processing Center', 
          'Auditory Cortex', 
          'Frontal Lobe Activity',
          'Temporal Perception',
          'Spatial Awareness',
          'Memory Imprints',
          'Emotional Responses'
        ];
        
        for (let i = 0; i < mindMirrorGlitchCount; i++) {
          const type = glitchTypes[Math.floor(Math.random() * glitchTypes.length)];
          const target = targets[Math.floor(Math.random() * targets.length)];
          
          newGlitches.push({
            id: uuidv4(),
            type,
            intensity: Math.random() * 0.5 + 0.2, // 0.2-0.7 intensity
            duration: Math.random() * 10 + 5, // 5-15 seconds
            complexity: Math.random() * 0.6 + 0.2, // 0.2-0.8 complexity
            persistence: Math.random() * 0.4 + 0.1, // 0.1-0.5 persistence
            active: true,
            target,
            source: 'Mind Mirror'
          });
        }
        
        // Add new glitches to state
        setGlitches(prev => [...prev, ...newGlitches]);
        
        // Update reality status to reflect mind mirror connection
        setRealityStatus(prev => ({
          ...prev,
          coherence: 'FLUCTUATING',
          stability: Math.max(0.3, prev.stability - 0.15)
        }));
        
        addConsoleMessage(`Generated ${newGlitches.length} glitches from consciousness patterns`, 'success');
      } else {
        // Connection failed
        addConsoleMessage('ERROR: Failed to establish neural connection with Mind Mirror', 'error');
        setMindMirrorStatus({
          connected: false,
          nodeCount: 0,
          connectionCount: 0,
          lastSyncTime: null
        });
      }
    }, 2000);
  };

  // Function to check if the glitch list container has overflow compared to control panel
  const checkGlitchListOverflow = () => {
    if (glitchListRef.current) {
      // Get the content height of the glitch list
      const { scrollHeight } = glitchListRef.current;
      
      // Check if list content is taller than the max control panel height
      setIsGlitchListScrollable(scrollHeight > MAX_CONTROL_PANEL_HEIGHT);
    }
  };

  // Effect to simulate reality fluctuations
  useEffect(() => {
    const timer = setInterval(() => {
      // Calculate new stability based on active glitches
      const activeGlitches = glitches.filter(g => g.active);
      let newStability = 0.95 - (activeGlitches.length * 0.05);
      
      // Add some randomness
      newStability += (Math.random() * 0.1) - 0.05;
      newStability = Math.max(0.1, Math.min(0.95, newStability));
      
      setRealityStatus(prev => ({
        ...prev,
        stability: newStability,
        coherence: newStability > 0.7 ? 'STABLE' : 
                 newStability > 0.4 ? 'UNSTABLE' : 'CRITICAL'
      }));
    }, 3000);
    
    return () => clearInterval(timer);
  }, [glitches]);

  // Effect to check overflow whenever glitches change
  useEffect(() => {
    // Small delay to ensure DOM is updated first
    const timer = setTimeout(checkGlitchListOverflow, 50);
    return () => clearTimeout(timer);
  }, [glitches]);

  // Initial check after mount
  useEffect(() => {
    checkGlitchListOverflow();
    // Add resize listener to adjust scrollability on window resize
    window.addEventListener('resize', checkGlitchListOverflow);
    return () => {
      window.removeEventListener('resize', checkGlitchListOverflow);
    };
  }, []);

  return (
    <div className="bg-black text-blue-300 p-6 font-mono cyber-bg" style={{minHeight: '100%', paddingBottom: '60px'}}>
      {/* Header with glitch effect */}
      <header className="text-center mb-8">
        <h1 className="text-3xl font-bold bg-gradient-to-r from-purple-400 via-blue-500 to-purple-400 bg-clip-text text-transparent cyber-text-glow visual-glitch" data-text="PROJECT89 REALITY GLITCHER">
          PROJECT89 REALITY GLITCHER
        </h1>
        <div className="mt-2 text-sm text-blue-400">Perception Manipulation Interface v3.9.1</div>
      </header>
      
      {/* Reality Status Dashboard */}
      <div className="mb-8 p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
        <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Reality Status</h2>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <div className="text-sm text-blue-400">Coherence Status:</div>
            <div className={`text-lg font-bold ${
              realityStatus.coherence === 'STABLE' ? 'text-green-400' : 
              realityStatus.coherence === 'FLUCTUATING' ? 'text-yellow-400' : 
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
            <div 
              className={`text-lg font-bold ${realityStatus.safetyProtocols ? 'text-green-400' : 'text-red-400'} cursor-pointer`}
              onClick={toggleSafetyProtocols}
            >
              {realityStatus.safetyProtocols ? 'ACTIVE' : 'DISABLED'}
            </div>
          </div>
          <div>
            <div className="text-sm text-blue-400">Session Active Since:</div>
            <div className="text-lg font-bold">{new Date(realityStatus.activeSince).toLocaleTimeString()}</div>
          </div>
        </div>
        
        {/* Stability Bar */}
        <div className="mt-4">
          <div className="h-2 w-full bg-gray-800 rounded overflow-hidden">
            <div 
              className={`h-full transition-all duration-1000 ${
                realityStatus.stability > 0.7 ? 'bg-green-500' : 
                realityStatus.stability > 0.4 ? 'bg-yellow-500' : 
                'bg-red-500'
              }`}
              style={{width: `${realityStatus.stability * 100}%`}}
            />
          </div>
        </div>
        
        {/* Mind Mirror Integration Status */}
        <div className="mt-5 border-t border-blue-800 pt-3">
          <div className="flex justify-between items-center mb-2">
            <div className="text-sm text-blue-400">Mind Mirror Integration:</div>
            <div className={`text-sm font-bold ${mindMirrorStatus.connected ? 'text-purple-400' : 'text-gray-500'}`}>
              {mindMirrorStatus.connected ? 'CONNECTED' : 'DISCONNECTED'}
            </div>
          </div>
          
          {mindMirrorStatus.connected && (
            <div className="grid grid-cols-2 gap-3 text-xs mt-2">
              <div>
                <span className="text-purple-400">Neural Nodes:</span> {mindMirrorStatus.nodeCount}
              </div>
              <div>
                <span className="text-purple-400">Connections:</span> {mindMirrorStatus.connectionCount}
              </div>
              <div className="col-span-2">
                <span className="text-purple-400">Last Sync:</span> {new Date(mindMirrorStatus.lastSyncTime).toLocaleTimeString()}
              </div>
            </div>
          )}
          
          <button 
            className={`mt-2 w-full py-2 rounded text-center ${
              mindMirrorIntegrated 
                ? 'bg-purple-800/50 border border-purple-600 text-purple-200' 
                : 'bg-blue-800/50 border border-blue-600 hover:bg-blue-700/50'
            }`}
            onClick={integrateWithMindMirror}
            disabled={mindMirrorIntegrated}
          >
            {mindMirrorIntegrated ? 'NEURAL LINK ACTIVE' : 'CONNECT TO MIND MIRROR'}
          </button>
        </div>
      </div>
      
      {/* Real-time Data Visualization */}
      <div className="mb-8 p-4 border border-blue-800 rounded-lg bg-gradient-to-b from-blue-900/30 to-purple-900/30 cyber-border">
        <h2 className="text-xl mb-3 border-b border-blue-700 pb-1">Quantum Fluctuation Analysis</h2>
        <RealTimeData 
          glitches={glitches} 
          realityStatus={realityStatus} 
          mindMirrorConnected={mindMirrorStatus.connected}
        />
      </div>
      
      {/* Main Content Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Glitch List Panel */}
        <div className="col-span-1">
          <div className="bg-blue-900/20 p-4 rounded-lg border border-blue-800 cyber-border h-full">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-lg font-semibold text-blue-200">Active Glitches</h2>
              <button 
                className="cyber-button cyber-button-primary px-3 py-1 rounded text-xs"
                onClick={() => setModalOpen(true)}
              >
                NEW GLITCH
              </button>
            </div>
            
            <div className="space-y-3 max-h-[400px] overflow-y-auto scrollbar pr-2">
              {glitches.map(glitch => (
                <GlitchCard
                  key={glitch.id}
                  glitch={glitch}
                  isSelected={selectedGlitch?.id === glitch.id}
                  onSelect={() => setSelectedGlitch(glitch)}
                  onToggle={() => toggleGlitch(glitch.id)}
                />
              ))}
              
              {glitches.length === 0 && (
                <div className="text-center text-blue-500 italic py-4">
                  No active glitches. Create one to begin.
                </div>
              )}
            </div>
          </div>
        </div>

        {/* Middle Panel: Controls and Visualization */}
        <div className="col-span-1">
          <div className="bg-blue-900/20 p-4 rounded-lg border border-blue-800 cyber-border h-full">
            <h2 className="text-lg font-semibold text-blue-200 mb-4">Reality Manipulation</h2>
            
            {selectedGlitch ? (
              <>
                <div className="mb-4">
                  <h3 className="text-sm text-blue-400 mb-1">Selected Glitch:</h3>
                  <div className="font-bold text-lg">{selectedGlitch.type} #{selectedGlitch.id.substring(0, 8)}</div>
                  <div className="text-xs text-blue-400 mt-1">
                    {selectedGlitch.source === 'Mind Mirror' ? 'Source: Mind Mirror' : 'Source: Manual Creation'}
                  </div>
                </div>
                
                <div className="mb-6">
                  <label className="text-sm text-blue-400 block mb-1">Intensity Control</label>
                  <input
                    type="range"
                    min="1"
                    max="100"
                    value={selectedGlitch.intensity * 100}
                    onChange={(e) => adjustIntensity(selectedGlitch.id, e.target.value / 100)}
                    className="w-full accent-blue-500 cyber-slider"
                  />
                  <div className="flex justify-between text-xs mt-1">
                    <span>Subtle</span>
                    <span>Intense</span>
                  </div>
                </div>
                
                <div className="flex space-x-2 mb-4">
                  <button
                    className={`flex-1 py-2 rounded text-sm ${selectedGlitch.active ? 'bg-green-800/50 text-green-300' : 'bg-blue-800/50 hover:bg-blue-700/50'}`}
                    onClick={() => toggleGlitch(selectedGlitch.id)}
                  >
                    {selectedGlitch.active ? 'DEACTIVATE' : 'ACTIVATE'}
                  </button>
                  <button
                    className="flex-1 py-2 rounded text-sm bg-purple-800/50 hover:bg-purple-700/50"
                    onClick={() => amplifyGlitch(selectedGlitch.id)}
                  >
                    AMPLIFY
                  </button>
                </div>
                
                {/* Visualization */}
                <div className="h-40 flex items-center justify-center">
                  <div 
                    className={`rounded-full transition-all duration-1000 flex items-center justify-center ${
                      selectedGlitch.type === 'VISUAL' ? 'bg-purple-600/50' :
                      selectedGlitch.type === 'AUDITORY' ? 'bg-green-600/50' :
                      selectedGlitch.type === 'TEMPORAL' ? 'bg-yellow-600/50' :
                      selectedGlitch.type === 'SPATIAL' ? 'bg-blue-600/50' :
                      selectedGlitch.type === 'COGNITIVE' ? 'bg-red-600/50' :
                      'bg-indigo-600/50'
                    }`}
                    style={{
                      width: `${Math.max(40, selectedGlitch.intensity * 150)}px`,
                      height: `${Math.max(40, selectedGlitch.intensity * 150)}px`,
                      filter: `blur(${selectedGlitch.intensity * 5}px) brightness(1.2)`,
                      opacity: selectedGlitch.active ? 1 : 0.3
                    }}
                  >
                    <div className="text-xs">{selectedGlitch.active ? 'ACTIVE' : 'INACTIVE'}</div>
                  </div>
                </div>
              </>
            ) : (
              <div className="text-center text-blue-500 italic h-64 flex items-center justify-center">
                Select a glitch to view controls
              </div>
            )}
          </div>
        </div>

        {/* Right Panel: Console Output */}
        <div className="col-span-1">
          <div className="bg-blue-900/20 p-4 rounded-lg border border-blue-800 cyber-border h-full">
            <h2 className="text-lg font-semibold text-blue-200 mb-2">System Console</h2>
            
            <div 
              ref={consoleRef}
              className="font-mono text-xs h-[400px] overflow-y-auto bg-black/50 p-3 rounded terminal-bg scrollbar"
            >
              {consoleMessages.map((msg, i) => (
                <div 
                  key={i} 
                  className={`mb-1 ${
                    msg.type === 'error' ? 'text-red-400' : 
                    msg.type === 'warning' ? 'text-yellow-400' : 
                    msg.type === 'success' ? 'text-green-400' : 
                    'text-blue-300'
                  }`}
                >
                  [{new Date(msg.timestamp).toLocaleTimeString()}] {msg.text}
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Create Glitch Modal */}
      {modalOpen && (
        <CreateGlitchModal 
          isOpen={modalOpen}
          onClose={() => setModalOpen(false)}
          onCreateGlitch={createGlitch}
        />
      )}
    </div>
  );
};

export default RealityGlitcherUI;