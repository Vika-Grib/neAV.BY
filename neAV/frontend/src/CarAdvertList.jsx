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
    <div style={advertsContainerStyle}>
      <h2>Список объявлений</h2>
      <div style={advertsListStyle}>
        {adverts.map((advert) => (
          <div key={advert.id} style={advertBlockStyle}>
            {advert.photo && (
              <div>
                <img
                  src={`http://127.0.0.1:8000${advert.photo}`}  // Обновите URL в соответствии с вашей конфигурацией Django
//                   alt={`${advert.brand} ${advert.model}`}
                  style={{ maxWidth: '100%', height: 'auto' }}
                />
                <br />
              </div>
            )}
            <p style={infoStyle}>Марка авто: {advert.brand}</p>
            <p style={infoStyle}>Модель авто: {advert.model}</p>
            <p style={infoStyle}>Цвет авто: {advert.color}</p>

            <Link to={`/api/v1/mainapp/car/advert/${advert.id}`} style={linkStyle}>Подробнее</Link>
          </div>
        ))}
      </div>
    </div>
  );
};

const advertsContainerStyle = {
  maxWidth: '1400px',
  margin: '0 auto',
};

const advertsListStyle = {
  display: 'flex',
  flexWrap: 'wrap',
  gap: '10px',
};

const advertBlockStyle = {
  width: '30%', // Или другой процент ширины в зависимости от количества объявлений в строке
  border: '1px solid #ccc',
  padding: '10px',
  margin: '10px 0',
  borderRadius: '8px',
};

const infoStyle = {
  fontSize: '16px',
  margin: '8px 0',
};

const linkStyle = {
  textDecoration: 'none',
  color: '#0366d6',
  display: 'block',
  marginTop: '10px',
};

export default CarAdvertList;
