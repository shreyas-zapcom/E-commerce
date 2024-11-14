import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api';

export const getCategories = () => axios.get(`${API_URL}/categories/`);
export const getProducts = () => axios.get(`${API_URL}/products/`);
export const getOrders = (token) => axios.get(`${API_URL}/orders/`, {
    headers: { Authorization: `Token ${token}` }
});
export const registerUser = (data) => axios.post(`${API_URL}/register/`, data);
export const loginUser = (data) => axios.post(`${API_URL}/login/`, data);
export const logoutUser = (token) => axios.post(`${API_URL}/logout/`, null, {
    headers: { Authorization: `Token ${token}` }
});