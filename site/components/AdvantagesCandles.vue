<template>
  <section class="advantages__candles">
    <div class="container">
      <div class="row">
        <div class="advantages__candles-title">
          <h1>Ароматические свечи из пчелиного воска</h1>
        </div>
        <div class="advantages__candles-subtitle">
          <h2>Какова же польза от них?</h2>
        </div>
        <div
          class="col-lg-6"
          v-for="item in advantages"
          :key="item.id"
        >
          <div class="advantages__candles-item">
            <img :src="item.img" alt="" />
            <span>{{ item.text }}</span>
            <div></div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "AdvantagesCandles",
  data() {
    return {
      advantages: [
        {
          id: 1,
          text: "Уникальная атмосфера",
          img: "/advantagesCandles/star.svg",
        },
        {
          id: 2,
          text: "Расслабляющая обстановка",
          img: "/advantagesCandles/lamp.svg",
        },
        {
          id: 3,
          text: "Хорошее настроение",
          img: "/advantagesCandles/Mask.svg",
        },
        {
          id: 4,
          text: "Обеспечение комфортного сна",
          img: "/advantagesCandles/sleep.svg",
        },
        {
          id: 5,
          text: "Расслабляющая обстановка",
          img: "/advantagesCandles/smile.svg",
        },
        {
          id: 6,
          text: "Сохранение сосредоточенности",
          img: "/advantagesCandles/bulb.svg",
        },
      ]
    }
  },
}
</script>

<style lang="scss">
.advantages__candles {
  background: lightgray url("/advantagesCandles/bg.png") 50% / cover no-repeat;
  padding: 100px 0 38px 0;
  position: relative;
  &:after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: lightgray;
    opacity: 0.7;
    z-index: 1;
  }
  &-title {
    display: flex;
    justify-content: center;
    position: relative;
    z-index: 2;
    h1 {
      text-align: center;
      max-width: 370px;
      font-size: 36px;
      font-weight: 700;
    }
  }
  &-subtitle {
    display: flex;
    justify-content: center;
    margin-bottom: 110px;
    position: relative;
    z-index: 2;
    h2 {
      text-align: center;
      font-size: 36px;
      font-weight: 700;
    }
  }
  &-item {
    position: relative;
    z-index: 2;
    background: url("/advantagesCandles/bg-advantages.png");
    margin-bottom: 72px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 12px 10px;
    max-width: 500px;
    width: 100%;
    z-index: 2;
    border-radius: 8px;
    img {
      position: relative;
      z-index: 2;
      background: #fff;
      border-radius: 50px;
      padding: 15px;
    }
    span {
      position: relative;
      z-index: 2;
      color: #FFF;
      font-size: 26px;
      font-weight: 400;
    }
  }
  .col-lg-6:nth-child(odd) {
    .advantages__candles-item {
      img {
        position: absolute;
        left: -15px;
      }
    }
  }
  .col-lg-6:nth-child(even) {
    display: flex;
    justify-content: flex-end;
    .advantages__candles-item {
      padding: 12px 50px;
      padding-left: 0;
      img {
        position: absolute;
        right: -15px;
      }
    }
  }
}
</style>
