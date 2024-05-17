function obterListaCarros(ordenacao) {
    let url = '/api/carros';
    if (ordenacao) {
        url += `?ordenacao=${ordenacao}`;
    }

    fetch(url, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);

        const tbody = document.querySelector('.table-carros tbody');
        if (tbody) {

            tbody.innerHTML = '';

            data.forEach(carro => {
                const newRow = `<tr>
                    <td>${carro.id}</td>
                    <td>${carro.nomeFabricante}</td>
                    <td>${carro.modelo}</td>
                    <td>${carro.ano}</td>
                    <td>${carro.cor}</td>
                    <td>${carro.km}</td>
                    <td><strong>R$: </strong>${carro.preco}</td>
                    <td><button onclick="editarCarro(${carro.id})">Editar</button></td>
                </tr>`;
                tbody.insertAdjacentHTML('beforeend', newRow);
            });
        } else {
            console.error('O elemento tbody não foi encontrado');
        }
    })
    .catch(error => {
        console.error('Erro:', error);
        alert('Ocorreu um erro ao obter a lista de carros.');
    });
}

document.addEventListener('DOMContentLoaded', () => {
    obterListaCarros();

    const selectOrdenacao = document.querySelector('#ordenacao');
    if (selectOrdenacao) {
        selectOrdenacao.addEventListener('change', () => {
            const ordenacaoSelecionada = selectOrdenacao.value;
            obterListaCarros(ordenacaoSelecionada);
        });
    } else {
        console.error('O elemento select para ordenação não foi encontrado');
    }
});

function editarCarro(idCarro) {
    window.location.href = `/editar_carro?id=${idCarro}`;
}
