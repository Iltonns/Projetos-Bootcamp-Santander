
/* Faça um programa que calcule e imprima o salário a ser transferido para um funcionário
  
Para realizar o calculo receba o valor bruto do salário e o adicional dos beneficios.

O salário a ser trasnferido é calculado da seguinte maneira:
    
valor bruto do salario - percentual de imposto mediana ai salário + adicional dos beneficios
    
Para calcular o percentual de imposto segue as aliquotas:
    
De R$ 0.00 a R$ 1.100,00 = 5.00%
DE R$ 1.100,00 a R$ 2.500,00 = 10.00 %
Maior que 2.500,00 = 15.00%
*/

// Para ler e escrever dados em Java:
// new Scanner(System.in): Cria um leitor de Entradas, com métodos úteis com prefixo "next";
// System.out.print: Imprime um texto de saída (output) e pulando uma linha

import java.util.Scanner;

public class Desafio {

    public static void main(String[] args) {
    // Ler os valores de entrada
    Scanner leitorDeEntradas = new Scanner(System.in);
    float valorSalario = leitorDeEntradas.nextFloat();
    float valorBeneficio = leitorDeEntradas.nextFloat();

    //Atribui as aliquotas mediante o salario:
    float valorImposto = 0;
    if (valorSalario >= 0 && valorSalario <= 1100) {
        valorImposto = 0.05F * valorSalario;
    } else if (valorSalario >= 1100.01 && valorSalario <= 2500) {
        valorImposto = 0.10F * valorSalario;
    } else (valorSalario >= 2500) {
        valorImposto = 0.15F * valorSalario;
    }
   
    // Calcula e imprime a Saída (Com 2 casas decimais):
    float saida = valorSalario - valorImposto + valorBeneficio;
    System.out.print(String.format("%.2f", saida));
    }
}

