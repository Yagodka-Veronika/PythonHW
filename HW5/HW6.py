# Дана строка (возможно,пустая),состоящаяиз букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE,которая на выходе даст строку вида:A4B3C2XYZD4E3F3A6B28 И сгенерирует ошибку,
# если на вход пришла невалидная строка.
# Пояснения:
# Если символ встречается 1 раз , он остается без изменений ;
# Если символ повторяется более 1 раза,
# к нему добавляется количество повторений





def rle(string):

    for i in string:
        if i not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return "Ошибка"

    use_str = ""
    count = 1

    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            use_str += string[i - 1] + (f"{count}" if count > 1 else "")
            count = 1

    if count > 0:
        use_str += string[-1] + (f"{count}" if count > 1 else "")

    return use_str


row = input("Введите строку ")
print(rle(row))





