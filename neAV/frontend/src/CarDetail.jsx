import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

export function useURLID() {
  const { id } = useParams();
  return { id };
}

const CarDetail = () => {
  const { id } = useURLID();
  const [car, setCar] = useState(null);

  useEffect(() => {
    const fetchCar = async () => {
      try {
        const response = await axios.get(`/api/v1/mainapp/car/detail/${id}/`);
        console.log(response);
        setCar(response.data);
      } catch (error) {
        console.error('Ошибка при получении сведений об автомобиле', error);
      }
    };

    fetchCar();
  }, [id]);

  if (!car) {
    return <div>Загрузка информации...</div>;
  }

  return (
    <div>
      <h2>Информация об автомобиле</h2>
      <p>ID: {car.id}</p>
      <p>Марка авто: {car.brand}</p>
      <p>Модель авто: {car.model || 'Нет информации о модели'}</p>
      <p>Цвет авто: {car.color}</p>
    </div>
  );
};

export default CarDetail;
