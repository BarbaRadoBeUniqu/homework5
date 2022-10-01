import re

class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        return f'Name: {self.__full_name} // Email: {self.__email} // FileName: {self.__file_name} // Color: {self.__color}' 

with open('MOCK_DATA.txt', "r", encoding='utf-8') as file:
    

    list = []    
    line = file.readline()
    while line:  

        full_name = re.findall(r"(?:^[A-Z][a-z-]+\s[A-Za-z-'. ]+)", line)
        full_name = ''.join(full_name)
            
        email = re.findall(r'[a-z](?:[a-z0-9]+@[a-z0-9-\.]+\.[a-z]+)', line)
        email = ''.join(email)

        file_name = re.findall(r'[A-Z](?:[a-zA-Z\.]+\.[a-z0-9]+)|[A-Z]\.[a-z0-9]+', line)
        file_name = ''.join(file_name)

        color = re.findall(r'#(?:[0-9a-z]+)', line)
        color = ''.join(color)

        data = Data(full_name, email, file_name, color)

        # print(data)

        # list.append(data.full_name)
        # list.append(data.email)
        # list.append(data.file_name)
        # list.append(data.color)
        list.append(data)
         

        line = file.readline()

file.close() 

# print(list)

for i in list:

    with open("fullname.txt", 'a') as fullname:
        fullname.write(i.full_name + '\n')

    with open("email.txt", 'a') as email:
        email.write(i.email + '\n')

    with open("file.txt", 'a') as filename:
        filename.write(i.file_name + '\n')

    with open("color.txt", 'a') as color:
        color.write(i.color + '\n')     
        
    # print(i.color)
