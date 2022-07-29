import requests
import json

response = requests.get('http://18.231.62.128:8400/sensors_logs', headers={ 'Authorization': 'Token b2925f3bba618a5f770ad67d6a1d5bd68e7f2d8f' })

objeto = response.json()

#--------------------------- "DUMMYS_FOUND" -------------------------
valores2 = []
v3 = []
v2 = []
v1 = []
index = 0
busca = 'DUMMYS_FOUND'

print("Relação de quantidade de DUMMYS_FOUND:")

# ------------------- LOOPING DE BUSCA DOS MICROFONES-----------------
for i in objeto['results']:
  data3 = i['type']
  if busca in data3:
    elem = data3
    elem2 = i['value']
    elem3 = i['owner']
    valores2.append(int(elem2))
    v3.append(elem3)
    var1 = int(elem2)
    porcentagem = (var1 / 8 * 100)
    valor_final = 100 - porcentagem
    v2.append(valor_final)
    index = index +1

    
print("Percentual de não conseguir achar todos os microfones: ", v2, "%")
print("Owners: ", v3)
print("Quant. operantes: ", valores2)
print("Total de dispositivos: ", index)

#Nossos equipamentos SmartMic são formados por uma central e até 8 microfones "dummy" associados a mesma. Durante a operação, a central procura na rede local os microfones a ela associados, mas por vezes, por problemas de rede, não consegue encontrar todos.

#Na rota /sensor_logs existem logs de type "DUMMYS_FOUND" que dizem quantos microfones foram encontrados pela central que gerou este log, em cada varredura, e quantos deveriam ter sido encontrados (em geral 8).
