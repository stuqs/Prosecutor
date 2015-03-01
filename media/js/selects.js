$(function test1(){
    $("select#id_department").change(function(){
        $.getJSON("/ajax/categ/",{department_id:+$(this).val()}, function(j) {
            var options = '<option value="">Выберите Отдел</option>';
            for (var i = 0; i < j.length; i++) {
                options += '<option value="' + parseInt(j[i].pk) + '">' + j[i].fields['name'] + '</option>';
            }
            $("#id_division").html(options);
            $("#id_division option:first").attr('selected', 'selected');
            $("#id_division").attr('disabled', false);
        })
        $("#id_department").attr('selected', 'selected');
    })
})