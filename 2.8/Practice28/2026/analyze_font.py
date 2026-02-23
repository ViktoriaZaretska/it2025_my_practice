from fontTools.ttLib import TTFont

font_path = 'liberationserif.ttf'  # шлях до твого файлу шрифту

font = TTFont(font_path)
print("Таблиці у шрифті:", font.keys())

# Виводимо інформацію з таблиці 'name'
for record in font['name'].names:
    name = record.string.decode(record.getEncoding(), errors='ignore')
    print(f"Name ID {record.nameID}: {name}")