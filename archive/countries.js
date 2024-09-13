document.addEventListener('DOMContentLoaded', () => {
    const selectDrop = $('#country');  // Using jQuery selector

    // Fetch countries from the API
    fetch('https://restcountries.com/v3.1/all')
        .then(res => res.json())
        .then(data => {
            // Map countries to an array and sort them alphabetically by name
            let countries = data.map(country => {
                return { id: country.name.common, text: country.name.common };
            }).sort((a, b) => a.text.localeCompare(b.text));

            // Add countries to Select2 dropdown
            selectDrop.select2({
                data: countries,
                placeholder: 'Select a country',  // Placeholder when no option is selected
                allowClear: true
            });

            // Ensure no country is selected by default
            selectDrop.val(null).trigger('change');  // Clear the selection initially

        })
        .catch(err => {
            console.log("Error fetching countries:", err);
        });

    // Focus cursor in the search box when the dropdown opens
    selectDrop.on('select2:open', function () {
        let searchField = document.querySelector('.select2-search__field');
        if (searchField) {
            searchField.focus();  // Automatically focus the search box
        }
    });
});



