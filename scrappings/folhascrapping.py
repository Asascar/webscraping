import time
from openpyxl import load_workbook


def folhascrapping(item,ws,browser):   
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
              ano = elem.text.find('.2021')
              dia = ano -6
              ano = ano + 5
              data = elem.text[dia:ano]
              data = data.replace('.', '-')
              valores = [
                (elem.text,elem.get_attribute("href"),'FOLHA', data),
              ]
              for linha in valores:
                ws.append(linha)
    except:
      continue






