let countrySelected = RM('#id_default_country').val();
if(!countrySelected) {
    RM('#id_default_country').css('color', '#aab7c4');
};
RM('#id_default_country').change(function() {
    countrySelected = RM(this).val();
    if(!countrySelected) {
        RM(this).css('color', '#aab7c4');
    } else {
        RM(this).css('color', '#000');
    }
});