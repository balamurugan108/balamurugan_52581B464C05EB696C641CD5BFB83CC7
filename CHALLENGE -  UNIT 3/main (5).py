def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["apple", "banana", "apple", "grape", "apple"]

while True:
    target_product = input("\n Enter the target product (or 'exit' to quit): ")
    
    if target_product.lower() == 'exit':
        break

    result = linear_search_product(products, target_product)
    
    if result:
        print(f"\n The product '{target_product}' was found at indices: {result}")
    else:
        print(f"\n The product '{target_product}' was not found in the list.")

