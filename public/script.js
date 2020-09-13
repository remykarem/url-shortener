var app = new Vue({
    el: '#app',
    data: {
        link: 'tech.gov.sg',
        shortLink: '',
        loading: false
    },
    methods: {
        shorten: function (event) {
            const vm = this;

            vm.loading = true;
            vm.shortLink = '';

            axios.post('/urls/', {
                raw: this.link
            })
                .then(function (response) {
                    console.log(response);
                    console.log(response.data.shortLink);
                    vm.loading = false;
                    vm.shortLink = response.data.shortLink;
                })
                .catch(function (error) {
                    console.log(error)
                })
        },
        copyToClipboard: function (event) {
            var text = document.getElementById('short-link');
            var range = document.createRange();

            window.getSelection().removeAllRanges();
            range.selectNode(text);
            window.getSelection().addRange(range);
            document.execCommand('copy');
            window.getSelection().removeAllRanges();

            UIkit.notification({
                message: "<center><small>Copied to clipboard</small></center>",
                pos: "bottom-center"
            });
        }
    }
})
