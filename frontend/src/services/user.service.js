import axios from "axios";
import authHeader from "./auth-header";

const API_URL = "http://localhost:8000/api/";

class UserService {
  getProducts() {
    return axios.get(API_URL + "products/");
  }
  getProduct(id) {
    return axios.get(API_URL + "products/" + id);
  }
  getOrders() {
    return axios.get(API_URL + "orders/", { headers: authHeader() });
  }

  getOrder(id) {
    return axios.get(API_URL + "orders/" + id, { headers: authHeader() });
  }

  // getAdminBoard() {
  //   return axios.get(API_URL + "admin", { headers: authHeader() });
  // }
}

export default new UserService();
