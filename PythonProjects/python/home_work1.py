def date_to_word(day_num):
    days_map = {
        1: "первое", 2: "второе", 3: "третье", 4: "четвёртое", 5: "пятое",
        6: "шестое", 7: "седьмое", 8: "восьмое", 9: "девятое", 10: "десятое",
        11: "одиннадцатое", 12: "двенадцатое", 13: "тринадцатое", 14: "четырнадцатое",
        15: "пятнадцатое", 16: "шестнадцатое", 17: "семнадцатое", 18: "восемнадцатое",
        19: "девятнадцатое", 20: "двадцатое", 21: "двадцать первое", 22: "двадцать второе",
        23: "двадцать третье", 24: "двадцать четвёртое", 25: "двадцать пятое",
        26: "двадцать шестое", 27: "двадцать седьмое", 28: "двадцать восьмое",
        29: "двадцать девятое", 30: "тридцатое", 31: "тридцать первое"
    }

    return days_map.get(day_num, "")
def month_to_word(month_num):
    months_map = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля", 5: "мая",
        6: "июня", 7: "июля", 8: "августа", 9: "сентября", 10: "октября",
        11: "ноября", 12: "декабря"
    }
    return months_map.get(month_num, "")

def year_to_word(year_num):
    thousands = year_num // 1000
    remainder = year_num % 1000
    if thousands == 1:
        prefix = "одна тысяча"
    elif thousands == 2:
        prefix = "две тысячи"
    else:
        prefix = str(thousands) + " тысяча"
    hundreds = remainder // 100
    tens_ones = remainder % 100
    hundreds_map = {
        0: "",
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот",
        9: "девятьсот"
    }
    tens_map = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто"
    }

    ones_map_dative = {
        1: "первого", 2: "второго", 3: "третьего", 4: "четвёртого", 5: "пятого",
        6: "шестого", 7: "седьмого", 8: "восьмого", 9: "девятого",
        10: "десятого", 11: "одиннадцатого", 12: "двенадцатого", 13: "тринадцатого",
        14: "четырнадцатого", 15: "пятнадцатого", 16: "шестнадцатого",
        17: "семнадцатого", 18: "восемнадцатого", 19: "девятнадцатого"
    }

    hundreds_part = hundreds_map.get(hundreds, "")
    tens = tens_ones // 10
    ones = tens_ones % 10
    if tens_ones <= 19:
        tail = ones_map_dative.get(tens_ones, "")
    else:
        tens_word = tens_map.get(tens, "")
        if ones > 0:
            ones_word = ones_map_dative.get(ones, "")
            tail = tens_word + " " + ones_word if ones_word else tens_word
        else:
            tail = tens_word

    middle_part = (hundreds_part + " " + tail).strip()
    year_str = prefix
    if middle_part:
        year_str += " " + middle_part
    return (year_str + " года").strip()

def convert_date_to_words(raw_date):
    dd, mm, yyyy = raw_date.split(".")
    day = int(dd)
    month = int(mm)
    year = int(yyyy)
    day_text = date_to_word(day)
    month_text = month_to_word(month)
    year_text = year_to_word(year)
    return f"{day_text} {month_text} {year_text}"

print(convert_date_to_words('2.08.1901 '))
