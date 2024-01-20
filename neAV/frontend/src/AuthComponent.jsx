import React, { useState } from 'react';
import axios from 'axios';
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';

function GetCSRFToken() {
  const [cookies, setCookie] = useCookies(['csrftoken']);
  console.log(cookies)
  return cookies;
 };

const AuthComponent = () => {
     const navigate = useNavigate();
     const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    borderRadius: '8px',
  };

  const formStyle = {
  width: '400px', // Ширина формы
  padding: '20px',
  border: '1px solid #ccc',
  borderRadius: '8px',
  boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)', // Меньшая тень
  marginTop: '-340px',
};



  const [formData, setFormData] = useState({
    username: '',
    password: '',
    'X-CSRFToken': GetCSRFToken().csrftoken,
//     'X-CSRF-Token': cookie.load('csrftoken'),
  });
  console.log(formData)


  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      console.log(formData)
      const response = await axios.post('./login/', formData, {
        headers: {
        'X-CSRFToken': formData['X-CSRFToken'],
        },
      });
      console.log('Login success:', response.data);

      // После успешной авторизации перенаправляем пользователя
      navigate('/api/v1/mainapp/car/advert/create');

    } catch (error) {
      console.error('Login error:', error);
    }
  };


  const handleRegister = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('./register/', formData, {
        headers: {
        'X-CSRFToken': formData['X-CSRFToken'],
        },
      });
      console.log('Registration success:', response.data);

      // После успешной регистрации перенаправляем пользователя
      navigate('/api/v1/mainapp/car/advert/create');

    } catch (error) {
      console.error('Registration error:', error);
    }
  };

  return (
    <div className="container mt-5" style={containerStyle}>
    <div style={formStyle}>
      <h2 className="text-center">Вход / Регистрация</h2>
      <form className="needs-validation" noValidate>
        <div className="mb-3">
          <label htmlFor="username" className="form-label">Имя пользователя:</label>
          <input type="text" className="form-control" id="username" name="username" value={formData.username} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите имя пользователя.
          </div>
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">Пароль:</label>
          <input type="password" className="form-control" id="password" name="password" value={formData.password} onChange={handleChange} required />
          <div className="invalid-feedback">
            Пожалуйста, введите пароль.
          </div>
        </div>

        <div class="form-group form-check">
        <input type="checkbox" class="form-check-input" id="rememberMe"/>
        <label class="form-check-label" for="rememberMe">Запомнить меня</label>
        </div>
        < br/>
        <button type="button" class="btn btn-outline-info" onClick={handleLogin} style={{ marginRight: '10px' }}>Войти</button>
        <button type="button" class="btn btn-outline-secondary" onClick={handleRegister}>Зарегистрироваться</button>
      </form>
    </div>
    </div>
  );
};

export default AuthComponent;
