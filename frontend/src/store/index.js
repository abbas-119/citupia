import { createStore } from 'vuex';

// Create a new store instance.
const store = createStore({
  state() {
    return {
      // Define your state here
      count: 0
    };
  },
  mutations: {
    // Define your mutations here
    increment(state) {
      state.count++;
    }
  },
  actions: {
    // Define your actions here
    increment(context) {
      context.commit('increment');
    }
  },
  getters: {
    // Define your getters here
    count: (state) => state.count
  }
});

export default store;
