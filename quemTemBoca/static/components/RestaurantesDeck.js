app.component('restaurante-deck', {
  props:{
    restaurantes:{
      type: Array,
      required: true
    },
  },
    template:
    /*html*/
    `
    <div class="container">
      <div class="row row-cols-1 row-cols-md-3 g-4">
        <div class="col" v-for="restaurante in restaurantes" :key="restaurante.id">
          <restaurante-card
            :background_image="restaurante.background_url"
            :restaurante_id="restaurante.id"
            :logo_image="restaurante.logo_url"
            :descricao="restaurante.descricao"
            :nome="restaurante.nome"
            :pontuacao="restaurante.pontuacao"
            :preco_entrega="restaurante.preco_entrega"
            :telefone="restaurante.telefone"
          ></restaurante-card>
        </div>
      </div>
    </div>
    `,


})