# Розглянемо приклад продажу автомобиля. Информация, яку потрібно знати це модель машини, її колір та ім'я власник.
# Особиста інофрмація (номер паспорту) буде інкапсульована і таку інформацію можна буде отримати тільки за допомогою
# гетерів та сетерів при продажі авто. Зробимо його protected з використанням __name_attr

class Car:
    def __init__(self, model, color, name_driver, passport_driver):
        self.model = model
        self.color = color
        self.name_driver = name_driver
        self._passport_driver = passport_driver

    @property
    def passport_driver(self):
        return f"Паспортні данні: {self._passport_driver}"

    @passport_driver.setter
    def passport_driver(self, new_passport_driver):
        print(f"Паспортні данні з {self._passport_driver} на {new_passport_driver}")
        self._passport_driver = new_passport_driver

    @passport_driver.deleter
    def passport_driver(self):
        del self._passport_driver


# Приклад використання класу Car
car = Car(model="Toyota", color="Blue", name_driver="Сергій", passport_driver="АА0000")
print(car.model)
print(car.color)
print(car.name_driver)
print(car.passport_driver)  # Виведе "АА0000"
car.passport_driver = "BB1111"
print(car.passport_driver)  # Виведе "BB1111"
