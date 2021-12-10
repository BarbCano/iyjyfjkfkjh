class Persona:
    def __init__(self, nombre, altura, edad, vestimenta):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.vestimenta = vestimenta

    def saludar(self):
        print('Hola me llamo', self.nombre)

    # Se ejecuta cuando imprimimos al objeto directamente
    def __str__(self) -> str:
        return f'La persona se llama {self.nombre} su edad es {self.edad}\n y su altura es {self.altura}\n viene vestido de {self.vestimenta}'

class Empleado(Persona):
    def __init__(self, nombre, altura, vestimenta, empresa, puesto):
        super().__init__(nombre, altura, vestimenta)
        self.empresa = empresa
        self.puesto = puesto

    def saludar(self):
        print(f'Hola me llamo {self.nombre} y soy empleado de {self.empresa}')

class Gerente(Empleado):
    def __init__(self, nombre, altura, vestimenta, empresa, puesto):
        super().__init__(nombre, altura, vestimenta, empresa, puesto)
        self.puesto = 'Gerente'

    def saludar(self):
        print(f'Soy el gerente de {self.empresa}, mi nombre es {self.nombre}')

    def entrevistar(self, persona):
        print(f'Estoy entrevistando a {persona}')

nombreGerente = input('Ingrese nombre del gerente\n')
gerenton = Gerente(nombreGerente, 1.80, 'Gaberdina de 3 botones', 'Monse.inc', 'Gerente de surcursal')
gerenton.saludar()
gerenton.entrevistar('Jona')