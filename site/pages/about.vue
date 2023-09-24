<template>
  <div>
    <main>
      <About />
    </main>
  </div>
</template>

<script>
import About from "~/components/About";
export default {
  name: "about",
  components: {
    About
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

<style scoped>

</style>
