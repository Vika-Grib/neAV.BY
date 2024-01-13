import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import axios from 'axios';
import App from './App';
import reportWebVitals from './reportWebVitals';

axios.defaults.withCredentials = true; // Включаем передачу куки

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);


