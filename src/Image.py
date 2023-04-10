from PIL import Image, ImageDraw, ImageFont

class TextToImage:
    def __init__(self):
        pass

    def merge_number_images(self, number): 
        # Abre las imágenes
        image1 = Image.open("img/numbers/"+number[0]+".png")
        image2 = Image.open("img/numbers/"+number[1]+".png")
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
        output_path  = "resultado.png"
        imagen_final.save(output_path)
        return output_path 
        

        
       

    def merge_text_to_image(self, src_input, src_output):
        image = imgae.open("")