import React from 'react';
import { BrowserRouter as Router, Route, Routes, Switch, Link, useParams } from 'react-router-dom';
import CarList from './CarList';
import CarDetail from './CarDetail';


export default function App() {
  return (
  <Router>
    <div className="App">
    <h1>Объявления о продаже авто</h1>
    <Link to="/api/v1/mainapp/all/">Car List</Link>

    <Routes>
        <Route path="/api/v1/mainapp/all/" element={<CarList />} />
        <Route path="/api/v1/mainapp/car/detail/car.id" element={<CarDetail />} />
    </Routes>


    </div>
  </Router>
  );
}


