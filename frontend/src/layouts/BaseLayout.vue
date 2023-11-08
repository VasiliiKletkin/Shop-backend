<template>
  <Header />
  <main>
    <b-col cols="9" class="mx-auto border p-3 rounded">
      <slot></slot>
    </b-col>
  </main>
  <Footer />
</template>

<script>
import Header from "../components/base/Header.vue";
import Footer from "../components/base/Footer.vue";

export default {
  name: "BaseLayout",
  components: {
    Header,
    Footer,
  },
};
</script>
