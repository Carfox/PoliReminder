from num2words import num2words

class Numero:
    def __init__(self):
        pass
        
    def numero_a_texto_digito (self, numero):
        text_list = []
        if(int(numero)<10):
            text_list.append(num2words("0"))
            text_list.append(num2words(int(numero)))

        for i in range(0,len(numero)):
            text_list.append(num2words(int(numero[i])))
        return  text_list
