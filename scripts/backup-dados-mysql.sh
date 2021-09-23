#!/bin/bash

CAMINHO_HOME=/home/gpaulela/alura-think

cd $CAMINHO_HOME
if [ ! -d backup ]
then
	mkdir backup
fi

mysqldump -u root -p --all-databases > $CAMINHO_HOME/backup/$1.sql
if [ $? -eq 0 ]
then
	echo "Backup performed successfully"
else
	echo "There was a problem with backup"
fi
