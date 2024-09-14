document.addEventListener('DOMContentLoaded', () => {
    const selectDrop = $('#country');  

    fetch('https://restcountries.com/v3.1/all')
        .then(res => res.json())
        .then(data => {

            let countries = data.map(country => {
                return { id: country.name.common, text: country.name.common };
            }).sort((a, b) => a.text.localeCompare(b.text));

            selectDrop.select2({
                data: countries,
                placeholder: 'Select a country', 
                allowClear: true
            });

            selectDrop.val(null).trigger('change');

        })
        .catch(err => {
            console.log("Error fetching countries:", err);
        });

    selectDrop.on('select2:open', function () {
        let searchField = document.querySelector('.select2-search__field');
        if (searchField) {
            searchField.focus(); 
        }
    });
});



