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
    return <div>Загрузка информации...</div>;
  }

  return (
    <div>
      <h2>Информация об объявлении</h2>
      <p>Марка авто: {advert.brand}</p>
      <p>Модель авто: {advert.model}</p>
      <p>Цвет авто: {advert.color}</p>
      {/* Другие поля информации об объявлении */}
    </div>
  );
};

export default CarAdvertDetail;
