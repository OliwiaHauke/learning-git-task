shopping_list = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"],
    "apteka": ["witamina C", "elektrolity"],
    "lidl": ["pinsa"]
}
for shop, products in shopping_list.items():
    products_capitalized = [product.capitalize() for product in products]
    print(f"Idę do {shop.capitalize()}, kupuję tam następujące rzeczy: {', '.join(products_capitalized)}")
total_items = sum(len(items) for items in shopping_list.values())
print(f"W sumie kupuję {total_items} produktów.") 