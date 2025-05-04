# Orientação a objetos
class Veiculo:
    def movimentar(self):
        print(f'sou um veiculo e me desloco')

    def __init__(self,fabricante,modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.num_registro = None

if __name__ == '__main__':
    meu_veiculo = Veiculo('GM','Cadilace')
    meu_veiculo.movimentar()
    print(meu_veiculo.fabricante,meu_veiculo.modelo)