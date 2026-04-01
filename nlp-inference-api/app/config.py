from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Carpeta raiz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Repositorio del modelo en HuggingFace 
MODEL_REPO = "sarahi-rdz/fine-tuning"

# Carpeta donde se guarda el modelo
MODEL_DIR = BASE_DIR / "best_model"