​#!/bin/bash

LOG="/tmp/log"

seller_ids=(81644614)
site_id=MLA

for seller_id in ${seller_ids[*]}
do
	curl -s https://api.mercadolibre.com/sites/${site_id}/search?seller_id=${seller_id} | ./jq '.results[] | { id: .id, title: .title, category_id: .category_id }' >> $LOG
done
