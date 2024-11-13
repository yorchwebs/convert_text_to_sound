import json
import os


current_directory = os.getcwd()
ruta_archivo = current_directory + "/nombre_archivo.json"


with open(ruta_archivo, "r") as f:
    datos = json.load(f)


def load_data():

    verbs_list = []
    for item in datos:
        if "key" in item:
            verbs_list.append(item["value"])

    return verbs_list
