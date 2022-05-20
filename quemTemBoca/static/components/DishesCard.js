app.component('dishes-card', {
  props:{
    pratos:{
      required: true
    },
  },
    template:
    /*html*/
    `
    <div class="container ">
      <div class="row row-cols-md-3">
      <div v-for="prato in pratos" :key="prato.id" class="col">
          <div  class="card mb-3 ms-1" style="max-width: 540px;">
        <div class="row g-0">
          <div class="col-md-5">
            <img :src="prato.img_url" class="img-fluid rounded-start" :alt="prato.nome">
          </div>
          <div class="col-md-7">
            <div class="card-body">
              <h5 class="card-title">{{ prato.nome }}</h5>
              <p class="card-text">{{ prato.descricao }}</p>
              <p class="card-text"><small class="text-muted">RS {{ prato.preco.replace('.',',') }}</small></p>
            </div>
        </div>
        </div>
      </div>
    </div>
    </div>
    </div>
    `,

})