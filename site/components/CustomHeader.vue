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
                <li>
                  <nuxt-link to="/">О компании</nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/">Отзывы</nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/">Каталог</nuxt-link>
                </li>
                <li>
                  <nuxt-link to="/">Контакты</nuxt-link>
                </li>
              </ul>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="header__nav">
              <button class="header__nav-cart" v-show="this.$auth.user">
                Корзина
                <img src="/header/cart.svg" alt="" />
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
          <div class="col-3">
            <div class="header__burger-logo">
              <img src="/header/logo.png" alt="" />
            </div>
          </div>
          <div class="col-7">
            <div class="header__nav">
              <button class="header__nav-cart">
                Корзина
                <img src="/header/cart.svg" alt="" />
              </button>
              <button class="header__nav-login" @click="openLogin = !openLogin">
                Вход
                <img src="/header/login.svg" alt="" />
              </button>
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
            <li>
              <nuxt-link to="/">О компании</nuxt-link>
            </li>
            <li>
              <nuxt-link to="/">Отзывы</nuxt-link>
            </li>
            <li>
              <nuxt-link to="/">Каталог</nuxt-link>
            </li>
            <li>
              <nuxt-link to="/">Контакты</nuxt-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <Login
      v-if="openLogin === true"
      :open-login="openLogin"
      :open-register="openRegister"
      @closeLoginPopup="controlPopup"
      @openRegisterPopup="controlPopup"
    />
    <Register
      v-if="openRegister === true"
      :open-register="openRegister"
      @closeRegisterPopup="controlPopup"
      @openLoginPopup="controlPopup"
    />
  </header>
</template>

<script>
import Login from "~/components/Login";
import Register from "~/components/Register";
export default {
  name: "CustomHeader",
  data() {
    return {
      openMenu: false,
      openLogin: false,
      openRegister: false,
    }
  },
  components: {
    Login, Register
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
.header {
  margin: 15px 0;
  .col-lg-7, .col-lg-4 {
    display: flex;
    align-items: center;
    justify-content: flex-end;
  }
  .header__nav {
    display: flex;
    column-gap: 60px;
    ul {
      column-gap: 30px;
      display: flex;
      margin-bottom: 0;
      li {
        a {
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
  .header__logo {
    display: flex;
    justify-content: center;
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
  .header__nav {
    position: relative;
    z-index: 4;
    display: flex;
    justify-content: space-between;
    margin-top: 25px;
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
      height: 100%;
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
