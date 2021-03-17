import time
from openpyxl import load_workbook

def cnnscrapping(item,ws,browser):
  base_url = f'https://www.cnnbrasil.com.br/search?q={item}'
  pesq = f'{item}'
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






