# Made by Lance Uy to automate CCAC Church google registration form
# Using python, selenium webdriver, pyautogui
# Dec 2021

from selenium import webdriver
from pyautogui import write
import time

mails = ['edwardlanceuy@gmail.com', 'another@gmail.com']
names = ['Lance Uy', 'test']


def fill_form(people, name):
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito") # Optional

    browser = webdriver.Chrome(executable_path="C:\\Users\\edwar\\Downloads\\chromedriver.exe", options=option)
    # Test form
    #browser.get('https://forms.gle/X6h3Abr8xEfQdauT6')
    # Real form
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLSeZoNAi3inJdEBFsDhAyhNpVaVVFPcItjRSkIkEmibsnGgBIQ/viewform')

    # -------------- PAGE 1 --------------
    # Locate all textboxes, buttons, dropdowns within page and need to
    # index which one you want
    textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    dropdown = browser.find_elements_by_class_name("quantumWizMenuPaperselectOption")

    textboxes[0].send_keys(mails[people])
    buttons[0].click()
    dropdown[0].click()

    # Select English Service
    time.sleep(0.5)
    for i in range(1): # Range changes based on which option you want
        write(['down'])
    write(['enter'])

    # Next page
    #time.sleep(0.5)
    submit = browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    submit.click()
    time.sleep(0.5)

    # -------------- PAGE 2 --------------
    # Select 1 person
    dropdown = browser.find_elements_by_class_name("quantumWizMenuPaperselectOption")
    dropdown[0].click()
    time.sleep(0.5)
    for i in range(1):
        write(['down'])
    write(['enter'])

    # Enter name of person
    time.sleep(0.5)
    textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
    textboxes[1].send_keys(names[name])
    time.sleep(0.5)

    # Next page
    submit = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    submit[1].click()
    time.sleep(0.5)

    # -------------- PAGE 3 --------------
    # No to all covid screenings
    buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    buttons[1].click()
    buttons[3].click()
    buttons[5].click()
    time.sleep(0.5)

    # Submit
    submit = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    submit[1].click()

    # End all browser windows and ends driver's session/process
    browser.quit()


if __name__ == '__main__':
    fill_form(0,0)
    #fill_form(1,1)

