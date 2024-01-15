<template>
  <div class="bg-gradient-to-r from-orange-100 to-orange-500 dark:bg-gradient-to-r from-blue-700 to-gray-700 min-h-screen flex flex-col justify-center items-center">
    <div class="flex items-center flex-wrap mb-8">
      <h1 class="text-5xl font-bold text-center font-sans text-black mr-8">Citupia</h1>
      <form @submit.prevent="submitForm" class=" dark:bg-gray-900 bg-gray-100 p-8 rounded-lg shadow-md w-96">
        <h1 class="text-3xl dark:text-blue-400 font-bold mb-8 text-center">Sign up</h1>
        <div class="mb-2">
          <label for="firstname" class="block dark:text-blue-400 text-black font-bold mb-1">First name</label>
          <input type="text" name="firstname" v-model="firstname" placeholder="First name"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400 ">
        </div>
        <div class="mb-2">
          <label for="lastname" class="block dark:text-blue-400 text-black font-bold mb-1">Last name</label>
          <input type="text" name="lastname" v-model="lastname" placeholder="Last name"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
        </div>
        <div class="mb-2">
          <label for="lastname" class="block dark:text-blue-400 text-black font-bold mb-1">Categories</label>
          <select v-model="user_type" class="w-full px-3 py-2 border border-gray-300 rounded" required>
          <option>  </option>
          <option value="municipality">Municipality/Transportation Agency</option>
          <option value="traffic_control">Traffic Control and Enforcement</option>
          <option value="consulting_firm">Consulting Firm</option>
          <option value="regular_user">Regular User</option>
        </select>
      </div>

        <div v-if="user_type === 'consulting_firm'" class="mb-2">
          <label for="companyName" class="block dark:text-blue-400 text-black font-bold mb-1">Company Name</label>
          <input type="text" name="companyName" v-model="company" placeholder="Company Name"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
        </div>

        <div v-if="user_type === 'municipality' " class="mb-2">
          <label for="city" class="block dark:text-blue-400 text-black font-bold mb-1">City</label>
          <select v-model="city" class="w-full px-3 py-2 border border-gray-300 rounded" required>
          <option>  </option>
          <option value="Stockholm">Stockholm</option>
          <option value="Braga">Braga</option>
        </select>
      </div>

        <div v-if="user_type === 'traffic_control' " class="mb-2">
          <label for="city" class="block dark:text-blue-400 text-black font-bold mb-1">City</label>
          <select v-model="city" class="w-full px-3 py-2 border border-gray-300 rounded" required>
          <option>  </option>
          <option value="Stockholm">Stockholm</option>
          <option value="Braga">Braga</option>
        </select>
      </div>

        <div v-if="user_type === 'regular_user' " class="mb-2">
          <label for="city" class="block dark:text-blue-400 text-black font-bold mb-1">City</label>
          <select v-model="city" class="w-full px-3 py-2 border border-gray-300 rounded" required>
          <option>  </option>
          <option value="Stockholm">Stockholm</option>
          <option value="Braga">Braga</option>
        </select>
      </div>

        <div v-if="user_type === 'municipality'" class="mb-2">
          <label for="position" class="block dark:text-blue-400 text-black font-bold mb-1">Position</label>
          <input type="text" name="position" v-model="position" placeholder="Position"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
        </div>
        <div v-if="user_type === 'traffic_control'" class="mb-2">
          <label for="position" class="block dark:text-blue-400 text-black font-bold mb-1">Position</label>
          <input type="text" name="position" v-model="position" placeholder="Position"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
        </div>
        <div v-if="user_type === 'consulting_firm'" class="mb-2">
          <label for="position" class="block dark:text-blue-400 text-black font-bold mb-1">Position</label>
          <input type="text" name="position" v-model="position" placeholder="Position"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
        </div>

        <div class="mb-2">
          <label for="username" class="block dark:text-blue-400 text-black font-bold mb-1">Email</label>
          <input :class="validEmail" type="email" name="username" v-model="username" placeholder="Email"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
        </div>

        <div class="mb-2">
          <label for="password" class="block dark:text-blue-400 text-black font-bold mb-1">Password</label>
          <input :class="invalidPasswordBox" type="password" name="password" v-model="password" placeholder="Password"
                 class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
        </div>
        <div class="mb-4">
          <label for="re_password" class="block dark:text-blue-200 text-gray-700 font-bold mb-2">Password confirmation</label>
          <input type="password" name="re_password" v-model="re_password" placeholder="Re-enter Password" :class="invalidPasswordBox" class="transition border-2 p-2 w-full rounded text-gray-700 focus:outline-none focus:ring-4 focus:ring-blue-400">
        </div>
        <div class="mb-3">
          <p class="text-gray-700 font-bold mb-2">By signing up, you agree to our <a href="/privacy" target="_blank" class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 text-blue-400 hover:underline hover:text-blue-500">Privacy Policy</a> and a email wil be sent to activate your account.</p>
        </div>
        <div class="mb-3 flex content-center">
          <button :disabled="!isValidEmail || isFormComplete" type="submit"
                  class="transition focus:ring-4 focus:ring-pink-400 flex-none h-[40px] bg-blue-500 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline hover:bg-blue-600 disabled:bg-gray-500">
            Sign up
          </button>
          <div class="ml-4">
            <label v-if="invalid" class="text-red-600 ">{{ errorMessage }}</label>
          </div>
        </div>
        <div>
          <a>Already have an account? </a>
          <a href="/log-in/" class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 text-blue-400 hover:underline hover:text-blue-500">Log in!</a>
        </div>
      </form>
    </div>
  </div>
