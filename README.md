# Proceso ETL con Python desde API CoinMarketCap y carga de datos en una base PostgreSQL

## **Conexión a la API**
En el script [coinmarketcap.py](https://github.com/Arnold-Acuna-Pestana/challenge_metafar/blob/main/coinmarketcap.py) está la parte correspondiente a como se hace la conexión con la API, seteando los parámetros y
endpoints. 

## **Creación de Base de Datos**
En el script [create_table.py](https://github.com/Arnold-Acuna-Pestana/challenge_metafar/blob/main/create_table.py) está la parte correspondiente a como se definió el esquema de la base de datos: campos, pk, tipos
de datos.
## **Proceso ETL**
En el script [coinmarketcap.py](https://github.com/Arnold-Acuna-Pestana/challenge_metafar/blob/main/coinmarketcap.py) está la parte correspondiente a la transformación de los datos, usando pandas para este proceso.

## **Automatización**
La automatización se hizo de manera local con cron ya que el proyecto se derrallo en WSL2.

## **Requerimientos**
En el archivo [requirements.txt](https://github.com/Arnold-Acuna-Pestana/challenge_metafar/blob/main/requirements.txt) están todos los paquete utilizados para ejecutar el proyecto.
