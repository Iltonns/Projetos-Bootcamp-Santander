descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

preco = float(input())
cupom = input().strip().upper()

if cupom in descontos:
    desconto = descontos[cupom]
    preco_final = preco * (1 - desconto)
    print(f"{preco_final:.2f}")
else:
    print("Cupom inválido")

