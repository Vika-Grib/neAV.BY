import axios from 'axios';
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';
import React, {FC, ReactElement, useEffect, useState} from 'react';


function GetCSRFToken() {
  const [cookies, setCookie] = useCookies(['csrftoken']);
  console.log(cookies)
  return cookies;
 };

const LogOutComponent = () => {
  const handleLogout = async (e) => {
    e.preventDefault();


sessionStorage.setItem('status','');


const response = await axios.post('./api/auth/logout/', {
        headers: {
        'X-CSRFToken': GetCSRFToken().csrftoken,
      },
    });

console.log('Logout success:', response.data);
};
};
export default LogOutComponent;