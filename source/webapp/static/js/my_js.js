// 3 ий этап добавление комментария

let data = JSON.stringify({
    'text': 'London Colney',
    'image': 6,
    'author': 1
});

$.ajax({
    url: 'http://localhost:8000/api/v1/comments/',
    method: 'post',
    data: data,
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log(response);},
    error: function(response, status){console.log(response);}
});

// 3 ий этап удаление комментария
$.ajax({
    url: 'http://localhost:8000/api/v1/comments/48/',
    method: 'delete',
    dataType: 'json',
    contentType: 'application/json',
    success: function(response, status){console.log(response);},
    error: function(response, status){console.log(response);}
});