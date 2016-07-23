#!/bin/bash

pokemon_id=$1
stardust=$2
cp=$3
filename="pokemon_data/pokemon_id_${pokemon_id}"
if [ -e ${filename} ]
  then python calculate.py ${filename} ${stardust} ${cp}
  else echo "pokemon id ${pokemon_id} not found."
fi
