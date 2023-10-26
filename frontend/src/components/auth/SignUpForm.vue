<template>
  <b-form @submit.prevent="register">
    <b-form-group
      id="input-group-1"
      label="Username:"
      label-for="input-1"
      description="We'll never share your username with anyone else."
    >
      <b-form-input
        id="username"
        v-model="form.username"
        type="text"
        placeholder="Enter username"
        required
      >
      </b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-2"
      label="Email:"
      label-for="email"
      description="We'll never share your email with anyone else."
    >
      <b-form-input
        id="email"
        v-model="form.email"
        type="email"
        placeholder="Enter email"
        required
      >
      </b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-3"
      label="Password:"
      label-for="password"
      description="Password must be at least 8 characters."
    >
      <b-form-input
        id="password"
        v-model="form.password"
        type="password"
        placeholder="Enter password"
        required
      >
      </b-form-input>
    </b-form-group>

    <b-form-group
      id="input-group-4"
      label="Repeat password:"
      label-for="passwordRepeat"
      description="Repeat password must be at least 8 characters."
    >
      <b-form-input
        id="passwordRepeat"
        v-model="form.passwordRepeat"
        type="password"
        placeholder="Repeat password"
        required
      >
      </b-form-input>
    </b-form-group>

    <b-button variant="primary" type="submit">Регистрация</b-button>
  </b-form>

  <b-card class="mt-3" header="Form Data Result">
    <pre class="m-0">{{ form }}</pre>
    <div>{{ message }}</div>
  </b-card>
</template>

<script>
import AuthService from "@/services/auth.service";

export default {
  name: "SignUpForm",

  data() {
    return {
      form: {
        username: "",
        email: "",
        password: "",
        passwordRepeat: "",
      },
      message: "",
      loading: false,
    };
  },
  // computed: {
  //   loggedIn() {
  //     return this.$store.state.auth.status.loggedIn;
  //   }
  // },
  // created() {
  //   if (this.loggedIn) {
  //     this.$router.push('/signin');
  //   }
  // },
  methods: {
    // onSubmit(event) {
    //   event.preventDefault();
    //   alert(JSON.stringify(this.form));
    // },
    register() {
      this.loading = true;
      this.message = "";
      this.$store.dispatch("auth/register", this.form).then(
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
<style></style>
