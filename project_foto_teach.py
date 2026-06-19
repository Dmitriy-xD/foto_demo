class Foto:
    def __init__(self, title, date, attraction, price):
        self.title = title
        self.date = date
        self.attraction = attraction
        self.price = price

    def info(self):
        return f"{self.title}, {self.date}, {self.attraction}, {self.price}"

objects_list = []

def choosing():
    print("1. Добавить фото")
    print("2. Показать все фотографии")
    print("3. Найти фотографии по аттракциону")
    print("4. Посчитать общую выручку")
    print("5. Удалить фото")
    print("6. Сохранить фото")
    print("7. Загрузить фото")
    print("Выберите число:")
    inp = int(input())
    if inp == 1:
        add_foto()
    if inp == 2:
        show_all()
    if inp == 3:
        search()
    if inp == 4:
        total_income()
    if inp == 5:
        delete_foto()
    if inp == 6:
        save_data()
    if inp == 7:
        load_data()

def add_foto():
    print("Впишите название, дату, аттракцион, цену, через запятую")
    data_foto = input()
    try:
        data = data_foto.split(", ")
        new_foto = Foto(data[0], data[1], data[2], int(data[3]))
        objects_list.append(new_foto)
        print("Отлично")
    except:
        print("Не правильно вписал")

def show_all():
    print("=" * 60)
    print("Все фото")
    print("=" * 60)
    for foto in objects_list:
        print(foto.info())

def search():
    print("Найти фото по аттракциону")
    print("Введите название аттракциона")
    name_atr = input()
    seek = False
    for foto in objects_list:
        if foto.attraction == name_atr:
            print(foto.info())
            seek = True
    if not seek:
        print("нет такого")
        
def total_income():
    total = 0
    for foto in objects_list:
        total += foto.price  
    print(f"Общая выручка: {total}")

def delete_foto():
    print("Выберите какое фото удалить")
    i = 1
    for foto in objects_list:
        print(f"{i}. {foto.info()}")
        i += 1
    inp_del = int(input())
    try:
        objects_list.pop(inp_del-1)
    except:
        print("такого нету")

def save_data():
    with open("photos.txt", "w", encoding="utf-8") as file:
        for foto in objects_list:
            file.write(
                f"{foto.title};{foto.date};{foto.attraction};{foto.price}\n"
            )

def load_data():
    with open("photos.txt", "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(";")

            foto = Foto(
                data[0],
                data[1],
                data[2],
                int(data[3])
            )

            objects_list.append(foto)

while True:

    choosing()