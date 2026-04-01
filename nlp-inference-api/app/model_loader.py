import os
from huggingface_hub import snapshot_download, login
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
from app.config import MODEL_REPO, MODEL_DIR

# Función para descargar el modelo desde HuggingFace Hub
def download_model():
    # Verificar si el modelo ya existe localmente antes de descargarlo
    if not os.path.exists(MODEL_DIR):
        print("Descargando modelo de HuggingFace...")
        snapshot_download(
            repo_id=MODEL_REPO,
            local_dir=MODEL_DIR,
            local_dir_use_symlinks=False,
            resume_download=True
        )
        print("Model descargado.")
    else:
        print("Model ya existe.")

# Función para cargar el modelo desde la carpeta local
def load_model():
    print("Cargando modelo...")
    # Cargar el modelo y el tokenizador desde la carpeta local
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, local_files_only=True)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR, local_files_only=True)
    # Crear el pipeline de clasificación de texto utilizando el modelo y el tokenizador cargados
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)
    print("Model loaded.")
    return classifier