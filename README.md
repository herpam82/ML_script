# ML_script
Script para test de ML

El script necesita para funcionar la applicación 'JQ' para parsear el JSON
Se puede obtener de: https://stedolan.github.io/jq/

Se ejecuta directamente sobre el path donde bajes el script con ./list_products.sh
No requiere ningún output, si se quieren buscar más clientes, se puede editar el vector seller_ids agregando más IDs.

El log se guarda en /tmp

Se utilizó la API: https://api.mercadolibre.com/sites/${site_id}/search?seller_id=${seller_id}
