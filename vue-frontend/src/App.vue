<template class="hue-rotate-[30deg] hue-rotate-[60deg] hue-rotate-[90deg] hue-rotate-[120deg] hue-rotate-[150deg] hue-rotate-[180deg] hue-rotate-[210deg] hue-rotate-[240deg] hue-rotate-[270deg] hue-rotate-[300deg] hue-rotate-[330deg] hue-rotate-[360deg]
hue-rotate-[-30deg] hue-rotate-[-60deg] hue-rotate-[-90deg] hue-rotate-[-120deg] hue-rotate-[-150deg] hue-rotate-[-180deg] hue-rotate-[-210deg] hue-rotate-[-240deg] hue-rotate-[-270deg] hue-rotate-[-300deg] hue-rotate-[-330deg] hue-rotate-[-360deg] tracking-tight tracking-wide">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <nav v-if="enable"
       class=" px-2 sm:px-4 border-b-[3px] border-black dark:border-white text-black dark:text-white"
       id="nav-vue">
    <div class="container mx-auto flex flex-wrap items-center justify-between h-full">
      <router-link to="/" class="pl-4 transition focus:ring-4 focus:outline-none focus:ring-blue-400">
        <img src="@/store/WaaS main.png" alt="WaaS Logo" class="h-10">
      </router-link>
      <div class="w-auto" id="navbar-default">
        <ul class="flex flex-col p-4 md:space-x-8 md:mt-0 md:flex-row md:border-0 md:text-sm md:font-medium">
          <li>
            <!-- In your App.vue template -->
            <button v-if="!$route.meta.hideLogout" @click="logout" class="logout-button">Logout</button>

          </li>
        </ul>
      </div>
    </div>
  </nav>
  <div class="flex text-black dark:text-white">

    <div class="w-full">
      <router-view/>
    </div>
  </div>

  <footer
      class="border-t-[3px] dark:border-white border-black  dark:bg-slate-900 p-4 shadow md:flex md:items-center md:justify-between md:p-6 text-black dark:text-white text-sm">
    <span class=" sm:text-center">© 2023 <a href="#" class="hover:underline">Citupia</a>. All Rights Reserved.
    </span>
    <ul class="mt-3 flex flex-wrap items-center sm:mt-0">
      <li>
        <a target="_blank" href="/privacy" class="mr-4 hover:underline md:mr-6">Privacy Policy</a>
      </li>
    </ul>
  </footer>

</template>

<script>
import axiosClient from '@/views/axiosClient';

export default {
  mounted() {
    this.$store.commit('initializeStore')


  },
  name: 'App',

  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token

    console.log(token)

    if (token) {
      axiosClient.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axiosClient.defaults.headers.common['Authorization'] = ''
    }

  },
  data() {
    return {
      showMobileNav: false,
      searchTerm: '',
      enable: true,
      modules: [],
      showModule: false
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('authToken'); // Remove the token from localStorage
      this.$store.commit('removeToken'); // Remove the token from the store
      delete axiosClient.defaults.headers.common['Authorization']; // Remove the token from axiosClient defaults
      this.$router.push('/log-in/'); // Redirect to login page
    },
    handleKeyboardShortcuts(event) {

      if (event.altKey && (event.key === 'H' || event.key === 'h')) {
        this.$router.push({path: '/'})
      }

    },

  }
}

</script>
