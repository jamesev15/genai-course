class Car:
    def __init__(self, marca, fecha):
        self.marca = marca
        self.fecha = fecha

    def arrancar(self, velocidad):
        print(f"arrancando hacia {velocidad}")

    def modelo(self):
        return f"marca: {self.marca}, fecha de fabricacion: {self.fecha}"

car = Car("honda", "2019")
car2 = Car("hyundai", "2020")

# print(car.fecha)

# print(car2.fecha)

car.arrancar(20)
especificaciones = car2.modelo()

print(especificaciones)