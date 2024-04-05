import React, { useState } from 'react';

const rulesContainerStyle = {
  fontFamily: 'Montserrat, sans-serif',
  backgroundColor: '#f5f5f5',
  color: '#fff',
  padding: '20px',
  borderRadius: '8px',
  marginTop: '20px',
  maxWidth: '390px',
  display: 'flex', // Добавляем flex-контейнер
  transition: 'background-color 0.3s ease',
};

const textContainerStyle = {
  flex: '1', // Занимает всю доступную ширину
};

const imageStyle = {
  width: '200px', // Ширина изображения
  marginTop: '5px', // Отступ сверху для картинки
  maxWidth: '50%', // Максимальная ширина изображения
  maxHeight: '50%', // Максимальная высота изображения
  marginRight: '10px',
};

// Стили для ссылки, которые не изменяются
const linkStyle = {
  textDecoration: 'none', // Убираем подчеркивание
  fontSize: '14px',
  fontWeight: 'bold', // Жирный текст
};

const textStyle = {
  fontSize: '12px', // Устанавливаем размер шрифта
};

const RulesComponent = () => {
  const [isHovered, setIsHovered] = useState(false); // Создаем состояние для отслеживания наведения

  // Стили для ссылки, которые изменяются
  const dynamicLinkStyle = {
    color: isHovered ? '#ff4500' : '#1a93ef', // Изменяем цвет в зависимости от состояния
  };

  return (
    <div style={rulesContainerStyle}>
      <div style={textContainerStyle}>
        <h3>
          <a
            href="https://av.by/pages/rules"
            target="_blank"
            rel="noopener noreferrer"
            style={{ ...linkStyle, ...dynamicLinkStyle }} // Применяем статические и динамические стили
            onMouseEnter={() => setIsHovered(true)} // Устанавливаем состояние при наведении
            onMouseLeave={() => setIsHovered(false)} // Сбрасываем состояние при уходе курсора
          >
            ПРАВИЛА
            <span style={{ display: 'block' }}>ПОДАЧИ</span>
            <span style={{ display: 'block' }}>ОБЪЯВЛЕНИЯ</span>
          </a>
        </h3>
        <p style={{ color: 'grey', ...textStyle }}>
          Модератор удалит<br />
          объявление, если<br />
          оно будет нарушать<br />
          правила подачи.
        </p>
      </div>
      <img src="https://pngicon.ru/file/uploads/svetofor-128x128.png" alt="светофор" style={imageStyle}/>
    </div>
  );
};

export default RulesComponent;
