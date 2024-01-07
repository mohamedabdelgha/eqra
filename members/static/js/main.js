$(document).on('submit','#task-form',function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'{% url "/" %}',
    })
});
