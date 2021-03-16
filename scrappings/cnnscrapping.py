import time
from openpyxl import load_workbook
from openpyxl.descriptors import MinMax, Sequence
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def cnnscrapping(item,wb,browser):
  try:
    ws = wb[item]
  except:
    wb.create_sheet(item)
    ws = wb[item]
  base_url = f'https://www.cnnbrasil.com.br/search?q={item}'
  pesq = f'{item}'
  pesqmais = pesq.replace(" ","+")
  pesqtraco = pesq.replace(" ","-")
  

  browser.get(base_url)
  time.sleep(10)

  try:
    main_news_container = browser.find_element_by_class_name('results')
    text_sections = main_news_container.find_elements_by_xpath("//a[@title]")
  except:
    return
  
  for elem in text_sections:
    try:
        if "/2021/" in elem.get_attribute("href"):
          if pesq in elem.text:
              print(elem.get_attribute("href"))
              print(elem.text)
              if elem.text == "":
                break
              valores = [
                (elem.text,elem.get_attribute("href"),'CNN'),
              ]
              for linha in valores:
                ws.append(linha)
    except:
      continue






