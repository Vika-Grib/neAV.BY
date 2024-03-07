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

      {/* Другие поля информации об объявлении */}
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
      <p>Марка авто: {advert.brand}</p>
      <p>Описание авто: {advert.description}</p>
      <p>Модель авто: {advert.model}</p>
      <p>Цвет авто: {advert.color}</p>
      {advert.transmission===1 &&
        <p>Коробка передач: Робот</p>}
      {advert.transmission===2 &&
        <p>Коробка передач: Механика</p>}
      {advert.transmission===3 &&
        <p>Коробка передач: Автомат</p>}
      <p>Материал салона: {advert.salon_material}</p>
      <p>Тип двигателя: {advert.engine_type}</p>
      <p>Привод: {advert.drive_unit}</p>
      <p>Пробег: {advert.mileage}</p>
      <p>Цена: {advert.price} {advert.price_type}</p>
    </div>
  );
};

export default CarAdvertDetail;
