words_dict = {}

with open("words.txt") as words:
    for word in words.read().split():
        words_dict[word] = 0

with open("input.txt") as file:
    for word in file.read().split():
        current_word = ''
        for ch in word:
            if ch.isalpha():
                current_word += ch
        if current_word.lower() in words_dict:
            words_dict[current_word.lower()] += 1

sorted_values = sorted(words_dict.items(), key=lambda x: -x[1])
for key, value in sorted_values:
    with open('words_count', 'a') as words_count:
        words_count.write(f'{key} - {value}\n')
