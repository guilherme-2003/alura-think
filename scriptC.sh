#!/bin/bash

read -p "Enter name of the first guest: " val

if [ -z $val ]
then
	echo "You need to enter some information!"
else
echo $val|grep "^[a-zA-Z]*$"

export val="$?"

if [[ $val == 0 ]]
then
	read -p "Enter name of the second guest: " val2
	if [ -z $val2 ]
	then
		echo "You need to enter some information!"
	else
  echo $val2|grep "^[a-zA-Z]*$"

  val2="$?"	

  if [[ $val2 == 0 ]]
	then
		read -p "Enter the day: " num
		if [ -z $num ]
		then
				echo "You need to enter some information!"
		else	
		echo "$num"|grep "^[0-9]*$" 

		num="$?"

		if [[ $num == 0 ]]
		then
			echo "Guests found!"
		else
			echo "Error! Invalid day!"

fi
	fi
		fi
		exit
		fi
	exit
	fi
exit
fi

