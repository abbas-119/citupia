<template>
  <div class="bg-gray-900 min-h-screen flex justify-center items-center">
    <div class="w-full max-w-md p-8 bg-white rounded-lg shadow-xl space-y-6">
      <h1 class="text-4xl font-bold text-center text-gray-900">Sign Up</h1>
      <form @submit.prevent="submitForm" class="dark:bg-gray-900 bg-gray-100 p-8 rounded-lg shadow-md w-96">
        <div class="mb-2">
          <label for="username" class="block dark:text-blue-400 text-black font-bold mb-1">Email</label>
          <input  type="email" name="username" v-model="username" placeholder="Email"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
          <small v-if='errors.username' class="text-danger">{{ errors.username }}</small>
        </div>
<!--        <div class="mb-2">-->
<!--          <label for="email" class="block dark:text-blue-400 text-black font-bold mb-1">Email</label>-->
<!--          <input  type="email" name="email" v-model="email" placeholder="Email"-->
<!--                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">-->
<!--          <small v-if='errors.email' class="text-danger">{{ errors.email }}</small>-->
<!--        </div>-->

        <div class="mb-2">
          <label for="firstName" class="block dark:text-blue-400 text-black font-bold mb-1">First name</label>
          <input type="text" name="firstName" v-model="firstName" placeholder="First name"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
        </div>
        <div class="mb-2">
          <label for="lastName" class="block dark:text-blue-400 text-black font-bold mb-1">Last name</label>
          <input type="text" name="lastName" v-model="lastName" placeholder="Last name"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
        </div>
        <div class="mb-2">
          <label for="user_type" class="block dark:text-blue-400 text-black font-bold mb-1">Categories</label>
          <select v-model="user_type" class="w-full px-3 py-2 border border-gray-300 rounded" required>
            <option value="municipality">Municipality/Transportation Agency</option>
            <option value="traffic_control">Traffic Control and Enforcement</option>
            <option value="consulting_firm">Consulting Firm</option>
            <option value="regular_user">Regular User</option>
          </select>
        </div>
        <div class="mb-2">
          <label for="password" class="block dark-text-blue-400 text-black font-bold mb-1">Password</label>
          <input :class="invalidPasswordBox" type="password" name="password" v-model="password" placeholder="Password"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
          <small v-if='errors.password' class="text-danger">{{ errors.password }}</small>
        </div>
        <div class="mb-4">
          <label for="re_password" class="block dark-text-blue-200 text-gray-700 font-bold mb-2">Password confirmation</label>
          <input type="password" name="re_password" v-model="re_password" placeholder="Re-enter Password" :class="invalidPasswordBox" class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
<small v-if='errors.re_password' class="text-danger">{{ errors.re_password }}</small>
        </div>

<!--        <div v-if="user_type === 'consulting_firm'" class="mb-2">-->
<!--          <label for="company" class="block dark:text-blue-400 text-black font-bold mb-1">Company Name</label>-->
<!--          <input type="text" name="company" v-model="company" placeholder="Company Name"-->
<!--                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">-->
<!--        </div>-->
<!--        <div v-if="user_type === 'municipality'" class="mb-2">-->
<!--          <label for="city" class="block dark:text-blue-400 text-black font-bold mb-1">City</label>-->
<!--          <select v-model="city" class="w-full px-3 py-2 border border-gray-300 rounded" required>-->
<!--            <option value="Stockholm">Stockholm</option>-->
<!--          </select>-->
<!--        </div>-->
<!--        <div class="mb-2">-->
<!--          <label for="position" class="block dark:text-blue-400 text-black font-bold mb-1">Position</label>-->
<!--          <input type="text" name="position" v-model="position" placeholder="Position"-->
<!--                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">-->
<!--        </div>-->
        <div class="mb-3">
          <p class="text-gray-700 font-bold mb-2">By signing up, you agree to our <a href="/privacy" target="_blank" class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 text-blue-400 hover:underline hover:text-blue-500">Privacy Policy</a> and an email will be sent to activate your account.</p>
        </div>
        <div class="mb-3 flex content-center">
          <button type="submit"
                  class="transition focus:ring-4 focus:ring-pink-400 flex-none h-[40px] bg-blue-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:bg-blue-600 disabled:bg-gray-500">
            Sign up
          </button>
<!--          <div class="ml-4">-->
<!--            <label v-if="invalid" class="text-red-600 ">{{ errorMessage }}</label>-->
<!--          </div>-->
        </div>
        <div>
          <a>Already have an account? </a>
          <router-link to="/log-in/" class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 text-blue-400 hover:underline hover:text-blue-500">Log in!</router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axiosClient from './axiosClient';
import axios from "axios";

export default {
  name: 'SignUpView',
  data() {
    return {
      username: '',
      // email: '',
      password: '',
      re_password: '',
      firstName: '',
      lastName: '',
      user_type: 'municipality',
      // company: '',
      // city: 'Stockholm',
      // position: '',
      // validEmail: '',
      // invalid: false,
      errors: {
        username: '',
        // email: '',
        password: '',
        re_password: '',
        wrong_credentials: ''
      }
    };
  },
  // computed: {
  //   isValidEmail() {
  //     if (/^[^@]+@\w+(\.\w+)+\w$/.test(this.username)) {
  //       this.validEmail = 'border-green-500 focus:ring-green-400';
  //       return true;
  //     } else {
  //       this.validEmail = 'focus:ring-blue-400 border-gray-200';
  //       return false;
  //     }
  //   },
  //   isFormComplete() {
  //     return (
  //       this.username === '' ||
  //       this.password === '' ||
  //       this.confirmPassword === '' ||
  //       this.firstname === '' ||
  //       this.lastname === ''
  //     );
  //   },
  // },
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
      if (this.password&&this.re_password&&this.password!==this.re_password) {
        this.errors.re_password = 'Passwords do not match'
      } else {
        this.errors.re_password = ''
      }
      if (this.errors.username || this.errors.password || this.errors.re_password) {
        valid = false;
      }
      return valid;

    },
    submitForm() {
  if (this.isValidForm()) {
    const url = '/api/signup/';
    axios.post(url, {
      username: this.username,
      password: this.password,
      re_password: this.re_password,
      firstName: this.firstName,
      lastName: this.lastName,
      user_type: this.user_type,
    }).then(response => {
      // Handle success
      console.log('Signup successful', response.data);
      this.$router.push('/log-in/');
    }).catch(error => {
      // Handle error
      console.log('Signup error', error.response.data);
    });
  }
},
  },
};
</script>
