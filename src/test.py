from PIL import Image, ImageDraw, ImageFont
import os
image1 = Image.open("img/numbers/one.png")
image2 = Image.open("img/numbers/two.png")

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
        #route_output_img = "answer"
imagen_final.save(os.path.basename("resultado.png"))