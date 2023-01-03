<template>
  <div>
    <h1>LifeGame</h1>
    <table class="align-center">
      <tr v-for="linha, i in grid" :key="i">
        <td v-for="celula, j in linha" :key="j" :class="{vivo: celula==1}"></td>
      </tr>
    </table>
  </div>
</template>

<script>

function _countVizinhosVivos(i,j,grid){
  const [M, N] = [grid.length, grid[0].length]
  const delta_coord = [
    [-1,-1],[-1,0],[-1,1],
    [0,-1], [0, 1],
    [1, -1], [1, 0], [1,1]
  ]
  let coord_vizinhos = []
  // debugger
  for (let k = 0; k < delta_coord.length; k++){
    coord_vizinhos.push([i + delta_coord[k][0], j + delta_coord[k][1]])
  }
  let coord_vizinhos_vivos = coord_vizinhos.filter((e) => e[0] >= 0 && e[0] < M && e[1] >= 0 && e[1] < N && grid [e[0]][e[1]] == 1)
  return coord_vizinhos_vivos.length
}

function _nextState(grid){
  const [M, N] = [grid.length, grid[0].length]
    let newGrid = new Array(M)
    for (let i= 0; i < M; i++) {
      newGrid[i] = new Array(N).fill(0)
    }
    for (let i=0; i < M; i++){
      for (let j=0; j < N; j++){
        let vizinhos = _countVizinhosVivos(i,j,grid)
        if (grid[i][j] == 1){
          if (vizinhos == 2  || vizinhos == 3){
            newGrid[i][j] = 1
          }
          else{
            newGrid[i][j] = 0
          }
        }
        else{
          if (vizinhos == 3){
            newGrid[i][j]=1
          }
          else{
            newGrid[i][j]=0
          }
        }
        }
      }
      
    return newGrid
    }


export default {
  name: 'LifeGame',
  data() {
    return{
      grid: [
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,1,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,0,0],
      ]
    }
  },
  created(){

  },
  methods:{
    proximoPasso() {
    this.grid = _nextState(this.grid)
    }
  },
  mounted(){
    setInterval(() =>{
      this.proximoPasso()
    }, 1000)
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
