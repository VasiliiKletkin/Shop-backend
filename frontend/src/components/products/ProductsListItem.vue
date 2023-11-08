<script>
export default {
  name: "ProductListItem",
  props: {
    id: Number,
    title: String,
    price: Number,
    description: String,
    image: String,
  },
};
</script>

<template>
  <b-card
    :title="this.title"
    img-src="https://picsum.photos/600/300/?image=25"
    img-alt="https://picsum.photos/600/300/?image=25"
    img-top
    tag="article"
    style="max-width: 20rem"
  >
    <b-card-text>
      {{ this.description }}
    </b-card-text>
    <b-button href="#" variant="primary">Положить в корзину</b-button>
  </b-card>
</template>
