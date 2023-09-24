<template>
  <header>
    <div class="container">
      <div class="header">
        <div class="row">
          <div class="col-lg-1">
            <div class="header__logo">
              <nuxt-link to="/">
                <img src="/header/logo.png" alt="" />
              </nuxt-link>
            </div>
          </div>
          <div class="col-lg-7">
            <div class="header__nav">
              <ul>
                <li><nuxt-link to="/" exact-active-class="active-link">Главная</nuxt-link></li>
                <li><nuxt-link to="/about" exact-active-class="active-link">О компании</nuxt-link></li>
                <li><nuxt-link to="/catalog" exact-active-class="active-link">Каталог</nuxt-link></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="header__nav">
              <button class="header__nav-login" v-show="this.$auth.user">
                <nuxt-link to="/personalCabinet/makingOrder">
                  Оформить заказ
                  <img src="/cabinet/delivery.svg" alt="" />
                </nuxt-link>
              </button>
              <button class="header__nav-login" v-if="this.$auth.user">
                <nuxt-link to="/personalCabinet">
                  {{ capitalizedFirstName }}
                  <img src="/header/login.svg" alt="" />
                </nuxt-link>
              </button>
              <button class="header__nav-login" v-else @click="openLogin = !openLogin">
                Вход
                <img src="/header/login.svg" alt="" />
              </button>
            </div>
          </div>
        </div>
      </div>
      <div class="header__burger" :class="{ open: openMenu }">
        <div class="row">
          <div class="col-10">
            <div class="header__burger-logo">
              <nuxt-link to="/">
                <img src="/header/logo.png" alt="" />
              </nuxt-link>
            </div>
          </div>

          <div class="col-2">
            <div class="header__burger-menu" :class="{ open: openMenu }">
              <div class="header__burger-menu-icon" @click="openMenu = !openMenu">
                <span :class="{ open: openMenu }"></span>
                <span :class="{ open: openMenu }"></span>
                <span :class="{ open: openMenu }"></span>
              </div>
            </div>
          </div>
          <ul class="header__burger-menu-items" :class="{ open: openMenu }">
            <li @click="openMenu = false">
              <nuxt-link to="/about" >О компании</nuxt-link>
            </li>
            <li @click="openMenu = false">
              <nuxt-link to="/catalog">Каталог</nuxt-link>
            </li>
          </ul>
        </div>
        <div class="row">
          <div class="col-12">
            <div class="header__nav">
              <button class="header__nav-login" v-show="this.$auth.user">
                <nuxt-link to="/personalCabinet/makingOrder">
                  Оформить заказ
                  <img src="/cabinet/delivery.svg" alt="" />
                </nuxt-link>
              </button>
              <button class="header__nav-login" v-if="this.$auth.user">
                <nuxt-link to="/personalCabinet">
                  {{ capitalizedFirstName }}
                  <img src="/header/login.svg" alt="" />
                </nuxt-link>
              </button>
              <button class="header__nav-login" v-else @click="openLogin = !openLogin">
                Вход
                <img src="/header/login.svg" alt="" />
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Login
      v-if="openLogin === true"
      :open-login="openLogin"
      :open-register="openRegister"
      @closeLoginPopup="controlPopup"
      @openRegisterPopup="controlPopup"
      @notificationLogin="notificationLogin"
    />
    <Register
      v-if="openRegister === true"
      :open-register="openRegister"
      @closeRegisterPopup="controlPopup"
      @openLoginPopup="controlPopup"
      @openConfirmPopup="controlPopup"
    />
    <notifications :messages="messages" />
  </header>
</template>

