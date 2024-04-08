<template v-if="render" class="transition">
    <div class="bg-orange-50 dark:bg-gray-900 h-full md:px-10 pb-20">
        <div class="min-h-screen">
            <div class="flex items-center mb-1 md:px-10 px-3 py-10">
                <br><br>
                <h1 class="text-5xl font-bold">Settings</h1>
            </div>
            <div class="flex border-gray-200 md:px-9 px-4 gap-1 mb-6 rounded-md flex-wrap">
                <button
                        class="transition hover:-translate-y-[2px] focus:ring-inset  shadow-[2px_2px_0px_0px_#000000] focus:ring-4  focus:ring-blue-400 py-2 px-4 text-xl bg-white dark:bg-black text-gray-700 dark:text-gray-200 border-b-2 rounded-md font-medium focus:outline-none dark:focus:bg-gray-800 dark:hover:bg-gray-800 focus:bg-sky-50 hover:bg-sky-50 mr-2"
                        :class="{ 'border-indigo-500 dark:shadow-[2px_2px_0px_0px_#8b5cf6] shadow-[2px_2px_0px_0px_#8b5cf6]': activeTab === 'my-details', 'dark:shadow-[2px_2px_0px_0px_#ffffff]': activeTab !== 'my-details' }"
                        @click="activeTab = 'my-details'"
                >
                    My Details
                </button>
                <button
                        class="transition hover:-translate-y-[2px] focus:ring-inset shadow-[2px_2px_0px_0px_#000000] focus:ring-4 focus:ring-blue-400 py-2 px-4 text-xl bg-white dark:bg-black text-gray-700 dark:text-gray-200 border-b-2 rounded-md font-medium focus:outline-none dark:focus:bg-gray-800 dark:hover:bg-gray-800 focus:bg-sky-50 hover:bg-sky-50 mr-2"
                        :class="{ 'border-indigo-500 dark:shadow-[2px_2px_0px_0px_#8b5cf6] shadow-[2px_2px_0px_0px_#8b5cf6]': activeTab === 'password', 'dark:shadow-[2px_2px_0px_0px_#ffffff]': activeTab !== 'password' }"
                        @click="activeTab = 'password'"
                >
                    Password
                </button>
                <button
                        class="transition hover:-translate-y-[2px] focus:ring-inset  shadow-[2px_2px_0px_0px_#000000] focus:ring-4  focus:ring-blue-400 py-2 px-4 text-xl bg-white dark:bg-black text-gray-700 dark:text-gray-200 border-b-2 rounded-md font-medium focus:outline-none dark:focus:bg-gray-800 dark:hover:bg-gray-800 focus:bg-sky-50 hover:bg-sky-50 mr-2"
                        :class="{ 'border-indigo-500 dark:shadow-[2px_2px_0px_0px_#8b5cf6] shadow-[2px_2px_0px_0px_#8b5cf6]': activeTab === 'accessibility', 'dark:shadow-[2px_2px_0px_0px_#ffffff]': activeTab !== 'accessibility' }"
                        @click="activeTab = 'accessibility'"
                >
                    Accessibility
                </button>
                <button
                        class="transition hover:-translate-y-[2px] focus:ring-inset dark:shadow-[2px_2px_0px_0px_#ffffff] shadow-[2px_2px_0px_0px_#000000] focus:ring-4 focus:ring-blue-400 py-2 px-4 text-xl bg-white dark:bg-black text-gray-700 dark:text-gray-200 border-b-2 rounded-md font-medium focus:outline-none dark:focus:bg-gray-800 dark:hover:bg-gray-800 focus:bg-sky-50 hover:bg-sky-50 mr-2"
                        @click="logout"
                >
                    Logout
                </button>
            </div>
            <div v-if="activeTab === 'my-details'" class="md:px-10 px-3">
                <h2 class="text-2xl font-bold mb-2">My Details</h2>
                <br>
                <form>
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="name">
                            Name:
                        </label>
                        <p class="font-medium mb-2">{{ username }}</p>
                    </div>
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="email">
                            Email:
                        </label>
                        <p class="font-medium mb-2">
                            {{ user_email }}
                        </p>
                    </div>

                </form>
            </div>
            <div v-if="activeTab === 'password'" class="md:px-10 px-3">
                <h2 class="text-2xl font-bold mb-4">Change Password</h2>
                <form @submit.prevent="submitForm">
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="current-password">
                            Current Password
                        </label>
                        <input
                                class="transition focus:ring-4 focus:ring-blue-400 appearance-none border rounded w-full py-2 px-3 text-gray-700 dark:text-gray-200 hover:bg-gray-100 leading-tight focus:outline-none focus:shadow-outline dark:bg-gray-800 dark:hover:bg-gray-700"
                                v-model="old_password"
                                type="password"
                                placeholder="********"
                        />
                    </div>
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="new-password">
                            New Password
                        </label>
                        <input
                                class="transition focus:ring-4 focus:ring-blue-400 appearance-none border rounded w-full py-2 px-3 hover:bg-gray-100 text-gray-700 dark:text-gray-200 leading-tight focus:outline-none focus:shadow-outline dark:bg-gray-800 dark:hover:bg-gray-700"
                                v-model="new_password"
                                type="password"
                                placeholder="********"
                        />
                    </div>
                    <div class="mb-4">
                        <label class="block text-gray-700 dark:text-gray-200 font-bold mb-2" for="confirm-password">
                            Confirm New Password
                        </label>
                        <input
                                class="transition focus:ring-4 focus:ring-blue-400 appearance-none border rounded w-full py-2 px-3 hover:bg-gray-100 text-gray-700 dark:text-gray-200 leading-tight focus:outline-none focus:shadow-outline dark:bg-gray-800 dark:hover:bg-gray-700"
                                v-model="conf_password"
                                type="password"
                                placeholder="********"
                        />
                    </div>
                    <div class="flex items-center justify-between">
                        <button :disabled="isFormComplete"
                                class="transition focus:ring-4  focus:ring-pink-400 bg-blue-500 hover:bg-blue-700 focus:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                                type="submit"
                        >
                            Save Changes
                        </button>
                        <label v-if="success" class="text-green-600 pl-4">{{ successMessage }}</label>
                        <label v-if="invalid" class="text-red-600 pl-4">{{ errorMessage }}</label>
                    </div>
                </form>
            </div>



            <div v-if="activeTab === 'accessibility'" class="md:px-10 px-3">
                <h2 class="text-2xl font-bold mb-4">Accessibility Options</h2>
                <p class="mb-2">Adjust the following settings to enhance the accessibility of this website:</p>
                <br>
                <div class=" rounded-lg md:px-16 px-5 py-8 mb-3  border-2 border-black bg-white dark:bg-gray-800 ">
                    <div class="mb-6">Keyboard shortcuts</div>
                    <div class="flex flex-wrap gap-1">
                      <ul>
                        <li><kbd class="font-bold">alt</kbd> + <kbd class="font-bold">h</kbd> to return home</li>
                        <li><kbd class="font-bold">alt</kbd> + <kbd class="font-bold">k</kbd> to search</li>
                        <li><kbd class="font-bold">alt</kbd> + <kbd class="font-bold">m</kbd> to jump to module bar</li>
                        <li><kbd class="font-bold">alt</kbd> + <kbd class="font-bold">q</kbd> to ask a question on a module specific page</li>


                      </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axiosClient from "@/views/axiosClient";

