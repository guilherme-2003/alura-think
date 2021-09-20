#!/bin/bash

CAMINHOS_IMAGENS=~/alura-think/imagens-livros

convert $CAMINHOS_IMAGENS/$1.jpg $CAMINHOS_IMAGENS/$1.png
convert $CAMINHOS_IMAGENS/$2.jpg $CAMINHOS_IMAGENS/$2.png
