<template>
  <div>
    <Nuxt />
  </div>
</template>

<script>
export default {
  name: "verify-email",
  mounted() {
    this.$nextTick(() => {
      window.scrollTo(0, 0);
    });
  }
}
</script>
