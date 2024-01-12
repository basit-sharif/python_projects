from collections import Counter
import re


def read_text_from_file(filename: str):
    with open(filename, "r") as file:
        return file.read()


def word_counter(text: str):
    # text.split()
    words_arr = re.findall(r'\w+', text.lower())
    word_counts = Counter(words_arr)
    print(word_counts.most_common(10))


readed_text = read_text_from_file(
    r"D:\path to your file .txt")
word_counter(readed_text)
