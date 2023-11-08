<template>
  <base-layout>
        {{ order }}
  </base-layout>
</template>

<script>
import UserService from "../services/user.service";
import BaseLayout from '../layouts/BaseLayout.vue';

export default {
  name: "OrderDetailView",
  components: { BaseLayoutBaseLayout },
  data() {
    return {
      order: {},
    };
  },
  mounted() {
    UserService.getOrder(this.$route.params.id).then(
      (response) => {
        this.order = response.data;
      },
      (error) => {
        this.order =
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

<style></style>
