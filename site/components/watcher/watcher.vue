<template>
  <div class="clock-icon">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="100"
      height="100"
      viewBox="0 0 100 100"
    >
      <circle cx="50" cy="50" r="20" fill="none" stroke="#FFFFFF" stroke-width="2" />
      <line ref="hourArrow" :class="'rotate-animation ' + arrowClass" x1="50" y1="50" x2="50" y2="70" stroke="#FFFFFF" stroke-width="2" />
      <line ref="minuteArrow" :class="'rotate-animation ' + arrowClass" x1="50" y1="50" x2="50" y2="60" stroke="#FFFFFF" stroke-width="2" />
    </svg>
  </div>
</template>

<script>
let hourIntervalId;
let minuteIntervalId;

export default {
  name: "watcher",
  props: {
    arrowClass: String
  },
  mounted() {
    const hourArrow = this.$refs.hourArrow;
    const minuteArrow = this.$refs.minuteArrow;

    let hourAngle = 0;
    let minuteAngle = 0;

    hourIntervalId = setInterval(() => {
      hourAngle += 10;
      hourArrow.style.transform = `rotate(${hourAngle}deg)`;
    }, 100);

    minuteIntervalId = setInterval(() => {
      minuteAngle += 2;
      minuteArrow.style.transform = `rotate(${minuteAngle}deg)`;
    }, 100);
  },
  watch: {
    arrowClass: {
      immediate: true,
      handler(newValue, oldValue) {
        if (newValue !== oldValue) {
          this.stopRotation();
          this.startRotation();
        }
      }
    }
  },
  methods: {
    startRotation() {
      // Здесь можно оставить только watch, если он вам нужен
    },
    stopRotation() {
      clearInterval(hourIntervalId);
      clearInterval(minuteIntervalId);
    }
  },
  beforeDestroy() {
    this.stopRotation();
  },
};
</script>

<style scoped>
.rotate-animation {
  transform-origin: center center;
}
</style>