</template>


<script>
import axiosClient from './axiosClient';

export default {
  name: 'SignUpView',
  data() {
    return {
      username: '',
      password: '',
      re_password: '',
      firstname: '',
      lastname: '',
      validEmail: '',
      company:'',
      city:'',
      position:'',
      user_type:'',
      invalid: false,
      invalidPasswordBox: '',
      errorMessage: ''
      
    }
  },
  computed: {
    isValidEmail() {
      if(/^[^@]+@\w+(\.\w+)+\w$/.test(this.username)){
        this.validEmail = 'border-green-500 focus:ring-green-400'
        return true
      }
      else{ 
        this.validEmail = 'focus:ring-blue-400 border-gray-200'
        return false
      }
    },
    isFormComplete(){
      return (this.username === '') || (this.password === '') || (this.re_password === '') || (this.firstname === '') || (this.lastname === '') || (this.user_type === '') ;
    }
  },
  methods: {
    submitForm(e) {
      console.log(this.lastname)
    // First POST request to create the user
      axiosClient.post('/v1/users/', {
        username: this.username,
        email: this.username,
        first_name: this.firstname,
        last_name: this.lastname,
        user_type: this.user_type,
        company: this.company,
        city: this.city,
        position: this.position,
        password: this.password,
        re_password: this.re_password,
    })
          .then(response => {
            // Second POST request to save additional user information
            axiosClient.post(`/signup/`, {
              username: this.username,
              first_name: this.firstname,
              last_name: this.lastname,
              user_type: this.user_type,
              company: this.company,
              city: this.city,
              position: this.position,
            })

            // Redirect to login page upon successful registration
            this.$router.push({name: 'LogIn', query: {redirect: this.$route.query.redirect}});
          })
      .catch(error => {
            console.log(error)
            if(Object.values(error.response.data)[0][0] == "A user with that username already exists."){
              this.errorMessage = "Email already in use."
            }
            else {
              this.errorMessage = Object.values(error.response.data)[0][0]
              this.invalidPasswordBox= 'border-red-500 focus:ring-red-100'
            }
            this.invalid = true

          })
  }
}

}
</script>