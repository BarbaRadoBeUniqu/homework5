import statistics


class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"ФИО: {self.fullname}, возраст: {self.age}, семейное положение: {self.is_married}")    


class Students(Person):
    
    def __init__(self, fullname, age, is_married, marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = dict(marks)

    def sr_ocenka(self):
        s=[]
        for i in self.marks.values():
            s.append(int(i))
        z = statistics.mean(s)
        print("Средняя оценка по всем предметам: ", z)
    
    def show_students(self):
        print(f'Студент {self.fullname}, Возраст {self.age}, Семейное положение {self.is_married}, оценки {self.marks} ')


class Teacher(Person):
    salary = 45000
    
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experience = experience

    def bonus(self):
        god = 0
        if self.experience > 3:
            staj = self.experience - 3
            for i in range(1, staj+1):
                god += 5
            self.salary = self.salary + (self.salary//100 * god)
            print(f"Надбавка к зарплате у учителя {self.fullname}, {self.age}, {self.is_married} с учетом стажа {staj} лет: ", god, "%")
            print(f"Зарплата у учителя {self.fullname}, {self.age}, {self.is_married} с учетом стажа {staj} лет: {self.salary} сом")


# Ivanov = Students("Ivanov", 22, "NeJenat", {"высшмат":4, "ооп":5, "философия":3})
# Ivanov.sr_ocenka()
# Ivanov.show_students()

# Zoya = Teacher("Zoya Mihailovna", 45, "zamuzhem", 10)
# Zoya.bonus()


def create_students():
    list = []

    Petrov = Students('Petrov', 22, "Holost", {"высшмат":5, "ооп":4, "философия":4})
    Gurov = Students('Gurov', 24, "Holost", {"высшмат":3, "ооп":4, "философия":5})
    Sidorov = Students('Sidorov', 23, "Holost", {"высшмат":5, "ооп":5, "философия":5})
    
    list.append(Petrov)
    list.append(Gurov)
    list.append(Sidorov)
    
    
    return list


p = create_students()
for i in p:
    print(i.show_students(), i.sr_ocenka())
    
