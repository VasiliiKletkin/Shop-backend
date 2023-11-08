<template>
  <BaseLayout>
    {{ product }}
  </BaseLayout>
</template>

<script>
import BaseLayout from "@/layouts/BaseLayout.vue";
import UserService from "../services/user.service";

export default {
  name: "ProductDetailView",
  components: { BaseLayout },

  data() {
    return {
      product: {},
    };
  },

  mounted() {
    UserService.getProduct(this.$route.params.id).then(
      (response) => {
        this.product = response.data;
      },
      (error) => {
        this.product =
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