export default {
    name: "SettingsView",
    data() {
        return {
            activeTab: 'my-details',
            username: '',
            // shouldDeleteContent: false,
            // first_name: '',
            // last_name: '',
            // user_fullname: '',
            user_email: '',
            old_password: '',
            new_password: '',
            conf_password: '',
            // success: false,
            // successName: false,
            // successMessageName: '',
            // successMessage: '',
            // errorMessage: '',
            // errorMessageName: '',
            // invalidName: false,
            // invalid: false,
            largeFontSize: localStorage.getItem("largeFont") === "true",
            readableFont: localStorage.getItem("readableFont") === "true",
            grayscaleMode: localStorage.getItem("grayscale") === "true",
            invert: localStorage.getItem("invert") === "true",
            colourHue: Number(localStorage.getItem("colourHue")) || 0,
            letterSpacing: ['tight', 'normal', 'wide'],
            currentLetterSpacing: localStorage.getItem("letterSpacing") || 'normal',
            highContrastMode: false,
            screenReaderMode: false,
            themeSelect: localStorage.getItem("theme") || "default",
            pageReload: localStorage.getItem("pageReload"),
            render: true,
            showForm: false,

        }
    },
    methods: {


       logout() {
        localStorage.removeItem('authToken'); // Remove the token from localStorage
        this.$store.commit('removeToken'); // Remove the token from the store
        this.$router.push('/log-in/'); // Redirect to login page
    },
        submitForm() {
        // Make sure to send the Authorization header with the token
        const headers = {
            'Authorization': `Token ${this.$store.state.authToken}`
        };

        const formData = {
            new_password: this.new_password,
            re_new_password: this.conf_password,
            current_password: this.old_password,
        };

        axiosClient.post('/auth/users/set_password/', formData, { headers })
            .then(response => {
                // Handle success
                this.success = true;
                this.invalid = false;
                this.successMessage = "Password successfully changed!";
                // Clear the form
                this.old_password = '';
                this.new_password = '';
                this.conf_password = '';
            })
            .catch(error => {
                // Handle error
                if (error.response.status === 400) {
                    this.errorMessage = "Invalid password";
                } else {
                    this.errorMessage = Object.values(error.response.data)[0][0];
                }
                this.invalid = true;
                this.success = false;
            });
    },
    },
    computed: {
        isFormComplete() {
            return (this.old_password === '') || (this.new_password === '') || (this.conf_password === '');
        },
        // isNameFormComplete() {
        //     return (this.first_name === '') || (this.last_name === '');
        // }
    },
    mounted() {
    // Retrieve the token in a way that matches how you store it. This is just an example.
    const token = this.$store.state.authToken || localStorage.getItem('authToken');

    // If there's no token, redirect to login
    if (!token) {
        this.logout();
        return;
    }

    // Set up the request headers
    const headers = {
        'Authorization': `Token ${token}`
    };

    // Make the request to your backend
    axiosClient.get("/api/signup/user-profile/", { headers })
        .then((response) => {
            // Assuming your backend sends the fields 'firstName' and 'lastName'
            this.username = response.data.firstName + ' ' + response.data.lastName;
            this.user_email = response.data.user; // Or however the email is sent in your response
        }).catch((error) => {
            console.error('Error fetching user details', error);
            this.logout(); // Redirect to login if there's an error
        });
}}
</script>

<style scoped>

</style>
