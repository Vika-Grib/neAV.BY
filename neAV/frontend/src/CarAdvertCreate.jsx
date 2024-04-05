import React, { useState } from 'react';
import axios from 'axios';
import { useCookies } from 'react-cookie';
import { car_brand_model_year } from './cars.js'; // Импорт данных о машинах
import RulesComponent from './RulesComponent';
// import { useNavigate } from 'react-router-dom';

function GetCSRFToken() {
  const [cookies] = useCookies(['csrftoken']);
  return cookies.csrftoken; // Обновлено для прямого возврата csrftoken
}

const CarAdvertCreate = () => {
//   const navigate = useNavigate();
  // Начальное состояние формы
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
    'X-CSRFToken': GetCSRFToken(),
  });

  // Состояния для контроля видимости полей
  const [visibleFields, setVisibleFields] = useState({
    model: false,
    car_year: false,
    photo: false,
    vin: false,
    transmission: false,
    color: false,
    drive_unit: false,
    car_type: false,
    engine_type: false,
    price: false,
    mileage: false,
    salon_material: false,
    description: false,
  });

  // Состояния для доступных моделей и годов
  const [selectedBrand, setSelectedBrand] = useState('');
  const [availableModels, setAvailableModels] = useState([]);
  const [availableYears, setAvailableYears] = useState([]);

  // Обработчик изменений для полей формы
  const handleChange = (e) => {
    const { name, value } = e.target;
    console.log(e.target);
    setFormData({
      ...formData,
      [name]: value,
    });
    console.log(formData);

    switch (name) {
      case 'brand':
        setSelectedBrand(value);
        setAvailableModels(Object.keys(car_brand_model_year[value] || {}));
        setVisibleFields({ ...visibleFields, model: true });
        break;
      case 'model':
        const selectedYear = car_brand_model_year[selectedBrand]?.[value] || [];
        setAvailableYears(selectedYear);
        setVisibleFields({ ...visibleFields, car_year: true });
        break;
      case 'car_year':
        setVisibleFields({ ...visibleFields, photo: true });
        break;
      case 'photo':
        setVisibleFields({ ...visibleFields, vin: true });
        break;
      case 'vin':
        setVisibleFields({ ...visibleFields, transmission: true });
        break;
      case 'transmission':
        setVisibleFields({ ...visibleFields, color: true });
        break;
      case 'color':
        setVisibleFields({ ...visibleFields, drive_unit: true });
        break;
      case 'drive_unit':
        setVisibleFields({ ...visibleFields, car_type: true });
        break;
      case 'car_type':
        setVisibleFields({ ...visibleFields, engine_type: true });
        break;
      case 'engine_type':
        setVisibleFields({ ...visibleFields, price: true });
        break;
      case 'price':
        setVisibleFields({ ...visibleFields, mileage: true });
        break;
      case 'mileage':
        setVisibleFields({ ...visibleFields, salon_material: true });
        break;
      case 'salon_material':
        setVisibleFields({ ...visibleFields, description: true });
        break;
      case 'description':
        // После заполнения описания, все поля формы открыты,
        // можно добавить действие, если необходимо, например, автофокус на кнопку отправки
        break;

      default:
        // Не забыть добавить обработку по умолчанию, если это необходимо
        break;
    }
  };

  // Обработчик изменения фото
  const handlePhotoChange = (e) => {
    setFormData({
      ...formData,
      photo: e.target.files[0],
    });
    setVisibleFields({ ...visibleFields, vin: true }); // Следующее поле становится видимым после выбора фото
  };

  // Функция отправки формы
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!formData['X-CSRFToken']) {
      console.error('CSRF token отсутсвует!');
      return;
    }

    try {
      const response = await axios.post('/api/v1/mainapp/car/advert/', formData, {
        headers: {
          'X-CSRFToken': formData['X-CSRFToken'],
          'Content-Type': 'multipart/form-data',
        },
      });
      console.log(response.data); // Выводим ответ сервера

//       // Используем navigate для перенаправления
//       navigate("/api/v1/mainapp/car/advert/");
    } catch (error) {
      console.error('Ошибка при создании объявления', error);
    }
  };

    const titleStyle = {
      marginTop: '20px',
    };

    const mainContainerStyle = {
      display: 'flex',
    };

    const contentContainerStyle = {
      flex: '1',
    };

    const formContainerStyle = {
      marginTop: '20px',
      backgroundColor: '#eeeeee',
      padding: '20px',
      borderRadius: '8px',
      boxShadow: '0 0 20px rgba(0, 0, 0, 0.1)',
      maxWidth: '700px',
      paddingBottom: '50px', // Добавлено нижнее пространство
    };

    const sideContainerStyle = {
      marginRight: '100px',
      marginTop: '-65px',
    };


  return (
  <div className="container">
    <h2 style={titleStyle}>Новое объявление о продаже автомобиля</h2>
    <div style={mainContainerStyle}>
      <div style={contentContainerStyle}>
        <div style={formContainerStyle}>
          <form onSubmit={handleSubmit} className="needs-validation" noValidate>
            <div className="mb-3 col-sm-6">
              <label htmlFor="advert_type" className="form-label">Вид транспорта:</label>
              <select
                className="form-control"
                id="advert_type"
                name="advert_type"
                value={formData.advert_type}
                onChange={handleChange}
                required>
                <option value="">Выберите вид транспорта</option>
                <option value="1">Легковой автомобиль</option>
                <option value="2">Грузовик или фургон</option>
                <option value="3">Мототехника</option>
                <option value="4">Спецтехника</option>
                <option value="5">Сельхозтехника</option>
                <option value="6">Водный транспорт</option>
              </select>
            </div>

            {formData.advert_type && <div className="mb-3 col-sm-6">
              <label htmlFor="brand" className="form-label">Марка авто:</label>
              <select
                className="form-control"
                id="brand"
                name="brand"
                value={formData.brand}
                onChange={handleChange}
                required>
                <option value="">Выберите марку</option>
                {Object.keys(car_brand_model_year).map(brand => (
                  <option key={brand} value={brand}>{brand}</option>
                ))}
              </select>
            </div>}

            {visibleFields.model && <div className="mb-3 col-sm-6">
              <label htmlFor="model" className="form-label">Модель авто:</label>
              <select
                className="form-control"
                id="model"
                name="model"
                value={formData.model}
                onChange={handleChange}
                required>
                <option value="">Выберите модель</option>
                {availableModels.map(model => (
                  <option key={model} value={model}>{model}</option>
                ))}
              </select>
            </div>}

            {visibleFields.car_year && <div className="mb-3 col-sm-6">
              <label htmlFor="car_year" className="form-label">Год выпуска:</label>
              <select
                className="form-control"
                id="car_year"
                name="car_year"
                value={formData.car_year}
                onChange={handleChange}
                required>
                <option value="">Выберите год</option>
                {availableYears.map(year => (
                  <option key={year} value={year}>{year}</option>
                ))}
              </select>
            </div>}

            {visibleFields.photo && <div className="mb-3 col-sm-6">
              <label htmlFor="photo" className="form-label">Фото авто:</label>
              <input
                type="file"
                className="form-control"
                id="photo"
                name="photo"
                onChange={handlePhotoChange}
                accept="image/*" />
            </div>}

            {visibleFields.vin && (
              <div className="mb-3 col-sm-6">
                <label htmlFor="vin" className="form-label">Vin номер:</label>
                <input
                  type="text"
                  className="form-control"
                  id="vin"
                  name="vin"
                  value={formData.vin}
                  onChange={handleChange}
                  required />
              </div>
            )}

            {visibleFields.transmission && (
              <div className="mb-3 col-sm-6">
                <label htmlFor="transmission" className="form-label">Коробка передач:</label>
                <select
                  className="form-control"
                  id="transmission"
                  name="transmission"
                  value={formData.transmission}
                  onChange={handleChange}
                  required>
                  <option value="">Выберите тип</option>
                  <option value="1">Робот</option>
                  <option value="2">Механика</option>
                  <option value="3">Автомат</option>
                </select>
              </div>
            )}

            {visibleFields.color && (
              <div className="mb-3 col-sm-6">
                <label htmlFor="color" className="form-label">Цвет авто:</label>
                <input
                  type="text"
                  className="form-control"
                  id="color"
                  name="color"
                  value={formData.color}
                  onChange={handleChange}
                  required />
              </div>
            )}

            {visibleFields.drive_unit && (
              <div className="mb-3 col-sm-6">
                <label htmlFor="drive_unit" className="form-label">Привод:</label>
                <select
                  className="form-control"
                  id="drive_unit"
                  name="drive_unit"
                  value={formData.drive_unit}
                  onChange={handleChange}
                  required>
                  <option value="">Выберите тип привода</option>
                  <option value="1">Полный привод</option>
                  <option value="2">Передний привод</option>
                  <option value="3">Задний привод</option>
                </select>
              </div>
            )}

            {visibleFields.car_type && (
              <div className="mb-3 col-sm-6">
                <label htmlFor="car_type" className="form-label">Тип авто:</label>
                <select
                  className="form-control"
                  id="car_type"
                  name="car_type"
                  value={formData.car_type}
                  onChange={handleChange}
                  required>
                  <option value="">Выберите тип авто</option>
                  <option value="1">Седан</option>
                  <option value="2">Хэтчбек</option>
                  <option value="3">Универсал</option>
                  <option value="4">Купе</option>
                  <option value="5">Кабриолет</option>
                </select>
              </div>
            )}

            {visibleFields.engine_type && (
              <div className="mb-3 col-sm-6">
                <label htmlFor="engine_type" className="form-label">Тип двигателя:</label>
                <select
                  className="form-control"
                  id="engine_type"
                  name="engine_type"
                  value={formData.engine_type}
                  onChange={handleChange}
                  required>
                  <option value="">Выберите тип двигателя</option>
                  <option value="1">Бензин</option>
                  <option value="2">Дизель</option>
                  <option value="3">Электро</option>
                  <option value="4">Гибрид</option>
                </select>
              </div>
            )}

            {visibleFields.price && (
              <div className="mb-3 col-sm-6">
                <label htmlFor="price" className="form-label">Цена:</label>
                <input
                  type="number"
                  className="form-control"
                  id="price"
                  name="price"
                  value={formData.price}
                  onChange={handleChange}
                  required />
                   <select type="text" className="form-control" id="price_type" name="price_type" value={formData.price_type} onChange={handleChange} required>
                   <option value="">Выберите тип валюты</option>
                    <option value="1">USD</option>
                    <option value="2">BYN</option>
                    </select>
              </div>
            )}

            {visibleFields.mileage && (
              <div className="mb-3 col-sm-6">
                <label htmlFor="mileage" className="form-label">Пробег (км):</label>
                <input
                  type="number"
                  className="form-control"
                  id="mileage"
                  name="mileage"
                  value={formData.mileage}
                  onChange={handleChange}
                  required />
              </div>
            )}

            {visibleFields.salon_material && (
              <div className="mb-3 col-sm-6">
                <label htmlFor="salon_material" className="form-label">Материал салона:</label>
                <select
                  className="form-control"
                  id="salon_material"
                  name="salon_material"
                  value={formData.salon_material}
                  onChange={handleChange}
                  required>
                  <option value="">Выберите материал салона</option>
                  <option value="1">Кожа</option>
                  <option value="2">Ткань</option>
                  <option value="3">Алькантара</option>
                </select>
              </div>
            )}

            {visibleFields.description && (
              <div className="mb-3 col-sm-6">
                <label htmlFor="description" className="form-label">Описание:</label>
                <textarea
                  className="form-control"
                  id="description"
                  name="description"
                  value={formData.description}
                  onChange={handleChange}
                  required />
              </div>
            )}

            {/* Кнопка отправки формы, которая появляется только после заполнения всех полей */}
            {visibleFields.description && <button type="submit" className="btn btn-secondary">Создать объявление</button>}
          </form>
        </div>
      </div>
      <div style={sideContainerStyle}>
        <RulesComponent />
      </div>
    </div>
  </div>
);
};

export default CarAdvertCreate;
