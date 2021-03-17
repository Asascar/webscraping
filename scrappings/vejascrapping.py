import time
from openpyxl import load_workbook

def vejascrapping(item,ws,browser):
  base_url = f'https://veja.abril.com.br/?s={item}&orderby=date'
  pesq = f'{item}'
  browser.get(base_url)
  time.sleep(1)
  
  try:
    main_news_container = browser.find_element_by_id("infinite-list")
    text_sections = main_news_container.find_elements_by_xpath("//a[@href]")
  except:
    return

  for elem in text_sections:
    try:
      if elem.text != "":
        if pesq in elem.text:
            if elem.text == "":
              break
            valores = [
              (elem.text,elem.get_attribute("href"),'VEJA'),
            ]
            for linha in valores:
              ws.append(linha)
    except:
     continue





