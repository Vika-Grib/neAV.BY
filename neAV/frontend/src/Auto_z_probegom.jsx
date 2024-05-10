import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import FloatingFish from './FloatingFish';
import UsedAutoFilterForm from './UsedAutoFilterForm';

const CarAdvertList = () => {
  const [adverts, setAdverts] = useState([]);
  const [currentPage, setCurrentPage] = useState(1); // Добавляем состояние для текущей страницы

  const handleFilter = (filters) => {
        const query = Object.keys(filters)
            .filter(key => filters[key]) // Удаление пустых полей
            .map(key => `${encodeURIComponent(key)}=${encodeURIComponent(filters[key])}`)
            .join('&');
        axios.get(`/api/v1/mainapp/car/used/filter?${query}`)
            .then(response => {
                setAdverts(response.data.results);
            })
            .catch(error => {
                console.error('Ошибка при фильтрации списка объявлений', error);
            });
    };

  useEffect(() => {
    const fetchAdverts = async () => {
      try {
        // Используем текущую страницу в запросе к API
        const response = await axios.get(`/api/v1/mainapp/car/used/?page=${currentPage}`);
        setAdverts(response.data.results);
      } catch (error) {
        console.error('Ошибка при получении списка объявлений', error);
      }
    };

    fetchAdverts();
  }, [currentPage]); // Добавляем currentPage в список зависимостей useEffect

  // Функции для навигации
  const goToPreviousPage = () => {
    setCurrentPage(currentPage > 1 ? currentPage - 1 : 1);
  };

  const goToNextPage = () => {
    setCurrentPage(currentPage + 1);
  };

  if (!adverts.length) {
    return <div>Загрузка списка объявлений...</div>;
  }

  return (
    <>
    <FloatingFish />
    <div style={advertsContainerStyle}>
      <h2 style={{ textAlign: 'center', margin: '0 auto' }}>Список объявлений</h2>
      <UsedAutoFilterForm onFilter={handleFilter} />
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
            <p style={{ ...infoStyle, fontWeight: 'bold' }}>{advert.name}</p>
            <p style={infoStyle}>Цена: {advert.price_for_bel_rub} BYN </p>
            <p style={infoStyle}>Кузов авто: {advert.kyzov}</p>
            <p style={infoStyle}>Привод: {advert.privod}</p>
            <p style={infoStyle}>Цвет авто: {advert.color}</p>
            <p style={infoStyle}>Пробег авто: {advert.probeg}</p>

            <Link to={`/api/v1/mainapp/car/used/${advert.id}`} style={linkStyle}>Подробнее</Link>
          </div>
        ))}
      </div>
      <div>
        {/* Кнопки для навигации */}
        {currentPage > 1 && (
          <button onClick={goToPreviousPage} style={{ marginRight: '10px' }}>Предыдущая страница</button>
        )}
        <button onClick={goToNextPage}>Следующая страница</button>
      </div>
    </div>
     </>
  );
};

const advertsContainerStyle = {
  maxWidth: '1400px',
  margin: '0 auto',
  paddingTop: '20px',
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
