<template>
  <section class="popup">
    <div class="registration">
      <div class="registration-close">
        <button @click="closeRegisterPopup">
          <img src="/svgIcon/close.svg" alt="">
        </button>
      </div>
      <div class="registration__header">
        <img src="/header/logo.png" alt="" />
      </div>
      <div class="registration__main">
        <form @submit.prevent="userRegistration">
          <div class="input-container">
            <input
              type="text"
              v-model="registration.email"
              placeholder=" "
              :class="{ 'error-input': emailError }"
              @focus="onInputFocus"
              @blur="onInputBlur"
            />
            <label :class="[{
              'floating-label': true,
              'active': registration.email || emailError,
              'error-label': emailError
            }]">
              Эл.почта
            </label>
            <span class="error-container" :class="{ 'error-active': emailError }">{{ emailError }}</span>
          </div>
          <div class="input-container">
            <input
              type="password"
              v-model="registration.password"
              placeholder=" "
              :class="{ 'error-input': passwordError }"
              @focus="onInputFocus"
              @blur="onInputBlur"
              ref="passwordInput"
            />
            <label :class="[{
              'floating-label': true,
              'active': registration.password || passwordError,
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
          <div class="input-container">
            <input
              type="text"
              v-model="registration.first_name"
              placeholder=" "
              :class="{ 'error-input': firstName }"
              @focus="onInputFocus"
              @blur="onInputBlur"
            />
            <label :class="[{
              'floating-label': true,
              'active': registration.firstName || firstName,
              'error-label': firstName
            }]">
              Имя
            </label>
            <span class="error-container" :class="{ 'error-active': firstName }">{{ firstName }}</span>
          </div>
          <div class="input-container">
            <input
              type="text"
              v-model="registration.last_name"
              placeholder=" "
              :class="{ 'error-input': lastName }"
              @focus="onInputFocus"
              @blur="onInputBlur"
            />
            <label :class="[{
              'floating-label': true,
              'active': registration.lastName || lastName,
              'error-label': lastName
            }]">
              Фамилия
            </label>
            <span class="error-container" :class="{ 'error-active': lastName }">{{ lastName }}</span>
          </div>
          <div>
            <button
              :disabled="isSubmitDisabled"
              :class="{ 'normal-button': !isSubmitDisabled, 'disabled-button': isSubmitDisabled }">
              Подтвердить
            </button>
          </div>
        </form>
      </div>
      <div class="registration__footer">
        <span>Уже есть аккаунт? </span><button @click="openLoginPopup">Войти</button>
      </div>
    </div>
    <Spinner ref="spinner"/>
  </section>
</template>

<script>
import Spinner from "~/components/Spinner.vue";
export default {
  name: 'Login',
  props: {
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
      registration: {
        email: '',
        password: '',
        first_name: '',
        last_name: ''
      },
      emailError: '',
      passwordError: '',
      firstName: '',
      lastName: '',
      isSubmitting: false,
      showPassword: false,
    }
  },
  methods: {
    async userRegistration() {
      try {
        const registerResponse = await this.$axios.post('/register', this.registration);

        if (registerResponse.status === 200) {
          this.$cookies.set("email", this.registration.email)
          this.$cookies.set("registration", this.registration)
          location.reload()
        }
      } catch (error) {

        this.emailError = error.response.data.email ? error.response.data.email.join(' ') : '';
        this.passwordError = error.response.data.password ? error.response.data.password.join(' ') : '';
        this.firstName = error.response.data.first_name ? error.response.data.first_name.join(' ') : '';
        this.lastName = error.response.data.last_name ? error.response.data.last_name.join(' ') : '';

        document.querySelectorAll('.error-container').forEach(container => {
          if (container.textContent.trim() !== '') {
            container.classList.add('active');
          } else {
            container.classList.remove('active');
          }
        });
      } finally {
        this.$refs.spinner.finish();
      }
    },
    onInputFocus(e) {
      const label = e.target.nextElementSibling;
      label.classList.add('active');
      this.emailError = '';
      this.passwordError = '';
      this.firstName = '';
      this.lastName = '';
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
    closeRegisterPopup() {
      this.$emit('closeRegisterPopup', {popup: 'register', status: false})
    },
    openLoginPopup() {
      this.$emit('openLoginPopup', {popup: 'login', status: true})
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword;
      const passwordInput = this.$refs.passwordInput;
      passwordInput.type = this.showPassword ? 'text' : 'password';
    }
  },
  computed: {
    isSubmitDisabled() {
      return !(this.registration.email && this.registration.password && this.registration.first_name && this.registration.last_name);
    },
    labelClasses() {
      return {
        'floating-label': true,
        'active': this.labelActive,
        'error-label': this.labelError
      };
    }
  }
}
</script>

<style lang="scss">
.registration {
  width: 400px;
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0px 2px rgba(0, 1, 1, 1);
  &-close {
    display: flex;
    justify-content: flex-end;
  }
  &__header {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 15px;
  }
  &__main {
    form {
      div {
        position: relative;
        display: flex;
        flex-direction: column;
        margin-bottom: 1rem;
        label {
          margin-bottom: 5px;
          font-size: 16px;
          font-weight: 500;
        }
        input {
          padding: 10px 4px 10px 10px;
          border: 1px solid #9d7d86;
          border-radius: 5px;
          position: relative;
          &::placeholder {
            font-size: 16px;
            font-weight: 400;
          }
        }
        .error-input {
          border: 1px solid red;
        }
        span {
          text-align: end;
          color: red;
        }
        button {
          background: #FF6F95;
          padding: 5px;
          color: #fff;
          font-size: 18px;
          border-radius: 5px;
          margin-top: 10px;
          transition: box-shadow 0.2s ease, background 0.3s;
        }

        button:hover {
          background: #FF5177;
        }

        .disabled-button {
          background: #ef9bb3;
          cursor: not-allowed;
        }
      }

    }
  }
  &__footer {
    text-align: center;
    button {
      color: cornflowerblue;
      text-decoration: underline;
    }
  }
  .password-toggle {
    position: absolute;
    top: 78%;
    right: 10px;
    transform: translateY(-50%);
    cursor: pointer;
    height: 100%;
    display: flex;
    align-items: center;
  }

  .password-toggle img {
    max-height: 100%;
  }
  .floating-label {
    position: absolute;
    top: 11px;
    left: 10px;
    transition: transform 0.2s ease, font-size 0.2s ease, top 0.2s ease;
    pointer-events: none;
    color: gray;
    background: #fff;
    padding: 0 3px;
  }

  input:focus {
    border: 1px solid #2f7fd9;
  }
  .floating-label.active {
    transform: translateY(1px);
    font-size: 15px;
    top: -10px;
    color: #2f7fd9;
  }
  input:not(:focus) + .floating-label.active {
    color: gray;
  }
  input:not(:focus) + .error-label.active {
    color: rgba(253, 105, 105, 0.99);
  }
  .error-label.active {
    color: rgba(253, 105, 105, 0.99);
  }
  .error-label {
    color: rgba(253, 105, 105, 0.99);
  }
  .error-container {
    display: inline-block;
    max-height: 0;
    overflow: hidden;
    opacity: 0;
    transition: max-height 0.3s ease, opacity 0.3s ease;
  }

  .error-active {
    max-height: 100px;
    opacity: 1;
  }
}

</style>
