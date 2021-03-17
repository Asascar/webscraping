import time
from openpyxl import load_workbook

def g1scrapping(item,ws,browser):
  base_url = f'https://g1.globo.com/busca/?q={item}'
  pesq = f'{item}'
  pesqmais = pesq.replace(" ","+")
  pesqtraco = pesq.replace(" ","-")
  browser.get(base_url)
  time.sleep(1)

  try:
    main_news_container = browser.find_element_by_class_name('results__list')
    text_sections = main_news_container.find_elements_by_xpath("//a[@href]")
  except:
    return

  for elem in text_sections:
      if "%2F2021%" in elem.get_attribute("href"):
        if (f'{pesqmais}') or (f'{pesqtraco}') in elem.get_attribute("href"):
            valores = [
              (elem.text,elem.get_attribute("href"),'G1'),
            ]
            for linha in valores:
              ws.append(linha)





