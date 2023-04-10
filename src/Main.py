from Numero import Numero
from Image import TextToImage

def main():
    img = TextToImage()
    obj = Numero()
    number = obj.numero_a_texto_digito(input())
    src_img = img.merge_number_images(number)
    print(f"{src_img}")
    

if __name__ == "__main__":
    main()