from pymongo import MongoClient
from urllib.parse import quote_plus

try:
    # Replace with your actual connection string
    username = "Lokesh"
    password = "Lokesh@2605"
    # Encode username and password
    encoded_username = quote_plus(username)
    encoded_password = quote_plus(password)
    # Construct the connection string
    connection_string = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.xjqpt5k.mongodb.net/reelgen?retryWrites=true&w=majority"
    client = MongoClient(connection_string)
    db = client['reelgen']
    print("Connection Successful!")
    # List collections in the database
    print("Collections:", db.list_collection_names())
except Exception as e:
    print("An error occurred:", e)
