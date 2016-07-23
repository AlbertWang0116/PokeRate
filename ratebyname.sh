#!/bin/bash

pokemon_name=$1
stardust=$2
cp=$3
filename="pokemon_data/${pokemon_name}"
if [ -e ${filename} ]
  then python calculate.py ${filename} ${stardust} ${cp}
  else echo "pokemon name ${pokemon_name} not found."
fi
