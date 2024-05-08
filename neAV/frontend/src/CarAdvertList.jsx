import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const emptyAdvertsStyle = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
  height: '400px', // Высота контейнера
  textAlign: 'center',
  color: '#666', // Цвет текста
  margin: '20px 0',
};

const CarAdvertList = () => {
  const [adverts, setAdverts] = useState([]);

  useEffect(() => {
    const fetchAdverts = async () => {
      // Проверяем, залогинен ли пользователь перед запросом объявлений
      if (sessionStorage.getItem('status') === 'loggedIn') {
        try {
          const response = await axios.get('/api/v1/mainapp/car/advert/');
          console.log(response.data);
          setAdverts(response.data.results);
        } catch (error) {
          console.error('Ошибка при получении списка объявлений', error);
        }
      } else {
        setAdverts([]);  // Очищаем список объявлений, если пользователь не залогинен
      }
    };

    fetchAdverts();

    // Подписка на события изменения sessionStorage для реакции на выход пользователя
    const handleStorageChange = () => {
      fetchAdverts();  // Перезапускаем загрузку объявлений при изменении sessionStorage
    };

    window.addEventListener('storage', handleStorageChange);

    return () => {
      window.removeEventListener('storage', handleStorageChange);
    };
  }, []);


  if (!adverts.length) {
      return (
        <div style={emptyAdvertsStyle}>
          <img
            src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExejFzN2RlOXdyZjlzc3d2bDdyc21rb3NwNmZycnkwdmFrZWl4ZHZ5YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oz8xTmX0sd5FjqrYc/giphy.gif" // Замените URL на адрес вашей картинки
            alt="Нет объявлений"
            style={{ maxWidth: '100%', height: 'auto' }}
          />
          <p>На данный момент объявлений нет. <Link to="/api/auth/" style={linkStyle}>Зарегестрируйтесь и разместите ваше объявление</Link></p>
        </div>
      );
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
                  src={`${advert.photo}`}
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
  width: '20%', // Или другой процент ширины в зависимости от количества объявлений в строке
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
