import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';




const CarAdvertDetail = () => {
  const { id } = useParams();
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
};

export default CarAdvertDetail;
