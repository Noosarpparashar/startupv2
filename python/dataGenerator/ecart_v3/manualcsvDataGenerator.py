import csv
import time
import random
from faker import Faker

fake = Faker()

# Predefined dictionary of product names and categories
PRODUCT_DICT = {
    'Laptop': 'Electronics',
    'Desktop Computer': 'Electronics',
    'Smartphone': 'Electronics',
    'T-shirt': 'Clothing',
    'Jeans': 'Clothing',
    'Dress': 'Clothing',
    'Sofa': 'Home Decor',
    'Coffee Table': 'Home Decor',
    'Bedding Set': 'Home Decor',
    'Action Figure': 'Toys',
    'Board Game': 'Toys',
    'Building Blocks': 'Toys',
    'Running Shoes': 'Sports',
    'Yoga Mat': 'Sports',
    'Basketball': 'Sports',
    'Novel': 'Books',
    'Cookbook': 'Books',
    'Art Book': 'Books',
    'Lipstick': 'Beauty',
    'Shampoo': 'Beauty',
    'Perfume': 'Beauty',
    'Milk': 'Grocery',
    'Bread': 'Grocery',
    'Fresh Vegetables': 'Grocery',
    # Add more products as needed
}


def generate_fake_data():
    num_records = random.randint(1, 5)
    data = []
    for _ in range(num_records):
        store_name = fake.company()
        store_address = fake.address()

        # Randomly select a product from the dictionary
        product_name, product_category = random.choice(list(PRODUCT_DICT.items()))

        product_price = fake.random.uniform(1.0, 100.0)

        data.append({
            'StoreName': store_name,
            'StoreAddress': store_address,
            'ProductName': product_name,
            'ProductCategory': product_category,
            'ProductPrice': product_price
        })
    return data


def generate_csv(file_path, data):
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['StoreName', 'StoreAddress', 'ProductName', 'ProductCategory', 'ProductPrice']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data
        writer.writerows(data)


def main():
    desktop_path = r'C:\Users\paras\OneDrive\Desktop\Startup\manualLoads\\'
    while True:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        file_name = f'new_product_{timestamp}.csv'
        file_path = desktop_path + file_name
        fake_data = generate_fake_data()
        generate_csv(file_path, fake_data)
        print(f"CSV generated at: {file_path}")
        time.sleep(5)  # Sleep for 60 seconds (1 minute)


if __name__ == "__main__":
    main()
