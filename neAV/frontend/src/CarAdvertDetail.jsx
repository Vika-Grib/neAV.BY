import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';



const CarAdvertDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate(); // Хук для перенаправления
  const [advert, setAdvert] = useState(null);

  useEffect(() => {
    const fetchAdvert = async () => {
      try {
        const response = await axios.get(`/api/v1/mainapp/car/advert/${id}/`);
        setAdvert(response.data);
      } catch (error) {
        console.error('Ошибка при получении сведений об объявлении', error);
      }
    };

    fetchAdvert();
  }, [id]);

  const handleDelete = async () => {
  if (window.confirm('Вы уверены, что хотите удалить это объявление?')) {
    try {
      // Предполагаем, что CSRF токен сохранён в cookies под именем 'csrftoken'
      const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrftoken=')).split('=')[1];

      const response = await axios.delete(`/api/v1/mainapp/car/advert/${id}/`, {
        headers: {
          'X-CSRFToken': csrfToken,
        }
        // withCredentials: true, // Этот параметр необходим только если вы используете аутентификацию на основе кук.
      });

        if (response.status === 204) {
          // Удаление прошло успешно
          navigate('/api/v1/mainapp/car/advert/'); // Перенаправление на страницу со всеми оставшимися своими объявлениями
        }
      } catch (error) {
        console.error('Ошибка при удалении объявления', error);
        alert('Не удалось удалить объявление. Пожалуйста, попробуйте ещё раз.');
      }
    }
  };

  if (!advert) {
    return <div style={styles.loading}>Загрузка информации...</div>;
  }

  return (
    <div style={styles.container}>
      <h2 style={styles.header}>Информация об объявлении</h2>
      {advert.photo && (
        <div style={styles.imageContainer}>
          <img src={advert.photo} alt={`${advert.brand} ${advert.model}`} style={styles.image} />
        </div>
      )}
      <div style={styles.card}>
        <p style={styles.infoTitle}>Марка авто: {advert.brand}</p>
        <p style={styles.info}>Модель авто: {advert.model}</p>
        <p style={styles.info}>Цвет авто: {advert.color}</p>
        {/* Ваши условные рендеры здесь */}
        <p style={styles.info}>Пробег: {advert.mileage}</p>
        <p style={styles.info}>Цена: {advert.price} {advert.price_type === 1 ? 'USD' : advert.price_type === 2 ? 'BYN' : ''}</p>
        <p style={styles.info}>Описание авто: {advert.description}</p>

        <button onClick={handleDelete} style={styles.deleteButton}>
        Удалить объявление
        </button>
      </div>
    </div>
  );
};

const styles = {
  container: {
    maxWidth: '800px',
    margin: '20px auto',
    padding: '20px',
    fontFamily: 'Arial, sans-serif',
  },
  header: {
    fontWeight: 'bold',
    marginBottom: '20px',
    fontSize: '24px',
    textAlign: 'center',
  },
  imageContainer: {
    textAlign: 'center',
    marginBottom: '20px',
  },
  image: {
    maxWidth: '50%',
    height: 'auto',
    borderRadius: '10px',
  },
  card: {
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
    padding: '20px',
    borderRadius: '8px',
    background: '#f9f9f9',
  },
  infoTitle: {
    fontWeight: 'bold',
    fontSize: '18px',
    marginBottom: '10px',
  },
  info: {
    fontSize: '16px',
    marginBottom: '8px',
  },
  loading: {
    textAlign: 'center',
    fontSize: '18px',
  },
  deleteButton: {
    backgroundColor: 'red',
    color: 'white',
    padding: '10px 20px',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    marginTop: '20px', // Пример отступа сверху
  },
};

export default CarAdvertDetail;
