import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, dotenv_values 

# Load the environment variables from the .env file
load_dotenv()

# Get the MongoDB URI from environment variables
uri = os.getenv("MONGO_URI")

if not uri:
    raise Exception("MONGO_URI not found in environment variables")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

