app.component('restaurante-card', {
  props:{
    background_image:{
      type: String,
      required: true
    },
    restaurante_id:{
      type: Number,
      required:true
    },
    preco_entrega:{
      type: String,
      required:true,
      coerce(val) {
        return Number(val)
      }
    },
    logo_image:{
      type:String,
      required: true
    },
    descricao:{
      type: String,
      required: true
    },
    nome:{
      type: String,
      required: true
    },
    pontuacao:{
      type: String,
      required: true
    },
    telefone:{
      type: String,
      required: true
    }
  },
    template:
    /*html*/
    `
    <div class="card mt-3" style="width: 23rem;">
      <img :src="background_image" class="card-img-top" :alt="nome">
      <div class="card-body row">
        <img :src="logo_image" style="object-fit: contain;" class="col-3 rounded-circle " :alt="nome">
        <div class="col-9">
          <h5 class="card-title">{{ nome }}</h5>
          <p class="card-text fs-6">
            {{ descricao }} <i style="color:yellow; font-size:1.2em;" class="bi bi-star-fill"></i> {{ pontuacao }} 
            <div  v-if="preco_entrega > 10">
              <i style="color:red; font-size:1.2em;" class="bi bi-truck"></i> R$ {{ preco_entrega.replace(".", ",") }}  
            </div>
            <div  v-else-if="preco_entrega > 0">
              <i style="color:orange; font-size:1.2em;" class="bi bi-truck"></i> R$ {{ preco_entrega.replace(".", ",") }}  
            </div>
            <div  v-else >
            <i style="color:green; font-size:1.2em;" class="bi bi-truck"></i> Gratis
            </div>
          </p>
        </div>
      </div>
      <div class="card-footer">
        <router-link :to="'/restaurante/'+restaurante_id" >Ver cardapio</router-link>
        <a :href="'tel:'+telefone" class="card-link">Ligar</a>
      </div>
    </div>
    `,

})