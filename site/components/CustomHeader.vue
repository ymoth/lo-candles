<template>
  <header>
    <div class="container">
      <div class="row">
        <div class="col-lg-5">
          <div class="header__nav">
            <ul>
              <li>
                <nuxt-link to="/">О компании</nuxt-link>
              </li>
              <li>
                <nuxt-link to="/">Отзывы</nuxt-link>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-lg-2">
          <div class="header__logo">
            <img src="/header/logo.png" alt="" />
          </div>
        </div>
        <div class="col-lg-5">
          <div class="header__nav">
            <ul class="header__nav-r">
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
    </div>
  </header>
</template>

<script>
export default {
  name: "CustomHeader",
}
</script>

<style lang="scss">
header {
  margin-top: 15px;
  .header__nav {
    margin-top: 31px;
    ul {
      display: flex;
      column-gap: 60px;
      li {
        a {
          font-size: 24px;
          font-weight: 600;
          text-decoration: none;
        }
      }
    }
    &-r {
      display: flex;
      justify-content: flex-end;
    }
  }
  .header__logo {
    display: flex;
    justify-content: center;
  }
}
</style>
