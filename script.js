// Aguarda o HTML carregar para aplicar o evento de clique no botão
document.getElementById('btnCalcular').addEventListener('click', calcularIMC);

function calcularIMC() {
    // Captura os valores dos inputs atualizados no momento do clique
    const peso = parseFloat(document.getElementById('peso').value);
    const altura = parseFloat(document.getElementById('altura').value);
    
    // Elementos da tela que vamos modificar
    const resultBox = document.getElementById('resultBox');
    const txtResultado = document.getElementById('resultado');
    const txtClassificacao = document.getElementById('classificacao');

    // Validação de segurança
    if (!peso || !altura || peso <= 0 || altura <= 0) {
        alert("Por favor, insira valores válidos para peso e altura.");
        return;
    }

    // Cálculo do IMC
    const imc = peso / (altura * altura);
    
    // Exibe o número com 2 casas decimais
    txtResultado.innerText = imc.toFixed(2);

    // Variáveis para guardar o texto e a classe CSS da resposta
    let classificacao = "";
    let classeCor = "";

    // Tabela de classificação do IMC
    if (imc < 18.5) {
        classificacao = "Abaixo do peso";
        classeCor = "alerta";
    } else if (imc >= 18.5 && imc < 25) {
        classificacao = "Peso normal";
        classeCor = "normal";
    } else if (imc >= 25 && imc < 30) {
        classificacao = "Sobrepeso";
        classeCor = "alerta";
    } else if (imc >= 30 && imc < 35) {
        classificacao = "Obesidade Grau I";
        classeCor = "perigo";
    } else if (imc >= 35 && imc < 40) {
        classificacao = "Obesidade Grau II";
        classeCor = "perigo";
    } else {
        classificacao = "Obesidade Grau III (Mórbida)";
        classeCor = "perigo";
    }

    // Atualiza o texto da classificação
    txtClassificacao.innerText = classificacao;
    
    // Limpa classes anteriores e aplica a nova cor correspondente
    txtClassificacao.className = classeCor; 
    
    // Torna o bloco do resultado visível na tela
    resultBox.style.display = "block";
}