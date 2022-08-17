import pandas as pd
import numpy as np
from pathlib import Path
import csv
import os


def Delimitador (path):
    data = open(path, "r", encoding="latin_1").read()
    delimiter = csv.Sniffer().sniff(data).delimiter
    return delimiter  

def archivos (path):
    #cantidad = Path().iterdir()
    archs = os.walk(path)
    for i,e,archivo in archs:
        return archivo

def DataFrame (path, nombre):
    datas = archivos(path)
    lista = []
    for i in datas:
        direc = path + "/" + i
        deli = Delimitador(direc)
        if i == "energyco2.csv" and nombre == "energy":
            df_energy = pd.read_csv(direc,delimiter=deli,encoding="latin_1", index_col=False)
            lista.append(df_energy)
            return df_energy
        if i == "global_power_plant_database.csv" and nombre == "global":
            df_global = pd.read_csv(direc,delimiter=",", encoding="latin1")
            lista.append(df_global)
            return df_global
        if i == "owid-energy-consumption-source.csv" and nombre == "owid1":
            df_owid1 = pd.read_csv(direc,delimiter=deli,encoding="latin_1")
            lista.append(df_owid1)
            return df_owid1
        if i == "owid-energy-datadiccionary.csv" and nombre == "owid2":
            df_owi2 = pd.read_csv(direc,delimiter=deli,encoding="latin_1")
            lista.append(df_owi2)
            return df_owi2

if __name__ == "__main__":
    directorio = os.getcwd()
    df_energy = DataFrame(directorio, "energy")
    df_global = DataFrame(directorio, "global")
    df_owid1 = DataFrame(directorio, "owid1")
    df_owid2 = DataFrame(directorio, "owid2")