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

    const linkStyle = {
      textDecoration: 'none', // Убираем подчеркивание
      color: '#1a93ef', // Цвет ссылки
      fontSize: '14px',
      fontWeight: 'bold', // Жирный текст
    };


   const textStyle = {
      fontSize: '12px', // Устанавливаем размер шрифта
    };



    const RulesComponent = () => (
      <div style={rulesContainerStyle}>
      <div style={textContainerStyle}>
        <h3>
          <a
          href="https://av.by/pages/rules"
          target="_blank"
          rel="noopener noreferrer"
          className="link" // Добавляем CSS-класс ссылке
          style={linkStyle} // Применяем стили к ссылке чтобы не было подчеркивания
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
{/*       <img width="94" height="140" src="https://img.icons8.com/3d-fluency/94/traffic-light.png" alt="traffic-light" style={imageStyle}/> */}
      <img src="https://pngicon.ru/file/uploads/svetofor-128x128.png" alt="светофор" style={imageStyle}/>


      </div>
    );

export default RulesComponent;