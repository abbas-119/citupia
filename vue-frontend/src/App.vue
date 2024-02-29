<template class="hue-rotate-[30deg] hue-rotate-[60deg] hue-rotate-[90deg] hue-rotate-[120deg] hue-rotate-[150deg] hue-rotate-[180deg] hue-rotate-[210deg] hue-rotate-[240deg] hue-rotate-[270deg] hue-rotate-[300deg] hue-rotate-[330deg] hue-rotate-[360deg]
hue-rotate-[-30deg] hue-rotate-[-60deg] hue-rotate-[-90deg] hue-rotate-[-120deg] hue-rotate-[-150deg] hue-rotate-[-180deg] hue-rotate-[-210deg] hue-rotate-[-240deg] hue-rotate-[-270deg] hue-rotate-[-300deg] hue-rotate-[-330deg] hue-rotate-[-360deg] tracking-tight tracking-wide">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <nav v-if="enable"
       class=" px-2 sm:px-4 border-b-[3px] border-black dark:border-white text-black dark:text-white"
       id="nav-vue">
    <div class="container mx-auto flex flex-wrap items-center justify-between h-full">
      <router-link to="/" class="pl-4 transition focus:ring-4 focus:outline-none focus:ring-blue-400">
        <img src="@/store/WaaS main.png" alt="WaaS Logo" class="h-8">
      </router-link>
      <div class="w-auto" id="navbar-default">
        <ul class="flex flex-col p-4 md:space-x-8 md:mt-0 md:flex-row md:border-0 md:text-sm md:font-medium">
          <li>
            <a href="/settings/"
               class="transition focus:ring-4 focus:outline-none focus:ring-blue-400 block rounded py-2 pr-4 pl-3 text-gray-700 dark:text-gray-200 hover:bg-gray-100 md:border-0 md:p-0 md:hover:bg-transparent md:hover:text-blue-700"><i
                class="fa fa-cog scale-150 pr-2" aria-hidden="true"></i>Settings</a>
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
    handleKeyboardShortcuts(event) {
      if (event.altKey && (event.key === 'K' || event.key === 'k')) {
        this.$refs.search.focus()
      }
      if (event.altKey && (event.key === 'M' || event.key === 'm')) {
        this.$refs.modules.focus()
      }
      if (event.altKey && (event.key === 'H' || event.key === 'h')) {
        this.$router.push({path: '/'})
      }
      if (event.altKey && (event.key === 'Q' || event.key === 'q') && this.$route.params.mod) {
        this.$router.push({path: '/ask/' + this.$route.params.mod})
      }
    },

    logout() {
      axiosClient.post('/v1/token/logout/')
          .then(response => {

            this.$store.commit('removeToken')

            axiosClient.defaults.headers.common['Authorization'] = ""
            localStorage.setItem("token", "")
            this.$router.push('/log-in/')
          })
          .catch(error => {
            console.log(error)
          })
    },
    // loadModules() {
    //   axiosClient.get('/module/list/')
    //       .then(response => {
    //         this.modules = response.data
    //       })
    //       .catch(error => {
    //         console.log(error)
    //         if (error.response.status === 401) {
    //           this.clientSideLogout()
    //         }
    //       })
    // },
    // clientSideLogout() {
    //   this.$store.commit('removeToken')
    //
    //   axiosClient.defaults.headers.common['Authorization'] = ""
    //   localStorage.setItem("token", "")
    //   this.$router.push('/log-in/')
    // }
  }
  ,
  created() {
    window.addEventListener('keydown', this.handleKeyboardShortcuts)

    // if (this.$store.state.isAuthenticated) {
    //   this.loadModules()
    // }

    if (localStorage.getItem("theme") === "dark") {
      document.body.classList.remove('light')
      document.body.classList.add('dark')
    } else if (localStorage.getItem("theme") === "light") {
      document.body.classList.remove('dark')
      document.body.classList.add('light')
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      document.body.classList.remove('light')
      document.body.classList.add('dark')
    } else {
      document.body.classList.remove('dark')
      document.body.classList.add('light')
    }
  }
  ,

  beforeDestroy() {
    console.log("before destroy")
    window.removeEventListener('keydown', this.handleKeyboardShortcuts)
  },
}


</script>
