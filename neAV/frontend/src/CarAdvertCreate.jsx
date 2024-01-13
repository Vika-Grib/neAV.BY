import React, { useState } from 'react';
import axios from 'axios';

const CarAdvertCreate = () => {
  const [formData, setFormData] = useState({
    brand: '',
    model: '',
    color: '',
    // Другие поля объявления
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('/api/v1/mainapp/car/advert/create/', formData);
      console.log(response.data); // Выводим ответ сервера, например, id созданного объявления
    } catch (error) {
      console.error('Ошибка при создании объявления', error);
    }
  };

  return (
     <div>
      <h2>Создание объявления</h2>
      <form onSubmit={handleSubmit} className="needs-validation" noValidate>
        <div className="mb-3">
          <label htmlFor="brand" className="form-label">Марка авто:</label>
          <input type="text" className="form-control" id="brand" name="brand" value={formData.brand} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите марку авто.
          </div>
        </div>
        <div className="mb-3">
          <label htmlFor="model" className="form-label">Модель авто:</label>
          <input type="text" className="form-control" id="model" name="model" value={formData.model} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите модель авто.
          </div>
        </div>
        <div className="mb-3">
          <label htmlFor="color" className="form-label">Цвет авто:</label>
          <input type="text" className="form-control" id="color" name="color" value={formData.color} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите цвет авто.
          </div>
        </div>
        {/* Добавить другие поля формы для создания объявления */}
        <button type="submit" className="btn btn-secondary">Создать объявление</button>
      </form>
    </div>
  );
};

export default CarAdvertCreate;
