<template>
  <section class="cabinet">
    <div class="container">
      <UserData />
      <myHistoryOrder />
    </div>
  </section>
</template>

<script>
import UserData from "~/components/UserData";
import myHistoryOrder from "~/components/myHistoryOrder.vue";
export default {
  name: "PersonalCabinet",
  middleware: 'personalCabinet',
  components: {
    UserData, myHistoryOrder
  },
  methods: {
    scrollToTop() {
      if (process.client) {
        window.scrollTo(0, 0);
      }
    }
  },
  mounted() {
    this.scrollToTop();
  }
}
</script>

<style lang="scss">
.cabinet {
  padding: 50px 0;
  background: url("/about/bg.png") no-repeat;
  background-size: cover;
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
}
</style>
