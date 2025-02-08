nome = input ("Qual o seu nome? ")
peso = input ("Qual o seu peso? ")
altura = input ("Qual a sua altura em metros? ")

imc = float (peso) // (float (altura) * float (altura))

print ("Olá ", nome, " baseado no peso de ", peso, "KG e na altura de ", altura, "metros seu IMC é de ", imc )