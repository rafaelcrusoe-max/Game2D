valor = 2000

class IDesconto:
    def calcular(self, valor):
        raise NotImplementedError

class DescontoNormal(IDesconto):
    def calcular(self, valor):
        return valor * 0.1
    
    def validar_normal(self):
        return True
    
class DescontoPremium(IDesconto):
    def calcular(self, valor):
        return valor * 0.2
    
    def validar_premium(self):
        return True
    
class DescontoVip(IDesconto):
    def calcular(self, valor):
        return valor * 0.3
    
    def validar_vip(self):
        return True
    
def aplicar_desconto(desconto: IDesconto, valor):
    return desconto.calcular(valor)

print(aplicar_desconto(DescontoVip(), valor))

print(DescontoVip().validar_vip())