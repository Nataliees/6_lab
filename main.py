def one():
    countries_dict = {"Австрия": "Вена", "Бельгия": "Брюссель", "Великобритания": "Лондон", "Германия": "Берлин", "Ирландия": "Дублин", "Лихтенштейн": "Вадуц", "Нидерланды": "Амстердам",
                 "Франция": "Париж", "Беларусь": "Минск", "Болгария": "София", "Польша": "Варшава", "Чехия": "Прага", "Албания": "Тирана", "Босния и Герцеговина": "Сараево",
                 "Северная Македония": "Скопье", "Сербия": "Белград"}
    print(countries_dict)
    a=input("Введите название страны ")
    print(countries_dict[a])
    for key in sorted(countries_dict):
        print(key, " - ", countries_dict[key])
def two():
    alphabet = {
        "а": 1,
        "в": 1,
        "б": 3,
        "г": 3,
        "д": 2,
        "е": 1,
        "ё": 3,
        "ж": 5,
        "з": 5,
        "и": 1,
        "й": 4,
        "к": 2,
        "л": 2,
        "м": 2,
        "н": 1,
        "о": 1,
        "п": 2,
        "р": 1,
        "с": 1,
        "т": 1,
        "у": 2,
        "ф": 10,
        "х": 5,
        "ц": 5,
        "ч": 5,
        "ш": 8,
        "щ": 10,
        "ъ": 10,
        "ы": 4,
        "ь": 3,
        "э": 8,
        "ю": 8,
        "я": 3
    }
    w = input("Введите слово: ")
    s = 0
    for i, value in w:
        s += alphabet[i.lower()]
    print("Сумма: ", s)

def three():
    import random

    students = {"Иванов", "Петров", "Смирнов", "Сидоров", "Васильев", "Кузнецов", "Попов", "Федоров", "Лебедев",
                "Семенов"}
    languages = {"Русский", "Английский", "Французский", "Немецкий", "Китайский"}

    lang_stud = {}

    for st in students:
        kolvo = random.randint(1, 3)
        lang_stud[st] = random.sample(list(languages), kolvo)

    unique_lang = set()
    for i in lang_stud:
        unique_lang = unique_lang.union(set(lang_stud[i]))

    # print(lang_stud)
    print("Множество различных языков, которые знают студенты: ", sorted(unique_lang), f" ({len(unique_lang)})")

    china = [i for i in lang_stud if "Китайский" in lang_stud[i]]
    print("Студенты, знающие китайский: ", china)
one()
two()
three()