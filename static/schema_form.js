  $( document ).ready(function() {
    $('#add_column').click(function() {
        var form_idx = $('#id_column_set-TOTAL_FORMS').val();
        $('#form_set').append($('#empty_form').html().replace(/__prefix__/g, form_idx));
        $('#id_column_set-TOTAL_FORMS').val(parseInt(form_idx) + 1);
    });
    $("[id$='column_type']").change((e) => {
        let row = $(e.target).parents(".form-inline")
        let from = $(row).find("[id$='range_from']")
        let to = $(row).find("[id$='range_to']")
        if( $(e.target).val() == "Text" || $(e.target).val() == "Integer" ) {
            $(from).show()
            $(to).show()
        }
        else {
            $(from).hide()
            $(to).hide()

        }
    }
 )
});