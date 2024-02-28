<template>
  <div
      class="bg-gradient-to-r from-orange-100 to-orange-500 dark:bg-gradient-to-r from-blue-700 to-gray-700 min-h-screen flex flex-col justify-center items-center">
    <div class="flex items-center flex-wrap mb-8">
      <h1 class="text-5xl font-bold text-center font-sans text-black mr-8">Citupia</h1>
      <form @submit.prevent="submitForm" class=" dark:bg-gray-900 bg-gray-100 p-8 rounded-lg shadow-md w-96">
        <h1 class="text-3xl dark:text-blue-400 font-bold mb-8 text-center">Log in</h1>
        <div v-if="errors.wrong_credentials" class="mb-4">
          <label class="text-red-600">{{ errors.wrong_credentials }}</label>
        </div>
        <div class="mb-4">
          <label for="username" class="block dark:text-blue-300 text-black font-bold mb-2">Email</label>
          <input type="username" name="username" v-model="username" placeholder="Email" :class="textInput">
          <small v-if='errors.username' class="text-danger">{{ errors.username }}</small>
        </div>
        <div class="mb-4">
          <label for="password" class="block dark:text-blue-300  text-black font-bold mb-2">Password</label>
          <input type="password" name="password" v-model="password" placeholder="Password" :class="textInput">
          <small v-if='errors.password' class="text-danger">{{ errors.password }}</small>
        </div>
        <div class="mb-2">
          <button type="submit"
                  class="transition focus:ring-4 dark:text-white  focus:ring-pink-400 bg-blue-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:bg-blue-600">
            Log in
          </button>
          <label v-if="invalid" class="text-red-600 pl-4">{{ errorMessage }}</label>
        </div>
        <div>
          <a>Don't have an account? </a>
          <button v-on:click="redirectToSignUp"
                  class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 text-blue-400 hover:underline hover:text-blue-500">
            Sign up!
          </button>
          <button v-on:click="redirectToResetPassword"
                  class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 text-blue-400 hover:underline hover:text-blue-500">
            Forgot password?
          </button>
        </div>
      </form>

    </div>
  </div>
</template>


<!--<template>-->
<!--    <div class="">-->
<!--        <h1>Log in</h1>-->

<!--        <form @submit.prevent="submitForm">-->
<!--            <label for="username">Username</label>-->
<!--            <input type="email" name="username" v-model="username" class="border-2">-->
<!--            <label for="password">Password</label>-->
<!--            <input type="password" name="password" v-model="password" class="border-2">-->
<!--            <button type="submit" class="bg-blue-300">Log in</button>-->
<!--        </form> -->
<!--    </div>-->
<!--</template>-->

<script>
import axios from 'axios';
import axiosClient from './axiosClient';

export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: '',
      errors: {
        username: '',
        password: '',
        wrong_credentials: ''
      }
    }
  },
  methods: {
    isValidForm() {
      let valid = true;
      if (!this.username) {
        this.errors.username = 'Username is required'
      } else {
        this.errors.username = ''
      }
      if (!this.password) {
        this.errors.password = 'Password is required'
      } else {
        this.errors.password = ''
      }
      if (this.errors.username || this.errors.password) {
        valid = false;
      }
      return valid;

    },
    submitForm() {
      if (this.isValidForm()) {
        const url = '/login/';
        axios.post(url, {
          username: this.username,
          password: this.password
        }).then(response => {
          this.$store.commit('setToken', response.data);
          this.username= '';
          this.password= '';
          // if (response.status === 200) {
          //   this.$store.commit('setToken', response.data.token);
          //   this.$store.commit('setUser', response.data.user);
          //   this.$router.push({path: this.$route.query.redirect || '/'});
          // }
        }).catch(error => {
          console.log(error.response.data.non_fields_errors);
          if (error.response.data.non_field_errors) {
            this.errors.wrong_credentials = error.response.data.non_field_errors.join('');
          }
          else {
            this.errors.wrong_credentials = '';
          }
          // if (error.response.status === 400) {
          //   this.errors.wrong_credentials = 'Invalid username or password';
          // }
        });
      } else {
        console.log('invalid form');
      }
    },
    redirectToSignUp() {
      this.$router.push({name: 'SignUp', query: {redirect: this.$route.query.redirect}})
    },
    redirectToResetPassword() {
      this.$router.push({name: 'ForgotPassword', query: {redirect: this.$route.query.redirect}})
    }
  }

}
</script>