function deletePost(i)
{
    $.ajax({
        url: '/Posts/Delete',
        type: 'POST',
        data: {
            id: i
        }
    }).then(function(data) {
        window.location = '/Posts'
    });
}
