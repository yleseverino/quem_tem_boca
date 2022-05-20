app.component('header-bar',{
    template:
    /*html*/
    `<header class="p-3 bg-dark text-white">
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <router-link to="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
        <h1 class="h3 me-2"> Quem Tem Fome</h1>
          <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" fill="currentColor" class="bi bi-egg-fried" viewBox="0 0 16 16">
            <path d="M8 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
            <path d="M13.997 5.17a5 5 0 0 0-8.101-4.09A5 5 0 0 0 1.28 9.342a5 5 0 0 0 8.336 5.109 3.5 3.5 0 0 0 5.201-4.065 3.001 3.001 0 0 0-.822-5.216zm-1-.034a1 1 0 0 0 .668.977 2.001 2.001 0 0 1 .547 3.478 1 1 0 0 0-.341 1.113 2.5 2.5 0 0 1-3.715 2.905 1 1 0 0 0-1.262.152 4 4 0 0 1-6.67-4.087 1 1 0 0 0-.2-1 4 4 0 0 1 3.693-6.61 1 1 0 0 0 .8-.2 4 4 0 0 1 6.48 3.273z"/>
          </svg> 
        </router-link>

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
        </ul>

        <form class="col-12 col-lg-auto mb-3 mb-lg-0 me-lg-3" role="search">
          <input  
            type="search" 
            class="form-control form-control-dark text-white bg-dark" 
            v-model="query_string" 
            @keyup="search" 
            placeholder="Procurar..." 
            aria-label="Search"
            @submit.prevent
            >
        </form>

        <div class="text-end">
          <button type="button" @submit.prevent class="btn btn-outline-light me-2">Login</button>
        </div>
      </div>
    </div>
  </header>
  `,

  data(){
    return {
        query_string:'',
    }
  },

  methods:{
      search() {
          this.$emit( 'search-food', this.query_string )
      }
  }

})