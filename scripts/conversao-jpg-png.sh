#!/bin/bash

cd ~/alura-think/imagens-livros
for imagem in *.jpg 
do
	convert $imagem $imagem.png
done
