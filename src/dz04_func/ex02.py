"""2.oop.

Используя функции и в целом функциональный подход реализовать ООП подход без использования синтаксиса классов, т.е. реализовать атрибуты и методы, Public/Protected/Private области, осуществить принципы ООП: наследование, инкапсуляция, полиморфизм и т.д. и т.п.. Может быть, хоть что-то из этого получится сделать.
Сразу скажу, скорее всего это реально. С другой стороны – у каждого будет индивидуальный взгляд на реализацию. Правильного решения здесь нет!"""

#class студент(почти) из ДЗ по ООП
def get_instance_student(name:str, age:int):
    #Приватные атрибуты, защищенные  и публичные не придумал как сделать 
    __name = name
    __age = age

    #Редактирование атрибута
    def set_age(age:int):
        nonlocal __age
        __age = age  

    #метод с атрибутами
    def get_info()->str:
        return f'Студент {__name}, возраст {__age}'
    
    #приватный метод
    def __print(text:str):
        print(text)

    #публичный метод с приватным внутри
    def get_info_print():
        __print(get_info())

    #словарь с публичными методами 
    return {
        'set_age':        set_age,
        'get_info':       get_info,
        'get_info_print': get_info_print
    }

#Наследование
def get_instance_graduate_student(name:str, age:int, research_topic:str):
    #super
    __student = get_instance_student(name, age)
    __research_topic = research_topic
    __publications = 0

    def get_info():
        return f'{__student['get_info']()}, тема: {__research_topic}'
    
    def add_publication():
        nonlocal __publications
        __publications += 1

    return {
        **__student, #наследуем методы
        'get_info':          get_info, #переопределили
        'add_publication':   add_publication, #новый метод
        'publication_count': lambda: __publications #get метод, можно без lambda:, но это уже как атрибут, правда если его поменять, то внутри фм он не поменяется
    }

obj1 = get_instance_student('Masha', 18)
print(obj1['get_info']())
obj1['get_info_print']()

obj1['set_age'](20)
print(obj1['get_info']())

obj2 = get_instance_graduate_student('Dima', 21, 'Искусственный интеллект')
print(obj2['get_info']())
obj1['get_info_print']()
obj2['get_info_print']() #тут не правильно((, внутри вызывается get_info родителя, если ввести правило, что внутри приват методов нельзя вызывать публичные методы, такой проблемы не будет

obj2['add_publication']()
obj2['add_publication']()
print(obj2['publication_count']())
