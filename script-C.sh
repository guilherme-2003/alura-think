#!/bin/bash

read -p "Enter name of the first guest: " val

echo $val|grep "^[a-zA-Z]*$"

val="$?"
export val
./script-B.sh

if [[ $val == 0 ]]
then
	read -p "Enter name of the second guest: " val2

  echo $val2|grep "^[a-zA-Z]*$"

  val2="$?"	
	export val2
	./script-B.sh

  if [[ $val2 == 0 ]]
	then
		read -p "Enter the day: " num
		
		echo "$num"|grep "^[0-9]*$" 

		num="$?"
		export num
		./script-B.sh

		if [[ $num == 0 ]]
		then
			echo "Guests found!"
		else
			echo "Error! Invalid day!"

		exit
		fi
 	exit
	fi
exit
fi
