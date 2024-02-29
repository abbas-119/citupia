<template>
  <div class="bg-gray-900 min-h-screen flex justify-center items-center">
    <div class="w-full max-w-md p-8 bg-white rounded-lg shadow-xl space-y-6">
      <h1 class="text-4xl font-bold text-center text-gray-900">Welcome to WaaS</h1>
      <form @submit.prevent="submitForm" class="space-y-4">
        <label class="text-red-600">{{ errors.wrong_credentials }}</label>
        <div class="relative">
          <input type="username" name="username" v-model="username" placeholder="Username"
                 class="w-full px-4 py-3 placeholder-gray-500 text-gray-900 bg-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"/>
          <label class="absolute top-0 left-3 -mt-2 text-xs text-gray-500" :class="{ 'text-blue-500': username }">Username</label>
          <small v-if='errors.username' class="text-danger">{{ errors.username }}</small>
        </div>
        <div class="relative">
          <input type="password" name="password" v-model="password" placeholder="Password"
                 class="w-full px-4 py-3 placeholder-gray-500 text-gray-900 bg-gray-100 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"/>
          <label class="absolute top-0 left-3 -mt-2 text-xs text-gray-500" :class="{ 'text-blue-500': password }">Password</label>
          <small v-if='errors.password' class="text-danger">{{ errors.password }}</small>
        </div>
        <button type="submit" class="w-full py-3 text-white font-bold bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg hover:from-blue-600 hover:to-blue-700 transition duration-300">
          Log in
        </button>
      </form>
      <div class="text-center">
        <a href="/password/reset" class="text-blue-500 hover:underline">Forgot password?</a>
      </div>
      <div class="text-center text-gray-700">
        <span>Don't have an account?</span>
        <br>
        <a href="/sign-up/" class="text-blue-500 hover:underline">Sign up now</a>
      </div>
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
          this.$router.push('/')
          // if (response.status === 200) {
          //   this.$store.commit('setToken', response.data.token);
          //   this.$store.commit('setUser', response.data.user);
          //   this.$router.push({path: this.$route.query.redirect || '/'});
          // }
        }).catch(error => {
          // console.log(error.response.data.non_fields_errors);
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