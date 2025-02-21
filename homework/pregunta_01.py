# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import pandas as pd
import matplotlib.pyplot as plt


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
   
    # Crear carpeta docs si no existe
    if not os.path.exists("docs"):
        os.makedirs("docs")
    
    # Leer el archivo CSV
    data = pd.read_csv("files/input/shipping-data.csv")
    
    # Gráfico de barras para Warehouse_block
    plt.figure(figsize=(6, 4))
    data["Warehouse_block"].value_counts().plot(kind="bar", color="skyblue")
    plt.title("Distribución de Warehouse Block")
    plt.xlabel("Warehouse Block")
    plt.ylabel("Cantidad")
    plt.savefig("docs/shipping_per_warehouse.png")
    plt.close()

    # Gráfico de barras para Mode_of_Shipment
    plt.figure(figsize=(6, 4))
    data["Mode_of_Shipment"].value_counts().plot(kind="bar", color="lightcoral")
    plt.title("Distribución de Mode of Shipment")
    plt.xlabel("Modo de Envío")
    plt.ylabel("Cantidad")
    plt.savefig("docs/mode_of_shipment.png")
    plt.close()

    # Histograma para Customer_rating
    plt.figure(figsize=(6, 4))
    data["Customer_rating"].hist(bins=5, color="gold", edgecolor="black")
    plt.title("Distribución de Customer Rating")
    plt.xlabel("Rating")
    plt.ylabel("Frecuencia")
    plt.savefig("docs/average_customer_rating.png")
    plt.close()

    # Histograma para Weight_in_gms
    plt.figure(figsize=(6, 4))
    data["Weight_in_gms"].hist(bins=30, color="purple", edgecolor="black")
    plt.title("Distribución de Weight in gms")
    plt.xlabel("Peso (g)")
    plt.ylabel("Frecuencia")
    plt.savefig("docs/weight_distribution.png")
    plt.close()
    
    # Crear HTML
    html_content = """
    <!DOCTYPE html>
    <html lang='es'>
    <head>
        <meta charset='UTF-8'>
        <meta name='viewport' content='width=device-width, initial-scale=1.0'>
        <title>Dashboard de Envíos</title>
    </head>
    <body>
        <h1>Dashboard de Envíos</h1>
        <h2>Distribución de Warehouse Block</h2>
        <img src='shipping_per_warehouse.png' alt='Warehouse Block'>

        <h2>Distribución de Mode of Shipment</h2>
        <img src='mode_of_shipment.png' alt='Mode of Shipment'>

        <h2>Distribución de Customer Rating</h2>
        <img src='average_customer_rating.png' alt='Customer Rating'>

        <h2>Distribución de Weight in gms</h2>
        <img src='weight_distribution.png' alt='Weight in gms'>
    </body>
    </html>
    """
    
    # Guardar HTML en docs
    with open("docs/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("Dashboard generado en docs/index.html")

# Ejecutar la función
pregunta_01()

