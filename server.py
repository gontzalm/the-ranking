from src.app import app
from config import PORT
import src.meme_controller

app.run("0.0.0.0", PORT, debug=True, load_dotenv=False)