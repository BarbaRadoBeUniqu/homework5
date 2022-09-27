
class Computer():
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    
    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, value):
        self.__cpu = value 

    @property
    def memory(self):
        return self.__memory
    
    @memory.setter
    def memory(self, value):
        self.memory = value    

    def make_computations(self):
           return self.cpu + self.memory

    def __str__(self):
        return f'Параметры: cpu = {self.cpu}, memory = {self.memory}'

    def __gt__(self, other):  # >
        return self.memory > other

    def __lt__(self, other):  # <
        return self.memory < other
    
    def __eq__(self, other):  # ==
        return self.memory == other

class Phone:
    
    def __init__(self, sim_cards_list: list ):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    
    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
       
            if sim_card_number == 1:
                print(f'Идет звонок на номер {call_to_number} с сим-карты {sim_card_number} oshka')
            elif sim_card_number == 2:
                print(f'Идет звонок на номер {call_to_number} с сим-карты {sim_card_number} beeline')
            elif sim_card_number == 3:
                print(f'Идет звонок на номер {call_to_number} с сим-карты {sim_card_number} megacom')

    def __str__(self):
        return f'Список симкарт {self.sim_cards_list}'
   
    

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)      

    def use_gps(self, location):
        print(f'Проложен маршрут до {location}: прямо 200 метров, далее налево')

    def __str__(self):
        return super(SmartPhone, self).__str__() + f" Список сим карт {self.sim_cards_list}"


Asus = Computer(2,4)

Nokia = Phone(['oshka', 'megacom', 'beeline'])

Xiaomi = SmartPhone(2,6,['oshka', 'beeline'])
Iphone = SmartPhone(1,3,['beeline', 'megacom'])



print(Asus)
print(Nokia)
print(Xiaomi)
print(Iphone)
Iphone.call(3, 996777998811)
Xiaomi.use_gps('home')
