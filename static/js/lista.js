function obterListaCarros() {
    fetch('/api/carros', {
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
                data.forEach(carro => {
                    const newRow = `<tr>
                    <td>${carro.id}</td>
                    <td>${carro.nomeFabricante}</td>
                    <td>${carro.modelo}</td>
                    <td>${carro.ano}</td>
                    <td>${carro.cor}</td>
                    <td>${carro.km}</td>
                    <td><strong>R$: </strong>${carro.preco}</td>
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



document.addEventListener('DOMContentLoaded', obterListaCarros);
