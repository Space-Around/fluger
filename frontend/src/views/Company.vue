<template>
  <div class="company">
    <chart/>
  </div>
</template>

<script>
import chart from "../components/Chart.vue"

export default {
  data() {
    return {
      activeCompany: {
        name: '',
        metaInfo: {},
        predictionsData: {
          2021: 617.0901875,
          2022: 656.3474277,
          2023: 695.60466789,
          2024: 734.86190809,
          2025: 774.11914828,
        }
      }
    }
  },
  components: {
    chart,
  }
}
</script>

<style lang="scss" scoped>

</style>