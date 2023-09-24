<template>
  <div class="notifications">
    <transition-group
      name="notification-animate"
      class="messages__list"
      tag="div"
    >
      <div
        class="notifications__content"
        v-for="message in messages"
        :key="message.id"
        :class="message.status"
      >
        <div class="notifications__content-text">
          <span>{{message.text}}</span>
          <img :src="`/notifications/${message.icon}`" alt="">
        </div>
      </div>
    </transition-group>
  </div>
</template>

<script>
export default {
  name: "Notifications",
  props: {
    messages: {
      type: Array,
      default: () => []
    },
    timeout: {
      type: Number,
      default: () => 3000
    },
  },
  methods: {
    hideNotifications() {
      let vm = this;
      if(this.messages.length) {
        setTimeout(() => {
          vm.messages.splice(vm.messages.length - 1, 1)
        }, vm.timeout)
      }

    }
  },
  watch: {
    messages:{
      handler(){
        this.hideNotifications()
      },
      deep: true
    }
  },
  mounted() {
    this.hideNotifications()
  },
}
</script>

<style lang="scss">
.notifications {
  position: fixed;
  top: 80px;
  right: 15px;
  z-index: 20;
  display: flex;
  flex-direction: column-reverse;
  .messages__list {
    display: flex;
    flex-direction: column-reverse;
  }
  &__content {
    padding: 16px 30px;
    border-radius: 4px;
    color: #fff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 50px;
    margin-bottom: 16px;
    &-text {
      display: flex;
      align-items: center;
      column-gap: 10px;
      img {
        filter: invert(100%) sepia(3%) saturate(7497%) hue-rotate(120deg) brightness(112%) contrast(110%);
      }
    }
    &.check {
      background: green;
    }
    &.error {
      background: red;
    }
    &.warning {
      background: orange;
    }
  }
  .notification-animate-enter {
    transform: translateX(120px);
    opacity: 0;
  }
  .notification-animate-enter-active {
    transition: all .6s ease;
  }
  .notification-animate-enter-to {
    opacity: 1;
  }
  .notification-animate-leave {
    height: 50px;
    opacity: 1;
  }
  .notification-animate-leave-active {
    transition: translate .6s ease, opacity .6s, height .6s .2s;
  }
  .notification-animate-leave-to {
    height: 0;
    transform: translateX(0px);
    opacity: 0;
  }
  .notification-animate-move {
    transition: transform .6s;
  }
}
</style>
