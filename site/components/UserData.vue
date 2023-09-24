<template>
  <aside class="user__data">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div class="user__data-title">
            <h2>Добро пожаловать в личный кабинет, </h2>
            <h2>{{ userData.first_name}} {{ userData.last_name }}</h2>
          </div>
          <div class="user__data__info">
            <p>Ваша почта: {{ userData.email }}</p>
            <p>Дата создания аккаунта: {{ userCreatedAtYear }} г.  {{userCreatedAtDay}} {{userCreatedAtMonth}}. </p>
          </div>
        </div>
        <div class="col-lg-3">
          <div class="user__data-logout">
            <button @click="logoutUser">
              <img src="/cabinet/logout.svg" alt="" />
              Выйти с аккаунта
            </button>
            <button class="button-admin-panel" v-if="userData.is_admin">
              <a href="https://dev.aromatic.kz/private/admin/">Перейти в админ панель</a>
            </button>
          </div>
        </div>
      </div>
    </div>
  </aside>

</template>

<script>
export default {
  name: "UserData",
  auth: false,
  data() {
    return {
      months: [
        "Января", "Февраля", "Марта", "Апреля", "Мая", "Июня",
        "Июля", "Августа", "Сентября", "Октября", "Ноября", "Декабря"
      ],
    }
  },
  methods: {
    async logoutUser() {
      await this.$auth.logout()
    }
  },
  computed: {
    userData() {
      return this.$auth.user
    },
    userCreatedAtYear() {
      const yearDate = new Date(this.userData.created_at)
      return yearDate.getFullYear()
    },
    userCreatedAtMonth() {
      const yearDate = new Date(this.userData.created_at)
      const monthName = this.months[yearDate.getMonth()];
      return monthName
    },
    userCreatedAtDay() {
      const yearDate = new Date(this.userData.created_at)
      return yearDate.getDate()
    }
  }
}
</script>

<style lang="scss">
.user__data {
  margin-bottom: 60px;
  &-title {
    margin-bottom: 30px;
    h2 {
      color: #fff;
      font-size: 36px;
      font-weight: 500;
    }
  }
  &__info {
    p {
      color: #fff;
      font-size: 18px;
      font-weight: 400;
    }
  }
  &-logout {
    button {
      padding: 10px 30px;
      background: #B71C1C;
      color: #fff;
      border-radius: 8px;
      margin-bottom: 1em;
      img {
        filter: brightness(0) invert(1);
      }
    }
  }
  .button-admin-panel {
    background: #5252f3;
    a {
      color: #fff;
      text-decoration: none;
    }
  }
}
@media (max-width: 520px) {
  .user__data {
    &__info-text {
      display: block;
      p {
        margin-bottom: 1em;
      }
    }
  }
}
</style>
