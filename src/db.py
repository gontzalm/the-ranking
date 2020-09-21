from src.config import DBURL
from src.vpymongo import MongoClient

client = MongoClient(DBURL)
db = client.get_database()