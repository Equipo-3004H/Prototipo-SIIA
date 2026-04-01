from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.model_loader import download_model, load_model
from app.schemas import DatosEntrada, DatosSalida
from app.inference import predict

# Carga del modelo al iniciar la aplicación utilizando lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Descargar el modelo
    download_model()
    # Asignar el modelo a la variable global 
    app.state.classifier = load_model()
    # Iniciar la aplicación
    yield

# Crear instancia de FastAPI con lifespan para cargar el modelo al iniciar la aplicación
app = FastAPI(lifespan=lifespan)

# Endpoint de prueba
@app.get("/")
def root():
    return {"status": "API running"}

# Endpoint para verificar se ha cargado correctamente el modelo al iniciar la aplicación
@app.get("/health")
def health():
    if hasattr(app.state, "classifier"):
        return {"status": "healthy", "model": "loaded"}
    return {"status": "loading"}

# Endpoint de Inferencia
@app.post("/sentiment-analysis/")
async def sentiment_analysis(data: DatosEntrada):
    # Obtener el clasificador cargado al iniciar el API
    classifier = app.state.classifier
    # Realizar la predicción utilizando el modelo cargado
    lexical_score = predict(classifier, data.text)
    # Contruir el JSON de respuesta
    result = DatosSalida(
        session_id=data.session_id,
        segment_id=data.segment_id,
        text=data.text,
        start_time=data.start_time,
        end_time=data.end_time,
        lexical_score=lexical_score)    
    return result