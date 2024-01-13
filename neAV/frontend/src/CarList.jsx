import React, { useEffect, useState } from 'react';
import axios from 'axios';
// import Map from './Map';
import { Link } from 'react-router-dom';

const CarList = () => {
  const [cars, setCars] = useState([]);

  useEffect(() => {
    const fetchCars = async () => {
      try {
        const response = await axios.get('/api/v1/mainapp/all/');
        console.log(response)
        setCars(response.data.results);
      } catch (error) {
        console.error('Ошибка при получении списка автомобилей', error);
      }
    };

    fetchCars();
  }, []);
  console.log(cars)
  if (!cars.length) {
    return <div>Загрузка списка автомобилей...</div>;
  }

  return (
    <div>
      <h2>Список автомобилей</h2>
      <ul>
        {cars.map((car) => (
          <li key={car.id}>
            <p>Марка авто: {car.brand}</p>
            <p>Модель авто: {car.model}</p>
            <p>Цвет авто: {car.color}</p>
            <Link to={`/api/v1/mainapp/car/detail/${car.id}`}>Подробнее</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CarList;
