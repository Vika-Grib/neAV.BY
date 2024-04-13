import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { useCookies } from 'react-cookie';
import ContactSellerButton from './ContactSellerButton';

//
// function GetCSRFToken() {
//   const [cookies, setCookie] = useCookies(['csrftoken']);
//   console.log(cookies)
//   return cookies;
//  };


const AutoZProbDetail = ({ csrfToken }) => {
    const { id } = useParams();
    const [advert, setAdvert] = useState(null);
    const [cookies] = useCookies(['csrftoken']);
//     const csrfToken = cookies.csrftoken;

    const telegram_id = sessionStorage.getItem('telegram_id');
    console.log(telegram_id);
    const [formData, setFormData] = useState({
        sender_id: telegram_id,
        'X-CSRFToken': cookies.csrftoken,
        // Другие поля объявления
      });


  useEffect(() => {
    const fetchAdvert = async () => {
      const telegram_id = sessionStorage.getItem('telegram_id');
      try {
        const response = await axios.get(`/api/v1/mainapp/car/used/${id}/`);
        setAdvert(response.data);
      } catch (error) {
         console.error('Ошибка 1 при получении сведений об автомобиле', error);
      }

       try {

       console.log(formData);

      // Обновляем состояние формы или выполняем другие действия по завершению запроса
      setFormData({ sender_id: telegram_id, 'X-CSRFToken': formData['X-CSRFToken'] });
    } catch (error) {
        console.error('Ошибка 2', error);
      }
      };
    fetchAdvert();
  }, [id]);


  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(`/api/v1/mainapp/car/used/${id}/`, formData, {
        headers: {
          'X-CSRFToken': formData['X-CSRFToken'],
          'Content-Type': 'multipart/form-data',
        },
        withCredentials: true,
      });
      console.log('Чат успешно создан:', response.data);
    } catch (error) {
      console.error('Ошибка при создании чата:', error);
//       alert('Ошибка при создании чата');
    }
  };

  if (!advert) {
    return <div style={styles.loading}>Загрузка информации...</div>;
  }
  console.log('Передаем в ContactSellerButton', `Seller ID: ${advert.telegram_id}`, `CSRF Token: ${csrfToken}`);

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

{/*         <form method="POST" name="chat" action={`/api/v1/mainapp/car/used/${id}/`} id="usrform"> */}

{/*            <input type="text" name="sender_id" value={formData.sender_id} hidden></input> */}
{/*            <input type="text" name="reciever_id" value={advert.telegram_id} hidden></input> */}
{/*            <button type="submit" className="btn_chat" >Написать продавцу</button> */}
            <ContactSellerButton sellerId={advert.telegram_id} csrfToken={csrfToken} />
{/*        </form> */}

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
