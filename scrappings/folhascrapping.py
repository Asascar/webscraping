import time
from openpyxl import load_workbook
from openpyxl.descriptors import MinMax, Sequence
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def folhascrapping(item,wb,browser):
  try:
    ws = wb[item]
  except:
    wb.create_sheet(item)
    ws = wb[item]
    
  base_url = f'https://search.folha.uol.com.br/?q={item}&site=todos'
  pesq = f'{item}'
  browser.get(base_url)
  time.sleep(1)
  
  try:
    text_sections = browser.find_elements_by_xpath("//a[@href]")
  except:
    return

  for elem in text_sections:
    try:
        if "/2021/" in elem.get_attribute("href"):
          if pesq in elem.text:
              print(elem.get_attribute("href"))
              print(elem.text)
              valores = [
                (elem.text,elem.get_attribute("href"),'FOLHA'),
              ]
              for linha in valores:
                ws.append(linha)
    except:
      continue






