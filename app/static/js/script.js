document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('citySelect').addEventListener('change', function() {
        var otherCityInput = document.getElementById('otherCity');
        if (this.value == 'Other') {
            otherCityInput.style.display = 'block';
        } else {
            otherCityInput.style.display = 'none';
        }
    });
});
