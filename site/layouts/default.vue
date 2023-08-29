<template>
  <div>
    <customHeader />
    <main>
      <Nuxt />
    </main>
  </div>
</template>

<script>
import customHeader from "~/components/CustomHeader";
export default {
  name: "default",
  components: {customHeader}
}
</script>

<style scoped>

</style>
