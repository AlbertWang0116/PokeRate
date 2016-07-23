#!/bin/bash

nidoranf="Nidoran♀"
pokemon_id=$1
curl http://pokemongo.gamepress.gg/pokemon/${pokemon_id} > /tmp/pokemonpage
pokemon_name=$(sed -n '/<title>/p' /tmp/pokemonpage | sed 's/^<title>//g' | sed 's/\ |\ Pokemon\ Go<\/title>//g')
echo "${pokemon_name}" > /tmp/pokemonname
pokemon_name=$(python rename.py /tmp/pokemonname)
echo "pokemon name:${pokemon_name}"
sed -n '/minmaxtable/,/table/p' /tmp/pokemonpage | sed -n '/tbody/,/tbody/p' > /tmp/pokemonxml
python parsedata.py /tmp/pokemonxml > pokemon_data/${pokemon_name}
cp pokemon_data/${pokemon_name} pokemon_data/pokemon_id_${pokemon_id}
