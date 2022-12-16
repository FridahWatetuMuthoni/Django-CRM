$(document).ready(function () {

    const csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    
    //################### adding a click event to delete a Lead ########################
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
//################### adding a click event to delete a Lead ########################
    $('#delete-agent').on('click', (e) => {
        e.preventDefault()
        const id = $('#delete-agent').data('id')
        const url =`/agents/delete/${id}/`
        if (confirm('Are you sure you want to delete this agent from the database?')) {
           $.ajax({
                type: 'POST',
                url: url,
                data: { csrfmiddlewaretoken: csrf_token },
                dataType: 'json',    
           })
        window.location.replace('/agents/')
    } else {
        window.location.replace('/agents/')
}
    })
//############################END ####################################
    
//############################ ADDING CLASSES TO ALL MY FORMS ####################################
/*const html_form_classes = ['block', 'w-full', 'p-3', 'rounded', 'focus:outline-none', 'focus:ring', 'focus:ring-opacity-25', 'focus:ring-violet-400', 'dark:bg-gray-50','mt-4','shadow']

    $('input').each((element) => {
        html_form_classes.forEach((class_name) => {
            let current_element = $('input')[element]
            if (current_element['type'] !== 'checkbox') {
                current_element.classList.add(class_name)
            }
        })
    })

    $('select').each((element) => {
        html_form_classes.forEach((class_name) => {
            let current_element = $('select')[element]
            current_element.classList.add(class_name)
            $('select').css('margin-top','20px')
        })
    })
*/
    //############################END ####################################


})