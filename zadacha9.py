# Напишите программу которая спрашивает от пользователя 2 вещи:
#
# 1.Путь до картинки которую нужно изменить.
trek = input('введите путь до картинки: ')
# 2.Путь до картинки НА которую нужно изменить.
trek2 = input('введите новый путь до картинки: ')
with open('trek', 'w') as ff:
    ff.write(trek2)
ff.close()
print(ff)
# Еслт переи оба пути существуюпишите первую картинку на вторую, если нет скажите пользователю какой картинке не существует.

