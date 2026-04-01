from pydantic import BaseModel

# JSON de entrada 
class DatosEntrada(BaseModel):
    session_id: str
    segment_id: int
    text: str
    start_time: float
    end_time: float

# JSON de salida 
class DatosSalida(BaseModel):
    session_id: str
    segment_id: int
    text: str
    start_time: float
    end_time: float
    lexical_score: float
