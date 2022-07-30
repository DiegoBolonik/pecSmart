Saída esperada 1 -Valores MAC repetidos

![image](https://user-images.githubusercontent.com/79227339/181866506-65fdf9f1-eb77-4653-8da3-392a28d13151.png)

Saída esperada 2 - Ângulo de inclinação
![image](https://user-images.githubusercontent.com/79227339/181866586-ef3d94c6-950b-4356-9d39-006f72d2902d.png)

Saída esperada 3 - Porcentagem de erro em medição dos microfones
![image](https://user-images.githubusercontent.com/79227339/181866746-da79d4e9-f7bb-4445-9e55-cfa8ea7c177b.png)


*Valores variam de acordo com as medições de log da API.

# Contexto 1

Dentro da PecSmart possuímos múltiplos sensores, de diferentes tipos, cada um possuindo um identificador único associado ao hardware. Sendo único, não deveria repetir na base, porém como seu cadastro é feito de forma manual, falhas podem acontecer.

Nossos sensores podem ser encontrados na rota /sensors/.

Pergunta 1

    Quantos sensores têm o campo "mac" duplicado? Você poderia gerar uma lista com os mesmos?

# Contexto 2

Um de nossos principais produtos é o SmartFeed. Este equipamento é acoplado internamente a um silo para a realização de medições de volume de ração ao longo do dia. Um dos problemas enfrentados na operação deste produto é que, por descuido na instalação ou uso incorreto, o encaixe dele entorta, comprometendo sua operação.

Nossos equipamentos possuem logs que são guardados em nossa base na rota /sensor logs, tendo informações úteis como o id do equipamento que a gerou (campo “owner”) e o tipo de log (campo “type”), e nestes é possível identificar quais feeds estão tortos analisando o valor de “IMU angle” contido no campo “message” em logs do tipo “SWEEP_MEASURE_SAFE”.

Pergunta 2

    Quantos e quais sensores SmartFeed estão tortos? Considere que o ângulo ideal para o mesmo é de 0 graus.

# Contexto 3

Os equipamentos SmartMic são formados por uma central e até 8 microfones “dummy” associados a mesma. Durante a operação, a central procura na rede local os microfones a ela associados, mas por vezes, por problemas de rede, não consegue encontrar todos.

Na rota /sensor_logs existem logs de type "DUMMYS_FOUND" que dizem quantos microfones foram encontrados pela central que gerou este log, em cada varredura, e quantos deveriam ter sido encontrados (em geral 8).

Pergunta 3

    Qual o percentual de vezes que as centrais não conseguem achar todos os microfones a ela associados?
