// DESAFIO EM JAVASCRIPT

// Desafio em JavaScript na DIO tem funções "gets" e "print" acessiveis globalmente.
// "gets": Ler uma linha com dados de entrada do usúario.
// "print": Imprime um texto de saída pulando linha.

// Ler os valores de entrada:
const valorSalario = parseFloat(gets());
const valorBeneficio = parseFloat(gets());

// calcula o imposto através da função "calcularImposto"
const valorImposto = calcularImposto(valorSalario);

// Calcula e imprime a sa´da (com 2 casas decimais)
const saida = valorSalario - valorImposto + valorBeneficio;
print(saida.toFixed(2));

// Função útil para o calculo do imposto (baseado nas aliquotas)
function calcularImposto(salario) {
    let aliquota;
    if (salario >= 0 && salario <= 1100) {
        aliquota = 0.05;
    } else if (salario >= 1100.01 && salario <= 2500) {
        aliquota = 0.10;
    } else if (salario >= 2500) {
        aliquota = 0.15;
    }


    return aliquota * salario;
}
