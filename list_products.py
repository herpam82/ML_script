import json, urllib.request

site_id = 'MLA'
seller_id = ["81644614"]

for id in seller_id:

    url = "https://api.mercadolibre.com/sites/"+site_id+"/search?seller_id="+id

    print(url)

    json_url = urllib.request.urlopen(url)

    data = json.loads(json_url.read())


    for x in data['results']:
        print("id:", x['id'],"\n","title:", x['title'],"\n","category_id:", x['category_id'])
        url2 = "https://api.mercadolibre.com/categories/"+x['category_id']
        json_url2 = urllib.request.urlopen(url2)
        data2 = json.loads(json_url2.read())
        if x['category_id'] == data2['id']:
            print(" categoria:",data2['name'],"\n")

