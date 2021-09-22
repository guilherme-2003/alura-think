#!/bin/bash

memoria_total=$(free | grep -i mem | awk '{ print $2 }')
memoria_consumida=$(free | grep -i mem | awk '{ print $3 }')
relacao_memoria_atual_total=$(bc <<< "scale=2;$memoria_consumida/$memoria_total *100" | awk -F. '{ print $1 }')

if [ echo $relacao_memoria_atual_total -gt 50 ]
then
mail -5 "Consumo de memória acima do limite" adm.mutilidae@gmail.com<<del
O consumo de memória está acima do limite que foi especificado. O limite é de $(free -h | grep -h | grep -i mem | awk '{ print $3 }')
del

fi
