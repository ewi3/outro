from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import time
import os

cmd = 'shutdown /p '
usr_input = input("Do you want to add a set time for the timer? Y/N")
if usr_input == 'Y':
    timer = int(input("Then, how much time do you want? (seconds)"))


def init_of_webdriver():
    path = wd.Chrome(executable_path='.\chromedriver.exe')
    path.get('https://www.youtube.com/watch?v=FX9eEhoRZhY')
    play_button = path.find_element(By.XPATH, '//*[@id="movie_player"]/div[28]/div[2]/div[1]/button')
    play_button.click()
    wd.Chrome.minimize_window(path)
    # this function starts the webDriver


def default_time(path):
    if usr_input == "N":
        duration = path.find_elements(By.XPATH, "//span[@class='ytp-time-duration']")[0]
        print('Video Length = ' + duration.text)
        duration_replaced = duration.text.replace(":", "")
        timer = (int(duration_replaced) / 600) * 4 + 12
    # this function sets a default time by getting the duration of the video


def main(timer):
    init_of_webdriver()

    for i in range(int(timer)):
        time.sleep(1)
        timer = timer - 1
        print(f'{timer} seconds left ')
    # this part prints the time by getting the timer of default_time()

    if timer >= 0:
        print("Byeee!!")
        time.sleep(1)
        os.system(cmd)
    # this part shuts down the computer when the timer is 0 or almost 0


if __name__ == '__main__':
    main(timer)
