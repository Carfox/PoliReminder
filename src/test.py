from PIL import Image, ImageDraw
w = 1280
h = 720
# Crear una imagen en blanco de 300x300 pixeles
img = Image.new("RGB", (w, h), "white")

# Crear un objeto ImageDraw
draw = ImageDraw.Draw(img)

# Dibujar un rectángulo amarillo con bordes redondos de 10 pixeles de radio
draw.rounded_rectangle([(0.10*w, 0.10*h),(0.9*w, 0.9*h)], 10, "yellow", "black")

# Mostrar la imagen
img.show()