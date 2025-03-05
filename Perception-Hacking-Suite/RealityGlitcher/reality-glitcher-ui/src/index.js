import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import './tailwind.css';
import './custom.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

// Create a root
const container = document.getElementById('root');
const root = createRoot(container);

// Render app to root
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();