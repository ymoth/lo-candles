<template>
  <div class="accordion accordion-flush">

    <div class="accordion-item">
      <h2
        class="accordion-header"
        v-for="(acc_header_item, index) in acc_header"
        :key="acc_header_item.id"
      >
        <button
          class="accordion-button collapsed"
          type="button"
          @click="openAcc(index)"
          :class="{ [activeClass]: activeIndex === index }"
        >
          <img :src="acc_header_item.img" alt="">
          {{acc_header_item.text}}
        </button>
      </h2>
      <transition
        name="acc-animated"
        enter-active-class="acc-animated-enter-active"
        leave-active-class="acc-animated-leave-active"
        enter-class="acc-animated-enter"
        leave-to-class="acc-animated-leave-to"
        enter-from-class="acc-animated-enter-from"
        leave-from-class="acc-animated-leave-from"
      >
        <div
          class="accordion-collapse"
          v-for="(acc_body_item, index) in acc_body"
          :key="acc_body_item.id"
          :class="{ show: activeIndex === index }"
          v-show="activeIndex === index"
        >
          <button
            class="accordion-body"
            v-for="acc_body_item_btn in acc_body_item.btn"
            :key="acc_body_item_btn.id"
            @click="openTab(acc_body_item_btn.open_tab)"
          >
            <img :src="acc_body_item_btn.img" alt="">
            {{acc_body_item_btn.text}}
          </button>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  name: "Accordion",
  props: {
    acc_header: {
      type: Array,
      default: () => [],
    },
    acc_body: {
      type: Array,
      default: () => []
    },
  },
  data() {
    return {
      activeIndex: null,
      activeTab: null,
      activeClass: 'active',
    }
  },
  methods: {
    openAcc(index) {
      if(this.activeIndex === index) {
        this.activeIndex = null
      } else {
        this.activeIndex = index
      }
    },
    openTab(open_tab) {
      this.$emit('openTab', open_tab)
    }
  }
}
</script>

<style lang="scss">
.accordion {
  margin-bottom: 30px;
  &-button::after {
    filter: brightness(0) invert(1);

  }
  &-button:focus {
    border: none;
    box-shadow: none;
  }
  &-item {
    background: #fff;
    border: 1px solid #000;
    border-radius: 5px;

  }
  .accordion-button.active {
    &:after {
      transform: rotate(180deg);
    }
  }
  &-header {
    button {
      background: rgb(211,81,123, 1);
      display: flex;
      align-items: center;
      column-gap: 10px;
      color: #fff;
    }
    img {
      height: 35px;
      filter: brightness(0) invert(1);
    }
  }
  &-button {

  }
  &-collapse {
    background:rgb(211,81,123, 1);
  }
  &-body {
    position: relative;
    color: #fff;
    display: flex;
    column-gap: 10px;
    background:rgb(133,25,90, 1);
    width: 100%;
    img {
      filter: brightness(0) invert(1);
    }
    &:before {
      content: "";
      position: absolute;
      height: 100%;
      width: 4px;
      background: #b2cd88;
      top: 0;
      left: 0;
    }
  }
  .acc-animated-enter-active,
  .acc-animated-leave-active {
    transition: all .2s ease;
  }
  .acc-animated-enter,
  .acc-animated-leave-to {
    transform: translateY(-10px);
    opacity: 0;
  }

}

</style>
