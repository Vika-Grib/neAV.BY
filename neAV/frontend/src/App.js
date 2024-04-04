import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import CarList from './CarList';
import CarDetail from './CarDetail';
import CarAdvertCreate from './CarAdvertCreate';
import CarAdvertList from './CarAdvertList';
import CarAdvertDetail from './CarAdvertDetail';
import AuthComponent from './AuthComponent';
import profile_photo from './noneuser.png';
import Auto_z_probegom from './Auto_z_probegom';
import Auto_z_prob_detail from './Auto_z_prob_detail';
import CarSearch from "./CarSearch";


const bannerStyle = {
  width: '100%',
};

const handleLogout = async (e) => {
    e.preventDefault();

    try {
      // Application, sessionStorage - там можем посмотреть что мы залогинены
      sessionStorage.setItem('status','');
      window.location.reload();

    } catch (error) {
      console.error('Logout error:', error);
    }
  };


export default function App() {
    const appStyle = {
    marginTop: '0px',      // Отступ сверху
    marginRight: '40px',    // Отступ справа
    marginLeft: '40px',     // Отступ слева
    padding: '20px',        // Внутренний отступ для содержимого
  };


    if (sessionStorage.getItem('status') == 'loggedIn'){
        return (
  <Router>
    <div className="App" style={appStyle}>
    <img
          src="https://avatars.mds.yandex.net/get-adfox-content/2765366/240108_adfox_2819692_8259184.711d98707dfbea76d073b0a431d0835e.jpg/optimize.webp"
          alt="Banner"
          style={bannerStyle}
        />

    <h1 style={{color: "red", textAlign: "center", borderBottom: "2px solid #808080", paddingBottom: "10px"}}></h1>
    <nav style={navStyle}>
        {/* <Link to="/api/v1/mainapp/all/">Список автомобилей</Link> */}
        <Link to="/api/v1/mainapp/car/used/" >Авто с пробегом</Link>
        <Link to="/api/v1/mainapp/car/advert/" >Мои объявления</Link>
        <Link to="/api/v1/mainapp/car/advert/create/" className="btn btn-primary" >Подать объявление</Link>



          <Link to="/api/auth/logout/">
          <button type="button" class="btn btn-outline-info" onClick={handleLogout} style={{ marginRight: '10px' }}> <img src={profile_photo} width={40} height={40} alt='Profile photo'/>Выйти</button>
          </Link>


    </nav>


    <Routes>
        {/*<Route path="/api/v1/mainapp/all/" element={<CarList />} /> */}
        {/*<Route path="/api/v1/mainapp/car/detail/id" element={<CarDetail />} /> */}
        <Route path="/api/v1/mainapp/car/advert/create/" element={<CarAdvertCreate />} />
        <Route path="/api/v1/mainapp/car/advert/" element={<CarAdvertList />} />
        <Route path="/api/v1/mainapp/car/advert/:id" element={<CarAdvertDetail />} />
        <Route path="/api/v1/mainapp/car/used" element={<Auto_z_probegom />} />
        <Route path="/api/v1/mainapp/car/used/:id" element={<Auto_z_prob_detail />} />
        <Route path="/api/auth/logout" element={<CarAdvertList />} />
        <Route path="/api/v1/mainapp/car/car_search" element={<CarSearch/>}/>
    </Routes>

    </div>
  </Router>
  );
}
    else{
        return (
  <Router>
    <div className="App" style={appStyle}>
    <img
          src="https://avatars.mds.yandex.net/get-adfox-content/2765366/240108_adfox_2819692_8259184.711d98707dfbea76d073b0a431d0835e.jpg/optimize.webp"
          alt="Banner"
          style={bannerStyle}
        />

    <h1 style={{color: "red", textAlign: "center", borderBottom: "2px solid #808080", paddingBottom: "10px"}}>Объявления о продаже авто</h1>
    <nav style={navStyle}>
        {/* <Link to="/api/v1/mainapp/all/">Список автомобилей</Link> */}
        <Link to="/api/v1/mainapp/car/used/" >Авто с пробегом</Link>
        <Link to="/api/v1/mainapp/car/advert/" >Все объявления</Link>
        <Link to="/api/v1/mainapp/car/advert/create/" className="btn btn-primary" >Подать объявление</Link>
        <Link to="/api/auth/">Авторизоваться</Link>
    </nav>


    <Routes>
        {/*<Route path="/api/v1/mainapp/all/" element={<CarList />} /> */}
        {/*<Route path="/api/v1/mainapp/car/detail/id" element={<CarDetail />} /> */}
        <Route path="/api/v1/mainapp/car/advert/create/" element={<CarAdvertCreate />} />
        <Route path="/api/v1/mainapp/car/advert/" element={<CarAdvertList />} />
        <Route path="/api/v1/mainapp/car/advert/:id" element={<CarAdvertDetail />} />
        <Route path="/api/auth/" element={<AuthComponent />} />
        <Route path="/api/v1/mainapp/car/used" element={<Auto_z_probegom />} />
        <Route path="/api/v1/mainapp/car/used/:id" element={<Auto_z_prob_detail />} />
        <Route path="/api/v1/mainapp/car/car_search" element={<CarSearch/>}/>
    </Routes>

    </div>
  </Router>
  );
    }
  };


const navStyle = {
  display: 'flex',
  justifyContent: 'space-around',
  padding: '10px',
  background: '#f0f0f0',
};

const buttonStyle = {
    display: 'inline-block',
    padding: '10px 20px',
    backgroundColor: '#007bff',
    color: '#fff',
    textDecoration: 'none',
    borderRadius: '5px',
    transition: 'background-color 0.3s ease',

  };