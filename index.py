from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

pesquisa = input("Qual bairro deseja pesquisar?: ")

driver = webdriver.Chrome()
driver.get('https://www.google.com.br/maps/preview')

sleep(10)

searchbox = driver.find_element(By.XPATH, "//input[@id='searchboxinput']")

searchbox.send_keys(pesquisa)

sleep(5)

botao_pesquisa = driver.find_element(By.XPATH,"//button[@id='searchbox-searchbutton']")

botao_pesquisa.click()

sleep(30)



