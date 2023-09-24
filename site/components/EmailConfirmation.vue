<template>
  <div class="email__confirm">
    <div class="email__confirm-title">
      <img src="/header/logo.png" alt="">
      <h2>Подтвердите почту</h2>
    </div>
    <div class="email__confirm-subtitle">
      <span>Мы отправили на почту {{ email }} 6-ти значный код подтверждения,</span>
      <span>что-бы пользоваться нашим магазином, пожалуйста введите код в эти колонки.</span>
    </div>
    <div class="email__confirm-input">
      <input
        v-for="(char, index) in code"
        :key="index"
        v-model="code[index]"
        @input="onInput(index)"
        @paste="onPaste"
        type="text"
        placeholder="·"
        maxlength="1"
        :ref="`input${index}`"
        pattern="\d"
      />
    </div>
    <div class="email-error">
      <span>{{ errorConfirm }}</span>
    </div>
    <div class="email__confirm-button">
      <button @click="emailConfirm">
        Подтвердить
      </button>
      <button @click="backToHome">
        Указал неправильную почту
      </button>
    </div>
    <Spinner ref="spinner"/>
  </div>
</template>

<script>
import spinner from "~/components/Spinner.vue";
export default {
  name: "emailConfirmation",
  data() {
    return {
      code: ['', '', '', '', '', ''],
      errorConfirm: "",
    };
  },
  components: {
    spinner
  },
  methods: {
    onInput(index) {
      if (this.code[index] && index < this.code.length - 1) {
        this.$refs[`input${index + 1}`][0].focus();
      } else if (!this.code[index] && index > 0) {
        this.$refs[`input${index - 1}`][0].focus();
      }
      if (this.code.every(char => char !== '')) {
        this.emailConfirm();
      }
    },
    onPaste(event) {
      event.preventDefault();
      const clipboardData = event.clipboardData || window.clipboardData;
      const pastedData = clipboardData.getData('text');

      if (pastedData.length <= this.code.length) {
        this.code = pastedData.split('');

        const lastInputIndex = this.code.length - 1;
        this.$refs[`input${lastInputIndex}`][0].focus();
      }
    },
    async emailConfirm() {
      try {
        const codeString = this.code.join('')
        const email = this.$cookies.get('email')
        const registrationData = this.$cookies.get('registration')
        const confirm = await this.$axios.post('https://dev.aromatic.kz/api/v1/confirmEmail', {
          access_code: codeString,
          email: email
        })
        if(confirm.status === 200) {
          this.$refs.spinner.start();
          const loginResponse = await this.$axios.post('/login',
            {
              email: registrationData.email,
              password: registrationData.password,
            })
          this.$auth.$storage.setUniversal('email', loginResponse.data.email)
          await this.$auth.setUserToken(loginResponse.data.access_token, loginResponse.data.refresh_token) // Получение токена
          this.$emit('notificationRegister', 'register')
          this.$cookies.removeAll()
          await this.$router.push('/');
        }
      } catch (e) {
        this.errorConfirm = e.response.data.error ? e.response.data.error.join(' ') : ''
      } finally {
        this.$refs.spinner.finish();
      }
    },
    backToHome() {
      this.$cookies.removeAll()
      location.href = '/'
    }
  },
  computed: {
    email() {
      return this.$cookies.get('email')
    }
  }
}
</script>

<style lang="scss">
.email__confirm {
  width: 400px;
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0px 2px rgba(0, 1, 1, 1);
  margin: 100px auto;
  &-title {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-bottom: 30px;
  }
  &-subtitle {
    margin-bottom: 30px;
    text-align: center;
  }
  &-input {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    justify-items: center;
    gap: 5px;
    margin-bottom: 20px;
    input {
      text-align: center;
      width: 50px;
      height: 30px;
      font-size: 22px;
      color: #000;
      border-bottom: 2px solid #B71C1C;
    }
  }
  .email-error {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 20px;
    color: #FF346C;
  }
  &-button {
    button {
      width: 100%;
      background: #FF6F95;
      border-radius: 8px;
      padding: 10px;
      color: #fff;
      margin-bottom: 15px;
    }
    button:nth-child(2) {
      background: none;
      color: cornflowerblue;
      text-decoration: underline;
    }
  }
}

</style>
