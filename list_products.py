import json, urllib.request

site_id = 'MLA'
seller_id = ["81644614"]

log_file = open("/tmp/LOG","w+")

for id in seller_id:

    url = "https://api.mercadolibre.com/sites/"+site_id+"/search?seller_id="+id

    json_url = urllib.request.urlopen(url)

    data = json.loads(json_url.read())

    for x in data['results']:
        L = ["id:", x['id'],"\n","title:", x['title'],"\n","category_id:", x['category_id']]
        log_file.writelines(L)
        url2 = "https://api.mercadolibre.com/categories/"+x['category_id']
        json_url2 = urllib.request.urlopen(url2)
        data2 = json.loads(json_url2.read())
        if x['category_id'] == data2['id']:
            L2 = ["\n","categoria:",data2['name'],"\n\n"]
            log_file.writelines(L2)
log_file.close()

