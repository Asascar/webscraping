import time
from openpyxl import load_workbook

def epocascrapping(item,ws,browser):
  base_url = f'https://epoca.globo.com/busca/?q={item}'
  pesq = f'{item}'
  browser.get(base_url)
  time.sleep(1)

  try:
    main_news_container = browser.find_element_by_class_name('resultado_da_busca')
    text_sections = main_news_container.find_elements_by_xpath("//a[@href]")
  except:
    return

  for elem in text_sections:
      if pesq in elem.text:
          valores = [
             (elem.text,elem.get_attribute("href"),'EPOCA',),
          ]
          for linha in valores:
            ws.append(linha)




