const RestauranteDetails = {

    data() {

        return {
            restaurante: {}
        }
    },

    template:
    /*html*/
    `
    <header-bar @search-food="search"></header-bar>
    <restaurante-card-details :restaurante=restaurante></restaurante-card-details>
    <dishes-card :pratos="restaurante.pratos"></dishes-card>
    `,
    

    methods: {

        getRestauranteDetails(restaurante_id){

            fetch(`/api?restaurant_id=1`).then(response => response.json()).then(data => {        

                this.restaurante = data
                
                })
                .catch((error) => {
                console.error('Error:', error);
                });

        },
        search(query_string){

            fetch(`/api/consulta/${query_string}`).then(response => response.json()).then(data => {        

                this.restaurantes = data['restaurantes']
                
                })
                .catch((error) => {
                console.error('Error:', error);
                });

        }
    },

    beforeRouteEnter(to, from, next) {

        fetch(`/api?restaurant_id=${to.params.id}`).then(response => response.json()).then(data=> {
            next( vm => {
                vm.restaurante = data
            }
            )
        })
   

    
    }



    
}