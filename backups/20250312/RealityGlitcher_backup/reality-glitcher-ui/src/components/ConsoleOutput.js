import React, { useRef, useEffect } from 'react';

const ConsoleOutput = ({ messages }) => {
  const consoleRef = useRef(null);

  // Auto-scroll to bottom of console when new messages arrive
  useEffect(() => {
    if (consoleRef.current) {
      consoleRef.current.scrollTop = consoleRef.current.scrollHeight;
    }
  }, [messages]);

  // Determine message type and apply appropriate styling
  const getMessageClass = (message) => {
    if (message.includes('ERROR')) return 'text-red-400';
    if (message.includes('WARNING')) return 'text-yellow-300';
    if (message.includes('INFO')) return 'text-blue-400';
    if (message.includes('initialized')) return 'text-green-400';
    return 'text-blue-400';
  };

  return (
    <div 
      ref={consoleRef}
      className="p-4 border border-blue-800 rounded-lg bg-black/70 h-32 overflow-y-auto font-mono text-xs"
    >
      {messages.map((message, index) => (
        <div key={index} className={getMessageClass(message)}>
          {message}
        </div>
      ))}
      {messages.length === 0 && (
        <div className="text-blue-700 italic">Console ready. No messages to display.</div>
      )}
    </div>
  );
};

export default ConsoleOutput; 