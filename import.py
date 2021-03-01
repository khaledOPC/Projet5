import requests
from constant import MAX_NB_CATEGORIES
from constant import MAX_NB_PRODUCTS_PER_CATEGORIE


url = "https://fr.openfoodfacts.org/categories.json"

response = requests.get(url)

if response.ok:
    response_json = response.json()
    for category_dict in response_json["tags"][:MAX_NB_CATEGORIES]:
        category_id = category_dict["id"][3:]
        payload = {"tag_0": category_id, "tag_contains_0": "contains", "page_size": MAX_NB_PRODUCTS_PER_CATEGORIE, "tagtype_0": "categories", "json": "true", "action": "process"}
        response = requests.get("https://fr.openfoodfacts.org/cgi/search.pl", params=payload)
        if response.ok:
            products = response.json()["products"]
            for product in products:
                product_catego_fr = product.get("product_name_fr")
                stores_tags = product.get("stores_tags")
                nova_groups = product.get("nova_groups")
                nutriscore_grade = product.get("nutriscore_grade")
                url_product = product.get("url")
                categories_hierarchy = product.get("categories_hierarchy")
                print(category_id, product_category_fr, stores_tags, nova_groups, nutriscore_grade, url_product, categories_hierarchy)













