import selenium.webdriver as webdriver
from time import sleep
import os
import csv
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://ge.globo.com/futebol/futebol-internacional/futebol-ingles/")
sleep(10) #aberto durante 10 segundos

lista_times = driver.find_elements(By.XPATH, "//strong[@class='classificacao__equipes classificacao__equipes--nome']")
lista_pontos = driver.find_elements(By.XPATH, "//td[@class='classificacao__pontos classificacao__pontos--ponto']")
classificacoes = driver.find_elements(By.XPATH, "//td[@class='classificacao__pontos']")

estatisticas_por_time = [classificacoes[i:i+8] for i in range(0, len(classificacoes), 8)]

with open('classificacao.csv', 'w', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Time", "Pontos", "Jogos", "Vitórias", "Empates", "Derrotas", "Gols pró", "Gols contra", "Saldo de gols", "Aproveitamento"])

    for i in range(len(lista_times)):
        time = lista_times[i].text.strip()
        pontos = lista_pontos[i].text.strip()
        estatisticas = [estat.text for estat in estatisticas_por_time[i]]
        writer.writerow(([time, pontos]) + estatisticas)

input('Toque em qualquer tecla para encerrar')

import pandas as pd

arquivo = pd.read_csv("classificacao.csv")