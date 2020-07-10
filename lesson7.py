from pprint import pprint


# Задача №1
def create_cook_book(File_name):
    cook_book = {}

    try:

        with open('recipes.txt', encoding='utf-8') as f:
            lst = [line.strip() for line in f]


        for i, c in enumerate(lst):
            if c.isdigit():
                cook_book[lst[i-1]] = []


                for slice in lst[i+1:i+int(c)+1]:
                    ingredient_name = slice.split('|')[0]
                    quantity = int(slice.split('|')[1])
                    measure = slice.split('|')[2]

                    cook_book[lst[i-1]].append({'ingredient_name':ingredient_name,'quantity':quantity,'measure':measure})
        return cook_book

    except FileNotFoundError:
        return(f'Файл: {file_name} не найден.')
    except Exception as error:
        return f'Ошибка - {error}'


# Задача №2

def get_shop_list_by_dishes(dishes, cooking_book, person_count):
    ing_dict = {}

    for key in cooking_book.keys ():
        for dish in dishes:
            if key == dish:
                for dictionary in cooking_book[key]:
                    ing_name = dictionary['ingredient_name']

                    try:
                        ing_dict[ing_name]['quantity'] += (dictionary['quantity'] * person_count)
                    except:
                        ing_dict[ing_name] = {'measure': dictionary['measure'],'quantity': dictionary['quantity'] * person_count}

    return ing_dict


#####################################

# Задача №1
print('Задача №1:\n')
pprint(create_cook_book('recipes.txt'))
print('\n' * 3)


# Задача №2
print('Задача №2:\n')
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], create_cook_book('recipes.txt'), 2))