modelo_carro = str(input("Qual é o modelo do carro? "))
velocidade = 61
local_carro = 100

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # Distância onde o radar pega

if velocidade > RADAR_1:
    print("Modelo de carro {} passou pelo radar {}".format(modelo_carro, RADAR_RANGE))

if velocidade <= RADAR_1:
        print("{} passou pela rodovia dentro do limite da velocidade".format(modelo_carro))

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
        
            print("{} multado no radar {}".format(modelo_carro, RADAR_RANGE))