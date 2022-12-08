$(document).ready(function () {

    const csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    
    //################### adding a click event to delete an item ########################
    $('#delete').on('click', (e) => {
        e.preventDefault()
        const id = $('#delete').data('id')
        const url =`/leads/delete/${id}/`
        if (confirm('Are you sure you want to delete this lead from the database?')) {
           $.ajax({
                type: 'POST',
                url: url,
                data: { csrfmiddlewaretoken: csrf_token },
                dataType: 'json',    
           })
        window.location.replace('/leads/')
    } else {
        window.location.replace('/leads/')
}
    })
//############################END ####################################

})