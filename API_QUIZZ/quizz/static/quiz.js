function get_all_quiz_old() {
    fetch('/questionnaires')
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
}

async function get_all_quiz() {
    const response = await fetch('/questionnaires');
    const data = await response.json();
    return data;
}



async function get_quiz_by_id(id) {
    const response = await fetch(`/questionnaires/${id}`);
    const data = await response.json();
    return data;
}

async function create_quiz(json) {
    const response = await fetch('/questionnaires', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
    });
    const data = await response.json();
    return data;
}

async function update_quiz(id, json) {
    const response = await fetch(`/questionnaires/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
    });
    const data = await response.json();
    return data;

}

async function delete_quiz(id) {
    const response = await fetch(`/questionnaires/${id}`, {
        method: 'DELETE'
    });
    const data = await response.json();
    return data;
}

async function get_all_question() {
    const response = await fetch('/questions');
    const data = await response.json();
    return data;
}

async function get_question_by_id(id) {

    const response = await fetch(`/questions/${id}`);
    const data = await response.json();
    return data;
}

async function create_question(json) {

    const response = await fetch('/questions', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
    });
    const data = await response.json();
    return data;
}

async function update_question(id, json) {

    const response = await fetch(`/questions/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)
    });
    const data = await response.json();
    return data;
}

async function delete_question(id) {
    const response = await fetch(`/questions/${id}`, {method: 'DELETE'});
    const data = await response.json();
    return data;
}


function clearDataset() {
    console.log('Clear');
    const THead = document.getElementById('Thead');
    const TBody = document.getElementById('Tbody');
    THead.innerHTML = '';
    TBody.innerHTML = '';
}
