
#ЗАДАНИЕ1
# list_1=(1,1.3,'fine',False, {'price', 224, True}, [1,3,5,5.5,8,0.5,'oro'])
# for all_type in list_1:
#     print(type(all_type))

#ЗАДАНИЕ2 (не работает как надо, не знаю почему)
# list1 = input("Перечислите не менее 5 наименований:").split()
# your_list = len(list1)
# i=0
# if your_list > 1:
#     while i < your_list - 1:
#         your_list[i], your_list[i+ 1] = your_list[i + 1], your_list[i]
#         i += 2
#
# print(your_list)

#ЗАДАНИЕ3
# month=input("Введите число месяца от 1 до 12:")
# win = 'зима'
# spr = 'весна'
# sum = 'лето'
# aut = 'осень'
# dict_season= {'1':win , '2':win, '3':spr, '4':spr, '5':spr, '6':sum, '7':sum, '8':sum, '9':aut, '10':aut, '11':aut, '12':win}
# print(dict_season[month])
#
# month_list=[win, win, spr, spr, spr, sum, sum, sum, aut, aut, aut, win,win]
# print(month_list[int(month)])

#ЗАДАНИЕ4
# name_user= (input('Введите ФИО полностью:')).split()
# for a, b in enumerate(name_user):
#     print(f'{a} - {b[:10]}')

#ЗАДАНИЕ5
rating = [7, 5, 3, 3, 2]
user_rating = int(input('Оцените работу оператора от 1 до 10:'))
answer = False
for index, elem in enumerate(rating):
    if user_rating > elem:
        rating.insert(index, user_rating)
        answer = True
        break

if not answer:
    rating.append(user_rating)

print(rating)






