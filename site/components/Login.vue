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
          <div class="input-container">
            <input
              type="text"
              v-model="login.email"
              placeholder=" "
              :class="{ 'error-input': userError }"
              @focus="onInputFocus"
              @blur="onInputBlur"
            />
            <label :class="[{
              'floating-label': true,
              'active': login.email || userError,
              'error-label': userError
            }]">
              Эл.почта
            </label>
            <span class="error-container" :class="{ 'error-active': userError }">{{ userError }}</span>
          </div>
          <div class="input-container">
            <input
              type="password"
              v-model="login.password"
              placeholder=" "
              :class="{ 'error-input': passwordError }"
              @focus="onInputFocus"
              @blur="onInputBlur"
              ref="passwordInput"
            />
            <label :class="[{
              'floating-label': true,
              'active': login.password || passwordError,
              'error-label': passwordError
            }]">
              Пароль
            </label>
            <span class="error-container" :class="{ 'error-active': passwordError }">{{ passwordError }}</span>
            <div class="password-toggle" @click="togglePasswordVisibility">
              <img v-if="showPassword" src="/popup/eye-open.svg" alt="Show Password" />
              <img v-else src="/popup/eye-closed.svg" alt="Hide Password" />
            </div>
          </div>
          <div>
            <button
              type="submit"
              :disabled="isSubmitDisabled"
              :class="{ 'normal-button': !isSubmitDisabled, 'disabled-button': isSubmitDisabled }"
            >
              Подтвердить
            </button>
          </div>
        </form>
      </div>
      <div class="registration__footer">
        <button>Забыли пароль?</button> | <button @click="openRegisterPopup">Регистрация</button>
      </div>
    </div>
    <Spinner ref="spinner" />
  </section>
</template>

<script>
import Spinner from '~/components/Spinner';
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
  components: {
    Spinner
  },
  data() {
    return {
      login: {
        email: '',
        password: ''
      },
      userError: '',
      passwordError: '',
      isSubmitting: false,
      showPassword: false,
    }
  },
  methods: {
    async userLogin() {
      try {
        const response = await this.$axios.post('/login', this.login)
        this.isSubmitting = true;
        this.$refs.spinner.start();
        this.$auth.$storage.setUniversal('email', response.data.email)
        await this.$auth.setUserToken(response.data.access_token, response.data.refresh_token)
        this.closeLoginPopup()
        this.$emit('notificationLogin', 'login')
      } catch (err) {
        this.userError = err.response.data.detail
        this.passwordError = err.response.data.password

        document.querySelectorAll('.error-container').forEach(container => {
          if (container.textContent.trim() !== '') {
            container.classList.add('active');
          } else {
            container.classList.remove('active');
          }
        });
      } finally {
        this.isSubmitting = false;
        this.$refs.spinner.finish();
      }
    },
    closeLoginPopup() {
      this.$emit('closeLoginPopup', {popup: 'login', status: false})
    },
    openRegisterPopup() {
      this.$emit('openRegisterPopup', {popup: 'register', status: true})
    },
    onInputFocus(e) {
      const label = e.target.nextElementSibling;
      label.classList.add('active');
      this.userError = '';
      this.passwordError = '';
    },
    onInputBlur(e) {
      const input = e.target;
      const label = input.nextElementSibling;

      if (!input.value) {
        label.classList.remove('active');
      } else {
        label.classList.add('active');
      }
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
      const passwordInput = this.$refs.passwordInput;
      passwordInput.type = this.showPassword ? 'text' : 'password';
    }
  },
  computed: {
    isSubmitDisabled() {
      return !(this.login.email && this.login.password);
    }
  }
}
</script>

<style scoped>

</style>
