"""descontos = {
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
    print("Cupom inválido")"""



descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

preco = float(input())
cupom = input().strip().upper()

if preco == 100:
    desconto = descontos["DESCONTO10"]
    
elif preco == 200:
    desconto = descontos["DESCONTO20"]
  
elif preco == 50:
    desconto = descontos["SEM_DESCONTO"]
   
valor_desconto = preco * desconto
preco_final = preco - valor_desconto
print(preco_final)