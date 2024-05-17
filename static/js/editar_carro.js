document.addEventListener('DOMContentLoaded', () => {
    const idCarro = obterIdCarroDaQuerystring();
    if (idCarro) {
        obterDadosCarro(idCarro);
    } else {
        console.error('ID do carro não encontrado na querystring.');
    }

    const btnSalvar = document.getElementById('btnSalvar');
    btnSalvar.addEventListener('click', salvarCarro);
});

function obterIdCarroDaQuerystring() {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get('id');
}

function obterDadosCarro(idCarro) {
    fetch(`/api/carros/${idCarro}/editar`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('fabricanteTexto').textContent = data.nomeFabricante;
        document.getElementById('modeloTexto').textContent = data.modelo;
        document.getElementById('anoTexto').textContent = data.ano;
        document.getElementById('corTexto').textContent = data.cor;
        document.getElementById('km').value = data.km;
        document.getElementById('preco').value = data.preco;
        document.getElementById('idCarro').value = idCarro;
    })
    .catch(error => {
        console.error('Erro ao obter dados do carro:', error);
        alert('Ocorreu um erro ao obter os dados do carro.');
    });
}

function salvarCarro() {
    const idCarro = document.getElementById('idCarro').value;
    const km = document.getElementById('km').value;
    const preco = document.getElementById('preco').value;

    const dadosCarro = {
        id: idCarro,
        km: km,
        preco: preco
    };

    fetch(`/api/carros/${idCarro}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dadosCarro)
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        alert(data.message);
        window.location.href = '/lista';
    })
    .catch(error => {
        console.error('Erro ao salvar carro:', error);
        alert('Ocorreu um erro ao salvar as alterações no carro.');
    });
}
