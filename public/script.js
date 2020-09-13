var app = new Vue({
    el: '#app',
    data: {
        link: 'tech.gov.sg',
        shortLink: '',
    },
    methods: {
        shorten: function (event) {
            const vm = this;
            axios.post('/urls/', {
                raw: this.link
            })
                .then(function (response) {
                    console.log(response);
                    console.log(response.data.shortLink);
                    vm.shortLink = response.data.shortLink;
                })
                .catch(function (error) {
                    console.log(error)
                })
        }
    }
})
