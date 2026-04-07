valor = 2000

class Desconto:
    def calcular(self, valor):
        pass

class DescontoNormal(Desconto):
    def calcular(self, valor):
        return valor * 0.1
    
class DescontoPremium(Desconto):
    def calcular(self, valor):
        return valor * 0.2
    
class DescontoVip(Desconto):
    def calcular(self, valor):
        return valor * 0.3
    
def aplicar_desconto(desconto: Desconto, valor):
    return desconto.calcular(valor)

print(aplicar_desconto(DescontoVip(), valor))