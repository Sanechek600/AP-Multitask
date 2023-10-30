from multiprocessing import Pool, cpu_count
from itertools import repeat
import argparse


def find_word(word: str, file_path: str) -> bool:
    """Looks for the word in the file, True if found"""
    with open(file_path, 'r') as f:
        text = f.read()
        print(text)
        if word in text: return True
        else: return False


if __name__=="__main__":
    """This script searches for a designated word word within multiple files using multiprocessing"""
    parser = argparse.ArgumentParser(description='Input the needed word and file paths')
    parser.add_argument('--word', type=str, default='enemies', help='Input the word to search for')
    parser.add_argument('--files', type=str, default='texts/is_1.txt, texts/isnt_1.txt', help='Input file paths separated by \', \'')
    args = parser.parse_args()
    file_list = [str(item) for item in args.files.split(', ')]
    cpus = cpu_count()
    print(file_list)

    with Pool(cpus) as p:
        answer = p.starmap(find_word, zip(repeat(args.word), file_list))
        print(answer)