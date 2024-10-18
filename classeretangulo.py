class retangulo:
  def __init__(self, largura, altura):
    self.largura = largura
    self.altura = altura

    # metodo para mudaro valor do lado 
    def mudar_lado(self,largura, altura):
      self.largura = largura
      self.altura = altura 

     # metodo para retornar o valor do lado
    def retornar_dados(self): 
      return self.largura, self.altura 

     # metodo para calcular área 
    def calcular_area(self): 
      return self.largura * self.altura 

     # metodo para calcular o perimetro 
    def calcular_perimetro(sel): 
      return 2 * (self.largura + self.altura) 

      
      # Programa principal 

    def main(): 

      # pedir o usúario as medidas do local 

      largura_local = float(input('Informe  a largura do local (em metros): '))
      altura_local = float(input('Informe a altura do local (em metros): '))

      # criar um objeto Retângulo com oas medidas do local.
      local = Retangulo(largura_local, altura_local)

      # calcule a área do local(para sabera quantidade de pisos) 
      area_local = local.calcular.area() 

      # calcular o perimetro do local ( para saber a quantidade de rodapés)
      perimetro_local = local.calcular_perimetro()

      # pedir ao usúario o tamanho dos pisos 
      largura_piso = float(input('Informe a largura do piso (em metros): '))
      altura_piso = float(input('Informe a altura do piso (em metros): '))

      # Criar um objeto Retângular com as medidas do piso 
      piso = Retangulo(largura_piso, altura_piso)

     # Calcular a área de um piso 
      area_piso = piso.calcular_area()

      # Calcular a quantidade de pisos necessários 
      quantidade_pisos = area_local / area_piso

      # Calcular a quantidade de rodapés necessários(conssiderando o comprimento do rodapé com a largura do local) 
      quantidade_rodapes = perimetro_local / (largura_piso + altura_piso)

     # exibir os resultados 
      print(f'\nArea do local: {area_local}m²')
      print(f'\nQuantidade de pisos necessários: {quantidade_pisos}unidades')
      print(f'\nQuantidade de rodapés necessários: {quantidade_rodapes} metros')



