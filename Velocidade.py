velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

condicao_multa = local_carro == LOCAL_1 + RADAR_RANGE or local_carro == LOCAL_1 - RADAR_RANGE or local_carro == LOCAL_1



if velocidade > RADAR_1:
    print ("Carro acima da velocidade permitida")
    if condicao_multa:
        print ("O carro será multado")
    else:
        print ("O carro não sera multado")

else:
    print ("Carro dentro da velocidade permitida")