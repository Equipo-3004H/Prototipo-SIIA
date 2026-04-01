def predict(classifier, text):
    # Realizar la predicción utilizando el pipeline de clasificación de texto
    resultado = classifier(text)[0]
    # Obtener el score y la etiqueta de la predicción
    score = resultado['score']
    label = resultado['label']
    # Convertir el lexical_score al valor positivo  
    if label == "POSITIVE":
        lexical_score = score
    # Convertir el lexical_score del valor negativo al valor positivo
    else:
        lexical_score = 1 - score
    return lexical_score