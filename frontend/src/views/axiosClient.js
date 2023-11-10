import axios from 'axios';

const axiosClient = axios.create({
  baseURL: 'http://localhost:8000', // Your Django backend URL
  // You can add your headers here
});

export default axiosClient;
