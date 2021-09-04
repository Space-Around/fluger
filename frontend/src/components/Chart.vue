<template>
  <div>
    <apexchart type="line" :options="options" :series="series"></apexchart>
  </div>
</template>

<script>
  import vueHighcharts from 'highcharts-vue'

  export default {
    props: ['x-axis', 'y-axis'],
    data() {
      return {
        
      }
    },
    computed: {
      options() {
        return {
          chart: {
            id: 'company information'
          },
          xaxis: {
            categories: this.xAxis
          }
        }
      },
      series() {
        return [{
          name: 'Цена',
          data: this.yAxis
        }]
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>