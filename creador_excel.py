import pandas as pd

#Dataframe es la informacion basica con el nombre de las piezas y centimetros para poder armar la tabla

data = {
    "Piezas:": ["Pata", "Tablero", "Puerta", "Estante", "Panel lateral"],
    "Centímetros": [40, 60, 80, 90, 50],
}

df = pd.DataFrame(data)

#Guardar el DataFrame en un archivo Excel

df.to_excel("muebles_medidas.xlsx", index=False)