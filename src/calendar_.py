import requests
import bs4 as bs
import os
import pdfplumber
import fecha

URL="https://www.epn.edu.ec/admision/calendario-academico-propedeutico-nivelacion"

def exist_pdf():
    path = "../pdf/"
    for root, dirs, files in os.walk(path):
        for _file in files:
            if _file != None: 
                return True  

def download_calendars():
    #Verificar si la carpeta pdf existe, si no la crea
    pdf_path = os.path.abspath("../pdf")
    if not os.path.exists(pdf_path):
        os.mkdir(pdf_path)
    #Web scraping a la pagina de la epn
    if requests.get(URL).status_code == 200:
        data = requests.get(URL).content
        soup = bs.BeautifulSoup(data, "html.parser")
        calendars = soup.find_all('a',{'class': 'wpb_button_a'})
        calendar_names = []

        for calendar in calendars:
                calendar_names.append(calendar['title'])
                #Handling file in python, low level
                path = f"{os.path.join(pdf_path,calendar['title'])}.pdf"
                with open(path,'wb') as file:
                    content_object = requests.get(calendar['href']).content
                    file.write(content_object)
                    file.close()
                    #Se Comprueba que los PDF's no esten corruptos, si el caso se procede a eliminar
                    try: 
                        pdfplumber.open(path)
                        print(f"{calendar['title']} se ha descargado correctamente")
                        print("\n")
                    except Exception as e:
                        print(f"{calendar['title']} es corrupto {e}")
                        os.remove(path)
    return calendar_names

# def check_pdf():
#     path = "../pdf/"
#     pdf_path = os.path.abspath("../pdf")
#     for root, dirs, files in os.walk(path):
#             for _file in files:
#                     try:
#                         with pdfplumber.open(f"{os.path.join(pdf_path,_file)}") as pdf:
#                             print(f"{_file} tiene {pdf.pages}")
#                             print("\n")
#                     except Exception as e:
#                         print(f"{_file} es corrupto {e}")
#                         os.remove(f"{os.path.join(pdf_path,_file)}")



def read_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_calendar = pdf.pages[0].extract_text()
        lines_text = first_calendar.split("\n")
    important_dates = []
    for lines in lines_text:
        if lines.startswith("Inicio Período Académico") or lines.startswith("Inicio Período Académico"):
            # fecha en español con formato d de m de aaaa
            important_dates.append(lines)
        elif lines.startswith("Inicio de Clases"):
            important_dates.append(lines)
        elif lines.startswith("Último día de clases"):
            important_dates.append(lines )
        elif lines.startswith("Cierre del SAEw"):
            important_dates.append(lines )
        elif lines.startswith("Fin de Periodo Académico"):
            important_dates.append(lines )
        elif lines.startswith("Matrículas Extraordinarias (ME)"):
            important_dates.append(lines)

    return important_dates

def main():    
    if(exist_pdf() == None):
        print("Funciona y descarga")
        download_calendars()
    else: 
        print(read_pdf(os.path.abspath(r"../pdf/CALENDARIO ACADÉMICO 2023 A.pdf")))

            


if __name__ == "__main__":
    main()