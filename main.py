from random import  *

idea = []
words = open('squad.txt', encoding='utf-8')
for i in words:
   idea.append(i.replace('\n', ''))

enterWord = ''
print('Генератор наименования отряда')

while enterWord != 'exit':
   print(idea[randint(0, len(idea) -1)])
   enterWord = input('Генерации следующего наименования, нажмите \'Enter\', для выхода нажмите \'exit\'')
