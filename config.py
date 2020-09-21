import dotenv
import os

dotenv.load_dotenv()

PORT = os.getenv("PORT")
DBURL = os.getenv("DBURL")