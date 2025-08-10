
word = input("Введите слово состоящее из латинских букв нижнего регистра: ")

vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
total_vowels = 0
total_consonants = 0

for letter in word:
    if letter in vowel_counts:
        total_vowels += 1
        vowel_counts[letter] += 1
    else:
        total_consonants += 1

for letter in vowel_counts:
    if vowel_counts[letter] != 0:
        print(f"{letter}: {vowel_counts[letter]}")
    else:
        print(f"{letter}: False")
print(f"Всего гласных букв: {total_vowels}")
print(f"Всего согласных букв: {total_consonants}") 