<script>
import Login from "~/components/Login";
import Register from "~/components/Register";
import notifications from "~/components/Notifications";
export default {
  name: "CustomHeader",
  data() {
    return {
      openMenu: false,
      openLogin: false,
      openRegister: false,
      messages: []
    }
  },
  components: {
    Login, Register, notifications
  },
  methods: {
    controlPopup(data) {
      if(data.popup === 'login') {
        this.openLogin = data.status
        this.openRegister = false
      } else {
        this.openLogin = false
        this.openRegister = data.status
      }
    },
    notificationLogin(data) {
      if(data === 'register') {
        this.messages.unshift({
          text: 'Вы успешно зарегистрировались и вошли в аккаунт',
          status: 'check',
          icon: 'checkMark.svg',
          id: Date.now().toLocaleString()
        })
      } else {
        this.messages.unshift({
          text: 'Вы успешно вошли',
          status: 'check',
          icon: 'checkMark.svg',
          id: Date.now().toLocaleString()
        })
      }
    },
  },
  computed: {
    capitalizedFirstName() {
      const firstName = this.$auth.user.first_name;
      return firstName.charAt(0).toUpperCase() + firstName.slice(1);
    }
  },
  watch: {
    openMenu: function(newValue) {
      if (newValue) {
        document.body.classList.add('no-scroll');
      } else {
        document.body.classList.remove('no-scroll');
      }
    },
  },
}
</script>

<style lang="scss">
header {
  box-shadow: 0px 1px 0px rgba(0, 0, 0, 0.1);
}
.header {
  margin: 15px 0;
  .col-lg-7 {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .col-lg-4 {
    display: flex;
    align-items: center;
    justify-content: flex-end;
  }
  .header__nav {
    display: flex;
    column-gap: 60px;
    ul {
      position: relative;
      column-gap: 30px;
      display: flex;
      margin-bottom: 0;
      li {
        position: relative;
        a {
          position: relative;
          font-size: 24px;
          font-weight: 600;
          text-decoration: none;
        }
      }
    }
    button {
      font-size: 22px;
      font-weight: 500;
      text-decoration: none;
      a {
        text-decoration: none;
      }
    }
  }
  .header__nav ul li a::before {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background-color: #FF6F95;
    transition: width 0.3s ease; /* Анимация */
  }

  .header__nav ul li a:hover::before {
    width: 100%;
  }
  .header__nav ul li a {
    font-size: 24px;
    font-weight: 600;
    text-decoration: none;
    color: #000;
    position: relative;
    transition: color 0.2s ease;
  }

  .header__nav ul li a:hover {
    color: #FF6F95;
  }
  .header__logo {
    display: flex;
    justify-content: center;
    margin-bottom: 15px;
  }
}
.header__burger {
  display: none;
}
@media(max-width: 990px) {
  .header {
    display: none;
  }
  .header__burger {
    padding: 10px 0 10px 0;
    display: block;
    &-logo {
      position: relative;
      z-index: 4;
    }
    &-menu {
      display: flex;
      justify-content: center;
      position: relative;
      &-icon {
        width: 20px;
        height: 15px;
        position: relative;
        z-index: 4;
        top: 35px;
        span {
          width: 100%;
          position: absolute;
          height: 2px;
          background: #FF6F95;
          &:nth-child(1) {
            top: 0;
          }
          &:nth-child(2) {
            top: 6px;
          }
          &:nth-child(3) {
            bottom: 0;
          }
        }
        span {
          transition: transform 0.3s ease-in-out, opacity 0.3s ease-in-out;
          &.open {
            &:nth-child(1) {
              transform: rotate(45deg);
              top: 3px;
            }
            &:nth-child(2) {
              opacity: 0;
            }
            &:nth-child(3) {
              transform: rotate(-45deg);
              top: 3px;
            }
          }
        }
      }
      ul {
        padding-left: 0;
      }
      &-items {
        display: none;
        background: #fff;
      }
    }
    &-menu.open {
      display: flex;
      z-index: 3;
      .header__burger-menu-icon {
        right: 0;
        top: 35px;
      }
    }
  }
  .col-7 {
    display: flex;
    justify-content: flex-end;
  }
  .header__nav {
    position: relative;
    z-index: 4;
    display: flex;
    justify-content: space-between;
    margin-top: 25px;
    &-login {
      display: flex;
      align-items: center;
      column-gap: 5px;
      a {
        text-decoration: none;
      }
    }
  }
  .header__burger.open {
    z-index: 10;
    .header__burger:before {
      overflow: hidden;
    }
    &:before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 132%;
      background: #fff;
      z-index: 3;
    }
  }
  .header__burger-menu-items.open {
    display: flex;
    flex-direction: column;
    align-items: center;
    background: #fff;
    z-index: 3;
    padding: 30px;
    li {
      font-size: 28px;
      a {
        text-decoration: none;
        color: #FF6F95;
      }
    }
  }
}


.no-scroll {
  overflow: hidden;
}
</style>
