// CarAdvertList.jsx
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const CarAdvertList = () => {
  const [adverts, setAdverts] = useState([]);

  useEffect(() => {
    const fetchAdverts = async () => {
      try {
        const response = await axios.get('/api/v1/mainapp/car/advert/');
        setAdverts(response.data.results);
      } catch (error) {
        console.error('Ошибка при получении списка объявлений', error);
      }
    };

    fetchAdverts();
  }, []);

  if (!adverts.length) {
    return <div>Загрузка списка объявлений...</div>;
  }

  return (
    <div>
      <h2>Список объявлений</h2>
      <ul>
        {adverts.map((advert) => (
          <li key={advert.id}>
            <p>Марка авто: {advert.brand}</p>
            <p>Модель авто: {advert.model}</p>
            <p>Цвет авто: {advert.color}</p>
            <Link to={`/api/v1/mainapp/car/advert/${advert.id}`}>Подробнее</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default CarAdvertList;
