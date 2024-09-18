document.addEventListener('DOMContentLoaded', function () {
    const regionSelect = document.getElementById('region');
    const provinceSelect = document.getElementById('province');
    const municipalitySelect = document.getElementById('municipality');

    const regions = {
        'Region III': {
            'Pampanga': ['Angeles City', 'San Fernando', 'Guagua'],
            'Tarlac': ['Tarlac City', 'Concepcion', 'Capas']
        },
        'Region IV-A': {
            'Laguna': ['Calamba', 'Santa Rosa', 'San Pedro'],
            'Cavite': ['Bacoor', 'Dasmariñas', 'Imus']
        }
    };

    // Update Province Options based on Region
    regionSelect.addEventListener('change', function () {
        const selectedRegion = regionSelect.value;

        // Clear current options
        provinceSelect.innerHTML = '<option value="">Select Province</option>';
        municipalitySelect.innerHTML = '<option value="">Select Municipality</option>';

        if (selectedRegion && regions[selectedRegion]) {
            const provinces = Object.keys(regions[selectedRegion]);
            provinces.forEach(function (province) {
                const option = document.createElement('option');
                option.value = province;
                option.textContent = province;
                provinceSelect.appendChild(option);
            });
        }
    });

    // Update Municipality Options based on Province
    provinceSelect.addEventListener('change', function () {
        const selectedRegion = regionSelect.value;
        const selectedProvince = provinceSelect.value;

        // Clear current options
        municipalitySelect.innerHTML = '<option value="">Select Municipality</option>';

        if (selectedRegion && selectedProvince && regions[selectedRegion][selectedProvince]) {
            const municipalities = regions[selectedRegion][selectedProvince];
            municipalities.forEach(function (municipality) {
                const option = document.createElement('option');
                option.value = municipality;
                option.textContent = municipality;
                municipalitySelect.appendChild(option);
            });
        }
    });
});
