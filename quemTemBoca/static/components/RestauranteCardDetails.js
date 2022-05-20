app.component('restaurante-card-details', {
  props:{
    restaurante:{
      required: true
    },
  },
    template:
    /*html*/
    `
    <div class="container mt-3">
      <div class="card mb-3">
      <img :src="restaurante.background_url" style="max-height: 400px;object-fit: cover;" class="card-img-top" :alt="restaurante.nome">
      <div class="card-body row">
        <img :src="restaurante.logo_url" style="object-fit: contain;" class="col-3 rounded-circle col-md-1" :alt="nome">
        <div class="col-9">
        <h5 class="card-title">{{ restaurante.nome }} <i style="color:yellow; font-size:1.2em;" class="bi bi-star-fill"></i> {{ restaurante.pontuacao }} 
        </h5>
        <p class="card-text">{{ restaurante.descricao }} <div  v-if="preco_entrega > 10">
        <i style="color:red; font-size:1.2em;" class="bi bi-truck"></i> R$ {{ preco_entrega.replace(".", ",") }}  
      </div>
      <div  v-else-if="preco_entrega > 0">
        <i style="color:orange; font-size:1.2em;" class="bi bi-truck"></i> R$ {{ preco_entrega.replace(".", ",") }}  
      </div>
      <div  v-else >
      <i style="color:green; font-size:1.2em;" class="bi bi-truck"></i> Gratis
      </div></p>
        <p class="card-text"><small class="text-muted">{{ restaurante.endereco }}</small></p>
        </div>
      </div>
      </div>
    </div>
    `,


})