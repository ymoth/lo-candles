<template>
  <div>
    <EmailConfirmation />
  </div>
</template>

<script>
import EmailConfirmation from "~/components/EmailConfirmation.vue";
export default {
  name: "verificationEmail",
  layout: 'verify-email',
  middleware: 'emailConfirm',
  components: {
    EmailConfirmation
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
