from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

############################
#### Endpoint "/items" #####
############################
# Devuelve el numero introducido, y la cadena introducida (literalmente, sin cambios)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

############################
#### Endpoint "/calcular-longitud" #####
############################
# PARAMETRO ================> RESPUESTA
# Ejemplo "hola" => {"cadena": "hola", "longitud": 4, "vocales": 2}
# Ejemplo "estamosenclasededam" => {"cadena": "estamosenclasededam", "longitud": 19, "vocales": 7}
@app.get("/calcular-longitud/{cadena}")
def read_item(cadena: str):
    num_vocales = sum(1 for char in cadena if char.lower() in "aeiou")
    return {"cadena": cadena, "longitud": len(cadena), "vocales": num_vocales}