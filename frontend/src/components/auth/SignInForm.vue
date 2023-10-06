<template>
  <b-form @submit.prevent="login">
    <b-form-group
      id="input-group-1"
      label="Username:"
      label-for="input-1"
      description="We'll never share your username with anyone else."
    >
      <b-form-input
        id="input-1"
        v-model="form.username"
        type="text"
        placeholder="Enter username"
        required
      ></b-form-input>
    </b-form-group>

    <b-form-group id="input-group-2" label="Password:" label-for="input-2">
      <b-form-input
        id="input-2"
        v-model="form.password"
        placeholder="Enter password"
        type="password"
        required
      ></b-form-input>
    </b-form-group>

    <b-button variant="primary" type="submit">Войти</b-button>
  </b-form>

  <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card>
</template>

<script>

export default {
  name: "SignIn",
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
      message: "",
      loading: false,
    };
  },
  // computed: {
  //   loggedIn() {
  //     return this.$store.state.auth.status.loggedIn;
  //   },
  // },
  // created() {
  //   if (this.loggedIn) {
  //     // this.$router.push('/profile');
  //   }
  // },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      alert(JSON.stringify(this.form));
    },
    login() {
      this.loading = true;
      this.message = "";
      this.$store.dispatch("auth/login", this.form).then(
        (data) => {
          this.$router.push("/");
          this.message = data.message;
        },
        (error) => {
          this.message =
            (error.response &&
              error.response.data &&
              error.response.data.message) ||
            error.message ||
            error.toString();
        }
      );
    },
  },
};
</script>
