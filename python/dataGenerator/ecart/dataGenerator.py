import psycopg2
import threading
import time
import random
import hashlib
from faker import Faker

speed = 150
conn = psycopg2.connect(
    database="pinnacledb",
    user="postgres",
    host="ecart-db-1",
    port="5432",
    password="9473"
)
fake = Faker()

def generateCustomer(speed=speed):
    choices = [1, 2, 3]
    n = random.choice(choices)
    print("Random value taken to generate customer is", n, "It will sleep for", (600 * n) / speed, "Speed is ", speed)
    time.sleep((600 * n) / speed)

    custID = 'C' + str(int(time.time()))[-8:]
    custName = fake.name()
    custAdd = fake.address()

    cursor = conn.cursor()
    postgres_insert_query = """INSERT INTO ECART.CUSTOMER (CUSTID, CUSTNAME, CUSTADD) VALUES (%s,%s,%s)"""
    record_to_insert = (custID, custName, custAdd)
    cursor.execute(postgres_insert_query, record_to_insert)
    conn.commit()

    count = cursor.rowcount
    print(count, "Record inserted successfully into customer table")

    return

def small_hash(input_string):
    # Use SHA-256 hash function
    hash_object = hashlib.sha256(input_string.encode())
    hex_dig = hash_object.hexdigest()
    # Take a subset of the hash (first 8 characters)
    return hex_dig[:10]

def generateProductsAndStores():
    choices = [2.5, 3.5, 4.5]
    n = random.choice(choices)
    print("Random value taken to generate products and stores is", n, "It will sleep for", (300 * n) / speed)
    time.sleep((300 * n) / speed)

    adjectives = ["Compact", "Portable", "Economical", "High-Power", "Durable", "Advanced", "Professional",
                  "Industrial", "Lightweight", "Heavy-Duty", "Superior", "Quality", "Easy-to-Use", "Premium",
                  "Innovative", "Reliable", "Sleek", "Multi-Functional", "Wireless", "Smart", "Fast", "Efficient",
                  "High-Capacity", "Ultra", "Precision", "Affordable", "Versatile", "Luxurious", "Comfortable",
                  "Rugged"]
    nouns = ["Drill", "Printer", "Mower", "Oven", "Headphones", "Camera", "Laptop", "Monitor", "Keyboard", "Watch",
             "Speaker", "Router", "Mouse", "Charger", "Smartphone", "Bag", "Tablet", "Adapter", "Microphone",
             "Projector", "Scanner", "Controller", "Flashlight", "Blender", "Coffee-Maker", "Fan", "Air-Purifier",
             "Toolset", "Hair-Dryer", "Tripod"]
    prefixes = ["Tech", "Digital", "Gadget", "Innovative", "Smart", "Global", "Worldwide", "Pro", "Quality", "Future",
                "Creative", "Eco", "Express", "Quick", "Mega", "Ultra", "Super", "Hyper", "Fantastic", "Amazing"]
    infixes = ["&", "and", "N'", "or", "plus", "versus"]
    suffixes = ["Store", "Hub", "Depot", "Market", "Place", "Plaza", "Mall", "Center", "Outlet", "World", "Galaxy",
                "Universe", "Domain", "Spot", "Point", "Zone", "Area", "Quarter", "Field", "Territory"]

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    prefix = random.choice(prefixes)
    infix = random.choice(infixes)
    suffix = random.choice(suffixes)
    storename = prefix + " " + infix + " " + suffix

    productID = int(str(int(time.time()))[4:10])
    productName = adjective + " " + noun
    productCategory = noun
    storeid = small_hash(storename)
    storeadd = fake.address()

    cursor = conn.cursor()
    postgres_insert_query_product_info = """INSERT INTO ECART.PRODUCTINFO (PRODUCTID, PRODUCTNAME, PRODCAT, STOREID) VALUES (%s,%s,%s,%s)"""
    record_to_insert_product_info = (productID, productName, productCategory, storeid)
    postgres_insert_query_store_info = """INSERT INTO ECART.STOREINFO (STOREID, STORENAME, STOREADD) VALUES (%s,%s,%s)"""
    record_to_insert_store_info = (storeid, storename, storeadd)

    cursor.execute(postgres_insert_query_product_info, record_to_insert_product_info)
    cursor.execute(postgres_insert_query_store_info, record_to_insert_store_info)
    conn.commit()

    count = cursor.rowcount
    print(count, "Record inserted successfully into product and store table each")

    return

def generateOrderFact():
    choices = [0.5, 1.5, 1]
    n = random.choice(choices)
    print("Random value taken is", n, "It will sleep for", (100 * n / speed), "seconds")
    time.sleep(100 * n / speed)

    postgreSQL_select_Query_cust = "SELECT CUSTID FROM ECART.CUSTOMER ORDER BY RANDOM() LIMIT 1"
    postgreSQL_select_Query_product = "SELECT PRODUCTID FROM ECART.PRODUCTINFO ORDER BY RANDOM() LIMIT 1"

    cursor = conn.cursor()
    cursor.execute(postgreSQL_select_Query_cust)
    custidrow = cursor.fetchall()

    cursor.execute(postgreSQL_select_Query_product)
    productidrow = cursor.fetchall()
    try:
        custID = custidrow[0][0]
        productid = productidrow[0][0]

        postgres_insert_query = """INSERT INTO ECART.FACT_ORDER (CUSTID, PRODUCTID) VALUES (%s,%s)"""
        record_to_insert = (custID, productid)

        cursor.execute(postgres_insert_query, record_to_insert)
        conn.commit()

        count = cursor.rowcount
        print(count, "Record inserted successfully into fact table")
    except Exception as e:
        # Code to handle other exceptions
        print("Looks like no data is present in customer or product table for now", str(e))
    finally:
        # Code that will be executed regardless of whether an exception occurred
        print("")

    return

# generateCustomer(speed)
# generateProductsAndStores()
# generateOrderFact()
#conn.close()
