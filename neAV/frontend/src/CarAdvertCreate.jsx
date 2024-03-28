import React, { useState } from 'react';
import axios from 'axios';
// import fs from 'fs';
import { useCookies } from 'react-cookie';

function GetCSRFToken() {
  const [cookies, setCookie] = useCookies(['csrftoken']);
  console.log(cookies)
  return cookies;
 };

const CarAdvertCreate = ({ csrfToken }) => {
  const [formData, setFormData] = useState({
    photo: null,
    vin: '',
    advert_type: '',
    brand: '',
    model: '',
    color: '',
    car_type: '',
    car_year: '',
    price: '',
    price_type: '',
    mileage: '',
    drive_unit: '',
    engine_type: '',
    salon_material: '',
    transmission: '',
    description: '',
    'X-CSRFToken': GetCSRFToken().csrftoken,
    // Другие поля объявления
  });


  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handlePhotoChange = (e) => {
    setFormData({
      ...formData,
      photo: e.target.files[0],
    });
  };

  console.log(formData)
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!formData['X-CSRFToken']) {
    console.error('CSRF token отсутсвует!');
    return;
  }

    try {
    console.log(formData);
      const response = await axios.post(
      '/api/v1/mainapp/car/advert/', formData,{
        headers: {
        'X-CSRFToken': formData['X-CSRFToken'],
        'Content-Type': 'multipart/form-data',
        },
      });


      console.log(response.data); // Выводим ответ сервера, например, id созданного объявления
    } catch (error) {
      console.error('Ошибка при создании объявления', error);
    }
  };

  return (
     <div>
      <h2>Создание объявления</h2>
      <form onSubmit={handleSubmit} className="needs-validation" noValidate>
        <div className="mb-3 col-sm-6">
          <label htmlFor="advert_type" className="form-label">Марка авто:</label>
          <select type="text" className="form-control" id="advert_type" name="advert_type" value={formData.advert_type} onChange={handleChange} required>
          <option value="1">Легковой автомобиль </option>
          <option value="2">Грузовик или фурго </option>
          <option value="3">Мототехника </option>
          <option value="4">Спецтехника </option>
          <option value="5">С/х техника </option>
          <option value="6">Водный транспорт </option>
          </select>
          <div className="invalid-feedback">
            Пожалуйста, введите вид транспорта
          </div>
        </div>

        <div className="mb-3 col-sm-6">
          <label htmlFor="brand" className="form-label">Марка авто:</label>
          <input type="text" className="form-control" id="brand" name="brand" value={formData.brand} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите марку авто.
          </div>
        </div>

        <div className="mb-3 col-sm-6">
          <label htmlFor="model" className="form-label">Модель авто:</label>
          <input type="text" className="form-control" id="model" name="model" value={formData.model} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите модель авто.
          </div>
        </div>

        <div className="mb-3 col-sm-6">
          <label htmlFor="photo" className="form-label">Фото авто:</label>
          <input type="file" className="form-control" id="photo" name="photo" onChange={handlePhotoChange} accept="image/*" />
          <div className="invalid-feedback">
            Пожалуйста, загрузите фото.
          </div>
        </div>

        <div className="mb-3 col-sm-6">
          <label htmlFor="vin" className="form-label">Vin номер:</label>
          <input type="text" className="form-control" id="vin" name="vin" value={formData.vin} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите vin номер авто.
          </div>
        </div>

        <div className="mb-3 col-sm-6">
          <label htmlFor="transmission" className="form-label">Коробка передач:</label>
          <select type="text" className="form-control" id="transmission" name="transmission" value={formData.transmission} onChange={handleChange} required>
          <option value="1">Робот </option>
          <option value="2">Механика </option>
          <option value="3">Автомат </option>
          </select>
          <div className="invalid-feedback">
            Пожалуйста, введите вид коробки передач
          </div>
        </div>

        <div className="mb-3 col-sm-6">
          <label htmlFor="color" className="form-label">Цвет авто:</label>
          <input type="text" className="form-control" id="color" name="color" value={formData.color} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите цвет авто.
          </div>

          <div className="mb-3 col-sm-6">
          <label htmlFor="drive_unit" className="form-label">Привод:</label>
          <select type="text" className="form-control" id="drive_unit" name="drive_unit" value={formData.drive_unit} onChange={handleChange} required>
          <option value="1">Полный привод </option>
          <option value="2">Передний привод </option>
          <option value="3">Задний привод </option>
          </select>
          <div className="invalid-feedback">
            Пожалуйста, введите какой привод у автомобиля.
          </div>
          </div>

        <div className="mb-3 col-sm-6">
          <label htmlFor="car_type" className="form-label">Тип авто:</label>
          <select type="text" className="form-control" id="car_type" name="car_type" value={formData.car_type} onChange={handleChange} required>
          <option value="1">Седан </option>
          <option value="2">Хэчбек </option>
          <option value="3">Универсал </option>
          <option value="4">Купе </option>
          <option value="5">Лифтбек </option>
          <option value="6">Кабриолет </option>
          </select>
          <div className="invalid-feedback">
            Пожалуйста, введите тип авто.
          </div>
          </div>

          <div className="mb-3 col-sm-6">
          <label htmlFor="engine_type" className="form-label">Тип двигателя:</label>
          <select type="text" className="form-control" id="engine_type" name="engine_type" value={formData.engine_type} onChange={handleChange} required>
          <option value="1">Дизель </option>
          <option value="2">Бензин </option>
          <option value="3">Бензин (пропан-бутан) </option>
          <option value="4">Бензин (бутан) </option>
          </select>
          <div className="invalid-feedback">
            Пожалуйста, введите Тип двигателя.
          </div>
          </div>

          <div className="mb-3 col-sm-6">
          <label htmlFor="car_year" className="form-label">Год авто:</label>
          <input type="text" className="form-control" id="car_year" name="car_year" value={formData.car_year} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите год авто.
          </div>
          </div>

          <div className="mb-3 col-sm-6">
          <label htmlFor="price" className="form-label">Цена:</label>
          <div className="input-group">
          <input type="text" className="form-control" id="price" name="price" value={formData.price} onChange={handleChange} required />
            <select type="text" className="form-control" id="price_type" name="price_type" value={formData.price_type} onChange={handleChange} required>
            <option value="1">USD</option>
            <option value="2">BYN</option>
            </select>
        </div>
        <div className="invalid-feedback">
            Пожалуйста, введите цену авто.
        </div>
        </div>

          <div className="mb-3 col-sm-6">
          <label htmlFor="mileage" className="form-label">Пробег:</label>
          <input type="text" className="form-control" id="mileage" name="mileage" value={formData.mileage} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите пробег авто.
          </div>
          </div>

          <div className="mb-3 col-sm-6">
          <label htmlFor="salon_material" className="form-label">Материал салона:</label>
          <select type="text" className="form-control" id="salon_material" name="salon_material" value={formData.salon_material} onChange={handleChange} required>
          <option value="1">Искусственная кожа </option>
          <option value="2">Натуральная кожа </option>
          <option value="3">Ткань </option>
          <option value="4">Велюр </option>
          <option value="5">Алькантара </option>
          <option value="6">Комбинированные материалы </option>
          </select>
          <div className="invalid-feedback">
            Пожалуйста, какой материал салона автомобиля.
          </div>
          </div>

          <div className="mb-3 col-sm-6">
          <label htmlFor="description" className="form-label">Описание:</label>
          <input type="text" className="form-control" id="description" name="description" value={formData.description} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите описание авто.
          </div>
          </div>


        </div>
        {/* Разделительный блок */}
        {/*<hr style={{ margin: '20px 0' }} />*/}
        {/* Добавить другие поля формы для создания объявления */}
        <button type="submit" className="btn btn-secondary">Создать объявление</button>
      </form>
    </div>
  );
};


export default CarAdvertCreate;
