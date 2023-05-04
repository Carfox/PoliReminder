from PIL import Image, ImageDraw, ImageFont
from numero import Numero
import os 
from num2words import num2words
import date

#Definir funcion de las fechas, 
#Definer una clase que grafica numeros 
#main bot insertar las 2 funciones y enviar las imanges
#poner un schedule para que se ejecute cada cierto tiempo deseado. 
NUMBER_PATH = os.path.relpath("resources/img/numbers")
FONT_PATH = os.path.relpath("resources/fonts")

class TextToImage(Image):
    def __init__(self):
        pass
    
    def create_canva(self, w,h,color):
        img = Image.new("RGB", (w,  h), "white")
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle([(0.10*w, 0.10*h),(0.9*w, 0.9*h)], 10, color, "black")
        path_image = "canva.png"
        img.save(path_image)
        return path_image

    def text_merge_image(self, text, font_name, image_path):
        img = Image.open(image_path)
        fnt = ImageFont.truetype(os.path.join(FONT_PATH,font_name),80)
        d = ImageDraw.Draw(img)
        # draw multiline text
        d.multiline_text((50, 50), text, font=fnt, fill=(0, 0, 0))
        img.save("canva.png")
        
    def merge_number_images(self, number): 
        # Abre las imágenes
        img_number = []
        for i in number:
            img_number[i] = f"{os.path.join(NUMBER_PATH,num2words(number[i]))}.png"
            
        image1 = Image.open(number1,"r")
        image2 = Image.open(number2,"r")
        ancho1, alto1 = image1.size
        ancho2, alto2 = image2.size
        # Crea una nueva imagen con el tamaño adecuado para ambas imágenes juntas
        ancho_total = ancho1 + ancho2 + 10
        alto_total = max(alto1, alto2)
        imagen_final = Image.new("RGB", (ancho_total, alto_total), "white")
        # Combina las imágenes
        imagen_final.paste(image1, (0, 0))
        imagen_final.paste(image2, (ancho1+10, 0))
        # Guarda la imagen resultante
        out_path  = "resultado.png"
        imagen_final.save(out_path)
        return out_path 
        

    def numbers_to_canva(self,img_path, background_path):
        # background = Image.open(background_path)
        numbers_image = Image.open(img_path)
        # canva = Image.new("RGB", (canva.size), "white")
        # canva.paste(background,(0,0))'
        with Image.open(background_path) as bg:
            bg.paste(numbers_image, (400,400))
            
            bg.show()
        # canva.paste(numbers_image,())
        # canva.paste()

       

    def merge_text_to_image(self, src_input, src_output):
        image = imgae.open("")