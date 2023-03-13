#!/usr/bin/env python
# coding: utf-8

# In[13]:


import time
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


# In[16]:


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://jill2023.github.io/Localisateur_Web/index.html")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,'//a[@href="index4.html"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//a[text()="Lien de Facebook"]').click()
#driver.find_element(By.XPATH,'//a[@href="https://www.facebook.com/search/top?q=%E8%92%99%E5%9F%8E%E4%B8%AD%E8%8F%AF%E8%AA%9E%E6%96%87%E5%AD%B8%E6%A0%A1"]').click()
time.sleep(3)
popup = driver.switch_to.window(driver.window_handles[-1])
try:
    popup.close()
except:
    pass
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,'//a[@href="index.html"]').click()
time.sleep(3)

#driver.find_element(By.XPATH,'//a[@href="page.html"]').click()
#time.sleep(3)
#driver.find_element(By.XPATH,'//a[@href="mailto:info@chineseschool-mtl.com"]').click()


#main_window_handle = driver.current_window_handle
#driver.switch_to.window(main_window_handle)

#driver.find_element(By.XPATH,'//a[@href="index.html"]').click()
#time.sleep(3)
driver.find_element(By.XPATH,'//a[text()="Cours"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//a[@href="https://chineseschool-mtl.com/fr/formulaire-dinscription/"]').click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.XPATH,'//button[@class="pum-close popmake-close "]').click()
time.sleep(2)

driver.find_element(By.NAME,"input_7").send_keys("Marie")
time.sleep(3)
driver.find_element(By.NAME,"input_8").send_keys("Dion")
time.sleep(3)
driver.find_element(By.NAME,"input_10").send_keys("5148889999")
time.sleep(3)
driver.find_element(By.NAME,"input_12").send_keys("abc@gmail.com")
time.sleep(3)
driver.find_element(By.NAME,"input_13.1").send_keys("123 Rue Liberal")
time.sleep(3)
driver.find_element(By.NAME,"input_13.3").send_keys("Laval")
time.sleep(3)
Select(driver.find_element(By.XPATH,'//select[@name="input_13.4"]')).select_by_visible_text("Québec")
time.sleep(3)
driver.find_element(By.NAME,"input_13.5").send_keys("J1K 4D5")
time.sleep(3)
driver.find_element(By.ID,"gform_next_button_1_4").click()
time.sleep(3)

driver.find_element(By.NAME,"input_15").send_keys("Julia")
time.sleep(3)
driver.find_element(By.NAME,"input_16").send_keys("Dion")
time.sleep(3)
Select(driver.find_element(By.XPATH,'//select[@id="input_1_17_3"]')).select_by_visible_text("2015")
time.sleep(3)
Select(driver.find_element(By.XPATH,'//select[@id="input_1_17_1"]')).select_by_visible_text("9")
time.sleep(3)
Select(driver.find_element(By.XPATH,'//select[@id="input_1_17_2"]')).select_by_visible_text("15")
time.sleep(3)
driver.find_element(By.ID,"gform_next_button_1_62").click()
time.sleep(3)

Select(driver.find_element(By.XPATH,'//select[@id="input_1_29"]')).select_by_visible_text("Session du Matin - Mandarin Simplifié - 3")
time.sleep(3)
driver.find_element(By.ID,"gform_next_button_1_30").click()
time.sleep(3)

Select(driver.find_element(By.XPATH,'//select[@id="input_1_45"]')).select_by_visible_text("Session du Midi - Chorale - Âge 8")
time.sleep(3)
driver.find_element(By.ID,"gform_next_button_1_50").click()
time.sleep(3)

Select(driver.find_element(By.XPATH,'//select[@id="input_1_57"]')).select_by_visible_text("Première Session de l'Après-Midi - Anglais - 3")
time.sleep(3)
driver.find_element(By.ID,"gform_next_button_1_63").click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH,'//a[@href="index.html"]').click()
time.sleep(3)
driver.close()


# In[ ]:





# In[ ]:




