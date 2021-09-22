#!/bin/bash

resposta_http=$(curl --write-out %{http_code} --silent --output /dev/null http://localhost)
if [ $resposta_http -eq 200 ]
then 
	echo "Everthing alright with the server"
else 
	echo "There was a problem with the server. Trying to reboot"
 	sudo service apache2 start
	echo "...Server reboot successfully executed"	
fi
