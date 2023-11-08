<template>
  <base-layout>
    <b-card-group deck>
      <ProductsListItem
        v-for="product in products"
        :key="product.id"
        :id="product.id"
        :title="product.name"
        :price="product.price"
        :description="product.description"
        :image="product.image"
      />
    </b-card-group>
  </base-layout>
</template>

<script>
import ProductsListItem from "../components/ProductsListItem.vue";
import BaseLayout from "../layouts/BaseLayout.vue";
import UserService from "../services/user.service";

export default {
  name: "Products",
  components: { BaseLayout, ProductsListItem },
  data() {
    return {
      products: [],
    };
  },
  mounted() {
    UserService.getProducts().then(
      (response) => {
        this.products = response.data;
      },
      (error) => {
        this.products =
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
.card-deck {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-flow: row wrap;
  flex-flow: row wrap;
  margin-right: -15px;
  margin-left: -15px;
}
</style>
