<template>
  <div>
    <h1>LifeGame</h1>
    <table class="center">
      <tr v-for="linha in grid" :key="linha">
        <td v-for="celula in linha" :key="celula"></td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'LifeGame',
  data() {
    return{
      grid: [
        [0.0,0,0,0,0,0,0,0,0],
        [0.0,0,0,0,0,0,0,0,0],
        [0.0,0,0,0,0,0,0,0,0],
        [0.0,0,0,0,0,0,0,0,0],
        [0.0,0,0,0,0,0,0,0,0],
        [0.0,0,0,0,0,0,0,0,0],
        [0.0,0,0,0,0,0,0,0,0],
        [0.0,0,0,0,0,0,0,0,0],
        [0.0,0,0,0,0,0,0,0,0],
        [0.0,0,0,0,0,0,0,0,0],]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
table, th, td {
  border: 1px solid black;
}
td{
  width: 30px;
  height: 30px;
}

.vivo{
  background-color: blue;
}
</style>
