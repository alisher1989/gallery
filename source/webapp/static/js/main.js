const baseUrl = 'http://localhost:8000/api/v1/';

function getFullPath(path) {
    path = path.replace(/^\/+|\/+$/g, '');
    path = path.replace(/\/{2,}/g, '/');
    return baseUrl + path + '/';
}


function makeRequest(path, method, auth=true, data=null) {
    let settings = {
        url: getFullPath(path),
        method: method,
        dataType: 'json'
    };
    if (data) {
        settings['data'] = JSON.stringify(data);
        settings['contentType'] = 'application/json';
    }
    if (auth) {
        settings.headers = {'Authorization': 'Token ' + getToken()};
    }
    return $.ajax(settings);
}

let homeLink, enterLink, exitLink, formSubmit, formTitle, content, formModal,
    authorInput, textInput, emailInput, like, dislike, commentForm, createLink;

function setUpGlobalVars() {
    commentForm = $('#comment_form');
    like = $('#like');
    dislike= $('#dislike');
    homeLink = $('#home_link');
    enterLink = $('#enter_link');
    exitLink = $('#exit_link');
    formSubmit = $('#form_submit');
    createLink = $('#create_link');
    formTitle = $('#form_title');
    content = $('#content');
    formModal = $('#form_modal');
    authorInput = $('#author_input');
    textInput = $('#text_input');
    emailInput = $('#email_input');
}

function createComment(text, author) {
    const credentials = {text, author};
    let request = makeRequest('photo/', 'post', true, credentials);
    request.done(function(data, status, response) {
        console.log(data);
        formModal.modal('hide');
    }).fail(function(response, status, message) {
        console.log('Could not add quote');
        console.log(response.responseText);
    });
}

function createCommentForm() {
    commentForm.on('submit', function (event) {
        event.preventDefault();
        createComment(textInput.val(), authorInput.val());
    });

    createLink.on('click', function (event) {
        event.preventDefault();
        console.log('yes');
        commentForm.removeClass('d-none');
        formTitle.text('Добавить');
        formSubmit.text('Добавить');
        formSubmit.off('click');
        formSubmit.on('click', function (event) {
            commentForm.submit()
        });
    });
    getComments();
}

function getComments() {
    let request = makeRequest('photo/', 'post', true, credentials);
    request.done(function(data, status, response) {
        console.log(data);
        formModal.modal('hide');
    }).fail(function(response, status, message) {
        console.log('Could not add quote');
        console.log(response.responseText);
    });
}




$(document).ready(function() {
    setUpGlobalVars();
    createCommentForm();
});