<template>
  <section class="popup">
    <div class="registration">
      <div class="registration-close">
        <button @click="closeLoginPopup">
          <img src="/svgIcon/close.svg" alt="">
        </button>
      </div>
      <div class="registration__header">
        <img src="/header/logo.png" alt="" />
      </div>
      <div class="registration__main">
        <form @submit.prevent="userLogin">
          <div>
            <label>Эл.почта</label>
            <input type="text" v-model="login.email" placeholder="email@gmail.com"/>
            <span>{{ userError }}</span>
          </div>
          <div>
            <label>Пароль</label>
            <input type="password" v-model="login.password" placeholder="********"/>
            <span>{{ passwordError }}</span>
          </div>
          <div>
            <button type="submit">Подтвердить</button>
          </div>
        </form>
      </div>
      <div class="registration__footer">
        <button>Забыли пароль?</button> | <button @click="openRegisterPopup">Регистрация</button>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Login",
  props: {
    openLogin: {
      type: Boolean,
      default: () => false,
    },
    openRegister: {
      type: Boolean,
      default: () => false,
    }
  },
  data() {
    return {
      login: {
        email: '',
        password: ''
      },
      userError: '',
      passwordError: ''
    }
  },
  methods: {
    async userLogin() {
      try {
        const response = await this.$axios.post('/login', this.login)
        this.$auth.$storage.setUniversal('email', response.data.email)
        await this.$auth.setUserToken(response.data.access_token, response.data.refresh_token) // Получение токена
        this.closeLoginPopup()
      } catch (err) {
        this.userError = err.response.data.detail
        this.passwordError = err.response.data.password
      }
    },
    closeLoginPopup() {
      this.$emit('closeLoginPopup', {popup: 'login', status: false})
    },
    openRegisterPopup() {
      this.$emit('openRegisterPopup', {popup: 'register', status: true})
    }
  },
}
</script>

<style scoped>

</style>
