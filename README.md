# ML_script
Script para test de ML

El script necesita para funcionar la applicación 'JQ' para parsear el JSON
Se puede obtener de: https://stedolan.github.io/jq/

Se ejecuta directamente sobre el path donde bajes el script con ./list_products.sh
No requiere ningún output, si se quieren buscar más clientes, se puede editar el vector seller_ids agregando más IDs.

El log se guarda en /tmp

Se utilizó la API: https://api.mercadolibre.com/sites/${site_id}/search?seller_id=${seller_id}

# ML_Script en Python

Nueva versión en Python, trae también el nombre de la categoria que olvidé poner en el script en bash.

Se llama list_products.py directamente. Si se quieren modificar el site_id o los seller_id se modifica dentro del script.

Se utilizó la API: https://api.mercadolibre.com/sites/${site_id}/search?seller_id=${seller_id}

Se utilizó la API: https://api.mercadolibre.com/categories/${category_id}
