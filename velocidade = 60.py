velocidade = 60
local_carro = 90

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local onde o radar 1 está
RADAR_RANGE = 1 # Distância onde o radar pega

if velocidade > RADAR_1:
    print("Velocidade do carro passou do radar 1")

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1
        
            print("Carro multado no radar 1")