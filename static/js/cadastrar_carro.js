function limparFormulario() {
    document.getElementById('cadastroForm').reset();
}

function enviarFormulario(event) {
    event.preventDefault();

    const form = document.getElementById('cadastroForm');
    const formData = new FormData(form);

    for (let value of formData.values()) {
        if (!value) {
            alert('Por favor, preencha todos os campos.');
            return;
        }
    }

    fetch('/api/carros', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(Object.fromEntries(formData))
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Erro ao cadastrar carro.');
        }
        return response.json();
    })
    .then(data => {
        console.log(data);
        alert(data.message);
        limparFormulario();
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao cadastrar o carro.');
    });
}

document.addEventListener('DOMContentLoaded', () => {
    const formCadastro = document.getElementById('cadastroForm');
    formCadastro.addEventListener('submit', enviarFormulario);
});
