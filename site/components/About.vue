<template>
  <section class="about">
    <div class="container">
      <div class="about-title">
        <h1>О компании</h1>
      </div>
      <div class="row">
        <div class="col-lg-8">
          <div class="about-text">
            <img src="/confirm/AromaticCandles.png" alt="" />
            <p>Наша команда делает свечи на заказ, также вы можете посмотреть ассортимент заказов, которые вы можете увидеть в нашем каталоге.
              Более 10.000тыс успешных заказов и новых интересных свечей.
              Также у нас есть магазин, где вы можете посмотреть не большой ассортимент товаров,
              по улице ул. Рихарда Зорге 18/1 (ТРЦ Mart Village) магазин “Микс Прайс”.
            </p>
            <p>
              Все свечи похожи друг на друга — они могут слегка отличаться внешним
              видом, но в конце концов это всегда свеча. Одна из причин такой схожести
              — то, что представители наиболее насыщенной части рынка пользуются услугами
              одних и тех же поставщиков, и в итоге их продукт схож не только внешне, но и
              имеет практически идентичную линейку ароматов. У нас же иначе, у нас разные свечи
              на ваш вкус, при заказе вы можете оставить комментарий к заказу
            </p>
          </div>
        </div>
        <div class="col-lg-4">
          <div class="about-logo">
            <img src="/about/logo.png" alt="" />
          </div>
        </div>
      </div>
      <div class="row">
        <div
          class="col-lg-4"
          v-for="item in advantages"
          :key="item.id"
        >
          <div class="about__advantages-item">
            <div class="about__advantages-item-img">
              <img :src="item.img" alt="" />
              <hr>
            </div>
            <div class="about__advantages-item-title">
              <h2>{{ item.title }}</h2>
            </div>
            <div class="about__advantages-item-subtitle">
              <p>{{ item.subtitle }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "About",
  data() {
    return {
      advantages: [
        {
          id: 1,
          img: "/about/lamp.svg",
          title: "Уникальность",
          subtitle: "Мы являемся одним из лучших изделием свечей для перемещения на рынке. Удобный дизайн и большой ассортимент дает нам право заявить о своей уникальности.",
        },
        {
          id: 2,
          img: "/about/client.svg",
          title: "Довольный клиент",
          subtitle: "Более 10.000 довольных клиентов за выполненную работу, сделанную профессиональными навыками нашей команды.",
        },
        {
          id: 3,
          img: "/about/price.svg",
          title: "Цена",
          subtitle: "Низкая цена – неотъемлемая часть хорошего продукта.",
        },
      ]
    }
  },
}
</script>

<style lang="scss">
.about {
  background: url("/about/bg.png") no-repeat;
  background-size: cover;
  padding: 25px 0 25px 0;
  position: relative;
  z-index: 1;
  &::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    z-index: -1;
    width: 100%;
    height: 100%;
    background: linear-gradient(59deg, rgb(0 0 0 / 55%) 22.47%, rgb(112 65 211 / 31%) 100%);
  }
  &-title {
    h1 {
      color: #FFF;
      font-size: 36px;
      font-weight: 600;
    }
    margin-bottom: 50px;
  }
  &-text {
    img {
      filter: brightness(0) saturate(100%) invert(100%) sepia(100%) saturate(38%) hue-rotate(321deg) brightness(110%) contrast(110%);
      margin-bottom: 20px;
    }
    p {
      color: #FFF;
      font-size: 24px;
      font-weight: 400;
      max-width: 680px;
    }
  }
  &__advantages-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    &-img {
      img {
        filter: brightness(0) saturate(100%) invert(100%) sepia(100%) saturate(38%) hue-rotate(321deg) brightness(110%) contrast(110%);
      }
      hr {
        color: #FF346C;
      }
    }
    &-title {
      h2 {
        color: #FFF;
        font-size: 32px;
        font-weight: 400;
      }
    }
    &-subtitle {
      p {
        color: #FFF;
        font-size: 24px;
        font-weight: 400;
      }
      width: 300px;
    }
  }
}
@media (max-width: 1023px) {
  .about {
    &-title {
      margin-bottom: 5px;
    }
    &-logo {
      img {
        width: 285px;
      }
    }
    .row {
      flex-direction: column-reverse;
    }
  }
}
</style>
