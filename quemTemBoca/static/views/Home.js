const Home = {
    data() {
        return {
            restaurantes: []
        }
    },

    template:
    /*html*/
    `
    <header-bar @search-food="search"></header-bar>
    <restaurante-deck :restaurantes="restaurantes"></restaurante-deck>`,

    methods: {

        getRestaurantes(){

            fetch('/api').then(response => response.json()).then(data => {        

                this.restaurantes = data['restaurantes']
                
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

    beforeMount(){
        this.getRestaurantes()
    },
}