var app = new Vue({
    el: '#app',
    data: {
        link: 'Hello Vue!',
        shortened: '',
    },
    methods: {
        shorten: function (event) {
            this.shortened = this.link + 'shortened';
            axios.post('/urls/', {
                link: this.link
            })
                .then(function (response) {
                    console.log(response)
                })
                .catch(function (error) {
                    console.log(error)
                })
        }
    }
})
