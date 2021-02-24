import glob
from PyPDF2 import PdfFileReader
pdf_dir = "C:/Users/gabri/Desktop/py4e/Contas EDP AAP/Leitor PDF/Faturas"
pdf_files = glob.glob("%s/*.pdf" % pdf_dir)
path = pdf_files

for file in pdf_files:

  with open(file, 'rb') as f:

      pdf = PdfFileReader(f)
      page = pdf.getPage(1)
      text = page.extractText()
      text = text.split()

      for word in text:
              if word.endswith('Créditos'):
                  word = word.replace("Créditos","")
                  word = word.replace("mês","")
                  word = word.replace("kWh","")
                  energia_injetada = word
                  print('Energia injetada: ', energia_injetada)

              elif word.endswith('Saldo'):
                  word = word.replace("mês","")
                  word = word.replace("Saldo","")
                  word = word.replace("Participação","")
                  word = word.replace("kWh","")
                  energia_injetada = word
                  if 'Recebido' not in word:
                   print('Energia injetada: ', energia_injetada)

              elif word.endswith('Saldo'):
                  word = word.replace("Recebido","")
                  word = word.replace("kWhSaldo","")
                  recebidos = word
                  print(recebidos)

              elif word.endswith('Participação'):
                  word = word.replace("mês","")
                  word = word.replace("Saldo","")
                  word = word.replace("Participação","")
                  word = word.replace("kWh","")
                  energia_injetada = word
                  print('Saldo Atualizado: ', energia_injetada)

              elif word.startswith('Verde'):
                 print('Bandeira verde')

              elif word.startswith('Vermelha:'):
                 print('Bandeira vermelha')

              elif word.startswith('Amarela'):
                 print('Bandeira Amarela: ')

              elif  word.startswith('('):
                  word = word.replace("(","")
                  data_inicial = word
                  print('Data inicial: ',data_inicial)

              elif word.endswith(')Nº'):
                  word = word.replace("Nº","")
                  data_final1 = word
                  print("Data Final: ", data_final1)

              elif word.endswith(")Agradecemos"):
                  word = word.replace(")Agradecemos","")
                  data_final = word
                  print('Data final: ',data_final)

              elif word.startswith('Saldo'):
                  word = word.replace("Saldo","")
                  participacao_saldo = word
                  print('Participação no Saldo: ', participacao_saldo)


                  print('\n\n')

              else: continue



if __name__ == '__main__' :
    print('ok')
