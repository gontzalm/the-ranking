from src.app import app
from config import PORT
import src.controllers.students_controller
import src.controllers.labs_controller

app.run("0.0.0.0", PORT, debug=True, load_dotenv=False)