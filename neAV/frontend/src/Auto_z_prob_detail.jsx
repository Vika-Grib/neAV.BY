import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

const AutoZProbDetail = () => {
  const { id } = useParams();
  const [advert, setAdvert] = useState(null);

  useEffect(() => {
    const fetchAdvert = async () => {
      try {
        const response = await axios.get(`/api/v1/mainapp/car/used/${id}/`);
        setAdvert(response.data);
      } catch (error) {
        console.error('Ошибка при получении сведений об автомобиле', error);
      }
    };

    fetchAdvert();
  }, [id]);

  if (!advert) {
    return <div style={styles.loading}>Загрузка информации...</div>;
  }

  return (
    <div style={styles.container}>
      <h2 style={styles.header}>Информация об автомобиле</h2>
      {advert.photo && (
        <div style={styles.imageContainer}>
          <img src={advert.photo} style={styles.image} alt="Фото автомобиля" />
        </div>
      )}
      <div style={styles.card}>
        <p style={styles.infoTitle}>{advert.name}</p>
        <p style={styles.info}>Цена: {advert.price_for_bel_rub} BYN</p>
        <p style={styles.info}>Кузов авто: {advert.kyzov}</p>
        <p style={styles.info}>Привод: {advert.privod}</p>
        <p style={styles.info}>Цвет авто: {advert.color}</p>
        <p style={styles.info}>Пробег авто: {advert.probeg}</p>
        <p style={styles.info}>Год авто: {advert.year}</p>
        <p style={styles.info}>Коробка передач: {advert.kpp}</p>
        <p style={styles.info}>Тип и объем двигателя: {advert.type_engine}, {advert.volume}</p>
        <p style={styles.info}>Описание авто: {advert.comment}</p>
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
    maxWidth: '100%',
    height: 'auto',
    borderRadius: '10px',
  },
  card: {
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
    padding: '20px',
    borderRadius: '8px',
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
  }
};

export default AutoZProbDetail;
