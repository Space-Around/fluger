<template>
  <div class="fade">
    <slot></slot>
  </div>
</template>

<script>
  export default {
    
  }
</script>

<style lang="scss" scoped>
.fade-enter, .fade-leave-to {
  opacity: 0;
}
.fade {
  transition: opacity 0.2s;
}
</style>