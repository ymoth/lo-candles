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
          <div>
            <label>Эл.почта</label>
            <input type="text" v-model="registration.email" placeholder="email@gmail.com"/>
            <span>{{ emailError }}</span>
          </div>
          <div>
            <label>Пароль</label>
            <input type="password" v-model="registration.password" placeholder="********"/>
            <span>{{ passwordError }}</span>
          </div>
          <div>
            <label>Имя</label>
            <input type="text" v-model="registration.first_name" placeholder="Петр"/>
            <span>{{ firstName }}</span>
          </div>
          <div>
            <label>Фамилия</label>
            <input type="text" v-model="registration.last_name" placeholder="Иванов"/>
            <span>{{ lastName }}</span>
          </div>
          <div>
            <button type="submit">Подтвердить</button>
          </div>
        </form>
      </div>
      <div class="registration__footer">
        <span>Уже есть аккаунт? </span><button @click="openLoginPopup">Войти</button>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Login',
  props: {
    openRegister: {
      type: Boolean,
      default: () => false,
    }
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
    }
  },
  methods: {
    async userRegistration() {
      try {
        const registerResponse = await this.$axios.post('/register', this.registration);
        if(registerResponse.status === 201) {
          const loginResponse = await this.$axios.post('/login',
            {
              email: this.registration.email,
              password: this.registration.password,
            })
          this.$auth.$storage.setUniversal('email', loginResponse.data.email)
          await this.$auth.setUserToken(loginResponse.data.access_token, loginResponse.data.refresh_token) // Получение токена
          this.closeRegisterPopup()
        }
      } catch (err) {
        this.emailError = err.response.data.email
        this.passwordError = err.response.data.password
        this.firstName = err.response.data.first_name
        this.lastName = err.response.data.last_name
      }
    },
    closeRegisterPopup() {
      this.$emit('closeRegisterPopup', {popup: 'register', status: false})
    },
    openLoginPopup() {
      this.$emit('openLoginPopup', {popup: 'login', status: true})
    }
  },
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
        display: flex;
        flex-direction: column;
        label {
          margin-bottom: 5px;
          font-size: 20px;
          font-weight: 500;
        }
        input {
          margin-bottom: 10px;
          padding: 7px 4px 7px 10px;
          border: 1px solid #FF6F95;
          border-radius: 5px;
          &::placeholder {
            font-size: 16px;
            font-weight: 400;
          }
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
          margin-bottom: 20px;
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
}
</style>
