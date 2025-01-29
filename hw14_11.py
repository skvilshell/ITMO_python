import re

# Чтение файла
with open("random_text.txt", "r", encoding="utf-8") as f:
    text_data = f.read()

# Определение трех различных регулярных выражений
regex_patterns = {
    "Цифры последовательностью": r"\d{5,}",  # Последовательности из 5 и более цифр
    "Слова с заглавной буквы": r"\b[A-Z][a-z]+\b",  # Слова, начинающиеся с заглавной буквы
    "Последовательности из 3 и более гласных": r"[AEIOUaeiou]{3,}"  # Группы из 3+ гласных подряд
}

# Поиск совпадений по каждому регулярному выражению
matches_results = {}
for name, pattern in regex_patterns.items():
    matches = re.findall(pattern, text_data)
    matches_results[name] = {
        "first_10": matches[:10],  # Первые 10 совпадений
        "total_count": len(matches)  # Общее количество совпадений
    }

print(matches_results)

