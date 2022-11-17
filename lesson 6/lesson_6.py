import re
text = """100  ИНФ  Информатика
213  МАТ Матиматика
156 АНГ Английский
"""
# Извлечь все номера курсов
ch = re.findall('[0-9]+', text)
# Извлечь все коды курсов (для латиницы [A-Z]
codes = re.findall('[А-ЯЁ]{3}', text)
# Извлечь все названия курсов
names = re.findall('[а-яА-ЯёЁ]{4,}', text)
print(ch)
print(codes)
print(names)

text = str(input('Ведите матемитическое выражение для вычисления: '))
# list_sign = list(text.replace(' ', ''))
# print(list_sign)
for i in range(len(text)):
    if text[i] == '*':
        temp = int(text[i - 1]) * int(text[i + 1])
        print(temp)
    elif text[i] == '/':
        temp = int(text[i - 1]) / int(text[i + 1])
        print(temp)
