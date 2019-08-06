#!/bin/bash

LOG="/tmp/log"

site_id=MLA
seller_ids=81644614

echo "Begginning LOG on $date" > $LOG

for seller_id in ${seller_ids[*]}
do
	echo "seller_id=${seller_id}" >> $LOG
	echo "-------------------" >> $LOG
	curl -s https://api.mercadolibre.com/sites/${site_id}/search?seller_id=${seller_id} | ./jq '.results[] | { id: .id, title: .title, category_id: .category_id }' >> $LOG
done
