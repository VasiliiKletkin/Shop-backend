<template>
  <base-layout>
    <b-card-group deck>
          <li v-for="order in orders" :key="order.id">
            {{ order.id }}
          </li>
      </b-card-group>
  </base-layout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import UserService from "../services/user.service";

export default {
  name: "Orders",
  components: { BaseLayout },
  data() {
    return {
      orders: [],
    };
  },
  mounted() {
    UserService.getOrders().then(
      (response) => {
        this.orders = response.data;
      },
      (error) => {
        this.orders =
          (error.response &&
            error.response.data &&
            error.response.data.message) ||
          error.message ||
          error.toString();
      }
    );
  },
};
</script>

<style>
</style>
