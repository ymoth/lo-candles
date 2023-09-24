<template>
  <footer class="footer">
    <hr>
    <div class="container">
      <div class="footer__top">
        <div class="col-2">
          <nuxt-link to="/">
            <img src="/header/logo.png" alt="" />
          </nuxt-link>
        </div>
        <div class="col-4">
          <p>Карта сайта</p>
        </div>
        <div class="col-3">
          <p>Адрес</p>
        </div>
      </div>
      <div class="footer__bottom">
        <div class="row">
          <div class="col-2">
            <div class="footer__bottom-social">
              <a href="https://www.instagram.com/aromatic_svechi">
                <img src="/footer/insta.svg" alt="">
              </a>
              <a href="https://t.me/+77787747039">
                <img src="/footer/telegram.svg" alt="">
              </a>
              <a href="https://wa.me/+77787747039">
                <img src="/footer/whatsapp.svg" alt="">
              </a>
            </div>
          </div>
          <div class="col-3">
            <nav class="footer__bottom-nav">
              <ul>
                <li><nuxt-link to="/" exact-active-class="active-link">Главная</nuxt-link></li>
                <li><nuxt-link to="/about" exact-active-class="active-link">О компании</nuxt-link></li>
                <li><nuxt-link to="/catalog" exact-active-class="active-link">Каталог</nuxt-link></li>
              </ul>
            </nav>
          </div>
          <div class="col-3">
            <div class="footer__bottom-communication">
              <div class="footer__bottom-communication-phone">
                <img src="/footer/phone.svg" alt="" />
                <span>+7 (705) 210 72 09</span>
              </div>
              <div class="footer__bottom-communication-address">
                <img src="/footer/address.svg" alt="" />
                <span>г.Алматы, ул. Рихарда Зорге 18/1 (ТРЦ Mart Village) магазин “Микс Прайс”</span>
              </div>
            </div>
          </div>
          <div class="col-lg-4">
            <div class="footer__bottom-map">
              <yandex-map :coords="coords" zoom="18">
                <ymap-marker :coords="coords" :markerType="'placemark'"  :markerId="'unique-marker-id'"></ymap-marker>
              </yandex-map>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="footer__top">
        <div class="row">
          <div class="col-6">
            <nuxt-link to="/">
              <img src="/header/logo.png" alt="" />
            </nuxt-link>
          </div>
          <div class="col-6">
            <div class="footer__top-social">
              <a href="https://www.instagram.com/aromatic_svechi">
              <img src="/footer/insta.svg" alt="">
              </a>
              <a href="https://t.me/+77787747039">
                <img src="/footer/telegram.svg" alt="">
              </a>
              <a href="https://wa.me/+77787747039">
                <img src="/footer/whatsapp.svg" alt="">
              </a>
            </div>
          </div>
        </div>
      </div>
      <div class="footer__bottom">
        <div class="row">
          <div class="col-6">
            <nav class="footer__bottom-nav">
              <p>
                Карта сайта
              </p>
              <ul>
                <li><nuxt-link to="/">Главная</nuxt-link></li>
                <li><nuxt-link to="/about">О компании</nuxt-link></li>
                <li><nuxt-link to="/catalog">Каталог</nuxt-link></li>
              </ul>
            </nav>
          </div>
          <div class="col-6">
            <div class="footer__bottom-communication">
              <p>Адрес</p>
              <div class="footer__bottom-communication-phone">
                <img src="/footer/phone.svg" alt="" />
                <span>+7 (705) 210 72 09</span>
              </div>
              <div class="footer__bottom-communication-address">
                <img src="/footer/address.svg" alt="" />
                <span>г.Алматы, ул. Рихарда Зорге 18/1 (ТРЦ Mart Village) магазин “Микс Прайс”</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-map">
        <yandex-map :coords="coords" zoom="12">
          <ymap-marker :coords="coords" :markerType="'placemark'"  :markerId="'unique-marker-id'"></ymap-marker>
        </yandex-map>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "CustomFooter",
  data() {
    return {
      coords: [43.337076, 76.955392], // Координаты центра карты
    };
  },
}
</script>

<style lang="scss">
.footer {
  background: linear-gradient(0deg, #A6A6A6 -4.11%, rgba(255, 255, 255, 0.00) 10.35%);
  padding: 15px 0 44px 0;
  .container:nth-child(3) {
    display: none;
  }
  &__top {
    display: flex;
    align-items: center;
    margin-bottom: 70px;
    p {
      margin-bottom: 0;
      font-size: 20px;
      text-transform: uppercase;
      font-weight: 700;
    }
  }
  &__bottom {
    &-social {
      display: flex;
      flex-direction: column;
      img {
        width: 40px;
        margin-bottom: 50px;
      }
    }
    &-nav {
      ul {
        padding-left: 0;
        li {
          a {
            font-size: 20px;
            text-decoration: none;
          }
        }
      }
    }
    &-nav ul li a::before {
      content: "";
      position: absolute;
      bottom: 0;
      left: 0;
      width: 0;
      height: 2px;
      background-color: #FF6F95;
      transition: width 0.3s ease;
    }

    &-nav ul li a:hover::before {
      width: 100%;
    }
    &-nav ul li a {
      font-size: 24px;
      font-weight: 600;
      text-decoration: none;
      color: #000;
      position: relative;
      transition: color 0.2s ease;
    }

    &-nav ul li a:hover {
      color: #FF6F95;
    }
    &-communication {
      div {
        display: flex;
        align-items: center;
        column-gap: 20px;
        margin-bottom: 20px;
        img {
          width: 25px;
        }
      }
    }
    .ymap-container {
      height: 100%;
    }
  }
  &__bottom-map {
    max-width: 696px;
    width: 100%;
    height: 305px;

    .yandex-map {
      height: 100%;

      .yandex-map-645596 {
        height: 100%;
      }
    }
  }
}
@media(max-width: 1023px) {
  .footer {
    &__bottom {
      &-communication {
        div {
          column-gap: 10px;
          margin-bottom: 1em;
          img {
            width: 20px;
          }
        }
      }
    }
  }
}
@media(max-width: 767px) {

  .footer {
    .container:nth-child(2) {
      display: none;
    }
    .container:nth-child(3) {
      display: block;
    }
    &__top {
      margin-bottom: 30px;
      .row {
        align-items: center;
      }
      &-social {
        display: flex;
        column-gap: 30px;
        a {
          img {
            width: 35px;
          }
        }
      }

    }
    &__bottom {
      &-nav {
        p {
          font-size: 24px;
        }
      }
      &-communication {
        p {
          font-size: 24px;
        }
      }
    }
    &-map {
      max-width: 696px;
      width: 100%;
      height: 305px;
      .ymap-container {
        height: 100%;
      }
      .yandexMap21961 {
        .ymaps-2-1-79-map {
          height: 100%;
        }
      }

    }
  }
}
</style>
