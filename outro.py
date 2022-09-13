from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import os


timer = 18
cmd = 'shutdown /p '

driver = wd.Chrome(executable_path= '..\Desktop\chromedriver.exe')

driver.get('https://www.youtube.com/watch?v=FX9eEhoRZhY')

play_button = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[27]/div[2]/div[1]/button')
play_button.click()
wd.Chrome.minimize_window(driver)


for i in range(timer):
    time.sleep(1)
    timer = timer - 1
    print("{} seconds left ".format(timer))

if timer == 0:
    print("Byeee!!")
    time.sleep(1)
    os.system(cmd)