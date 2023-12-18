<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <div class="bg-red-500">hi</div>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
