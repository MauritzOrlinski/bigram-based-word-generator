import nltk
from bigram_model import model as bm
from get_data import get_data as gd
from nltk.corpus import words
from sys import argv
from os import listdir
from os.path import isfile, join
import pathlib

def main():
    data_dir = pathlib.Path(__file__).parent.parent / 'data'
    try:
        number_of_words_to_generate = int(argv[1])
    except IndexError:
        number_of_words_to_generate = 10

    try:
        paths = argv[2:]
        if len(paths) == 0:
            paths = [data_dir / f for f in listdir(data_dir) if isfile(data_dir / f)]

    except IndexError:
        paths = [data_dir / f for f in listdir(data_dir) if isfile(data_dir / f)]

    print(f"Paths: {paths}")

    print(f"Number of words to generate: {number_of_words_to_generate}")

    generator = bm.BigramWordGeneration()
    generator.train(gd.get_words_from_file(paths))
    number_of_real_words = 0
    for i in range(number_of_words_to_generate):
        generated_word = generator.generate()
        is_real_word = generated_word in words.words()
        print(f"{generated_word} is a word: {is_real_word}")
        if is_real_word:
            number_of_real_words += 1

    print(
        f"Number of real words: {number_of_real_words} \nNumber of generated words: {number_of_words_to_generate} \nAccuracy: {number_of_real_words / number_of_words_to_generate}")


if __name__ == '__main__':
    nltk.download('words')
    main()
