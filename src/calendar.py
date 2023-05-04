import requests
import bs4 as bs
import os
import pdfplumber

URL="https://www.epn.edu.ec/admision/calendario-academico-propedeutico-nivelacion/"

def download_calendars():
    #Verificar si la carpeta pdf existe, si no la crae
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
            with open(f"{os.path.join(pdf_path,calendar['title'])}.pdf",'wb') as file:
                content_object = requests.get(calendar['href']).content
                file.write(content_object)
                file.close()
                check_pdf()
        
        #Comprobar que los pdf no esten corruptos, caso contrario se elimina. 
        check_pdf()
    
    return calendar_names

def check_pdf():
    path = "../pdf/"
    #os.startfile(path)
    pdf_path = os.path.abspath("../pdf")
    #archivo = os.path.join(pdf_path,_file)
    for root, dirs, files in os.walk(path):
            for _file in files:
                    try:
                        with pdfplumber.open(f"{os.path.join(pdf_path,_file)}") as pdf:
                            print(f"{_file} tiene {pdf.pages}")
                            print("\n")
                    except Exception as e:
                        print(f"{_file} es corrupto {e}")
                        os.remove(f"{os.path.join(pdf_path,_file)}")


def read_pdf(pdf_path):
    """ Lee fechas importantes y las retorna
    Args:
        pdf_path (_type_): _description_
    """
    with pdfplumber.open(pdf_path) as pdf:
        first_calendar = pdf.pages[0].extract_text()

        lines_text = first_calendar.split("\n")


    important_dates = []
    for linesines in lines_text:
        if lines.startswith("Inicio Período Académico") or lines.startswith("Inicio Período Académico"):
            important_dates.append(lines )
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
    

            