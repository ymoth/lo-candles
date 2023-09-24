<template>
  <transition name="slide" mode="out-in">
    <slot></slot>
  </transition>
</template>

<script>
export default {
  name: "pageTransition"
}
</script>

<style scoped>
.slide-enter-active, .slide-leave-active {
  transition: transform 0.3s,  opacity 0.5s;
}

.slide-enter, .slide-leave-to {
  transform: translateX(100%);
  opacity: 0;
}
</style>
