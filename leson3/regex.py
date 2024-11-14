import re

def find_char_at_start(text, char):
    """Ищет строки, начинающиеся с указанного символа."""
    pattern = rf'^{char}'
    return re.findall(pattern, text, re.MULTILINE)
 
def find_char_at_end(text, char):
    """Ищет строки, заканчивающиеся указанным символом."""
    pattern = rf'{char}$'
    return re.findall(pattern, text, re.MULTILINE)
 
def find_group_at_start(text, group):
    """Ищет строки, начинающиеся с указанной группы символов."""
    pattern = rf'^{group}'
    return re.findall(pattern, text, re.MULTILINE)
 
def find_group_at_end(text, group):
    """Ищет строки, заканчивающиеся указанной группой символов."""
    pattern = rf'{group}$'
    return re.findall(pattern, text, re.MULTILINE)
 
def find_char_in_text(text, char):
    """Ищет строки, содержащие указанный символ."""
    pattern = rf'{char}'
    return re.findall(pattern, text)
 
def find_group_in_text(text, group):
    """Ищет строки, содержащие указанную группу символов."""
    pattern = rf'{group}'
    return re.findall(pattern, text)
