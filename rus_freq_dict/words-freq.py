import re
import csv
import itertools
from typing import Iterable, Iterator

def main():
    for word, freq in all_words_together():
        print(word)


def all_words_together() -> Iterable[tuple[str, float]]:
    """ Merge words from multiple sources """
    source = itertools.chain(
        # Word sources
        read_35000rus(),
        # read_rus_freq_dict_1920_2019(),  # too old and forgotten
        read_rus_freq_dict_1992_2019(),
    )

    # Merge
    words = dict()
    for word, freq in source:
        if word not in words:
            words[word] = freq

    # Sort
    return sorted(words.items(), key=lambda v: v[1], reverse=True)


# === SOURCES

def read_35000rus() -> tuple[str, float]:
    """ Words: 35000rus.csv """
    # ROW:[0] ordinal number [1] freq per million [2] word [3] type
    # types card, adjpron, misc, pron, noun, ord, verb, prep, adv, adj
    return (
        (word, float(freq))
        for n, freq, word, type_ in _iter_csv("35000rus.csv", delim=',', quote='"')
        if type_ == 'noun'
    )

def read_rus_freq_dict_1920_2019() -> tuple[str, float]:
    """ Words: rus_freq_dictionary_1920-2019.csv """
    yield from _read_rus_freq_dict_2019("rus_freq_dictionary_1920-2019.csv")

def read_rus_freq_dict_1992_2019() -> tuple[str, float]:
    """ Words: rus_freq_dictionary_1992-2019.csv """
    yield from _read_rus_freq_dict_2019("rus_freq_dictionary_1992-2019.csv")

def _read_rus_freq_dict_2019(filename: str) -> tuple[str, float]:
    """ Words: rus_freq_dictionary """
    reader = _iter_csv(filename, delim='\t', quote='"')
    next(reader)  # skip

    rex = re.compile('(\d+) ([^(]+) \((\w+)\)')

    # ROW: [0] word, conjugated [1] position [2] freq per million
    # [4]: id word (NOUN)
    for row in reader:
        m = rex.match(row[4]).groups()  # [0] id [1] word [2] type
        if m[2] == 'NOUN':
            yield (m[1], float(row[2]))


def _iter_csv(filename: str, delim: str, quote: str) -> Iterator[list]:
    """ Read CSV file, line by line """
    with open(filename, 'rt') as csvfile:
        reader = csv.reader(csvfile, delimiter=delim, quotechar=quote)
        for row in reader:
            yield row




# === Go

if __name__ == '__main__':
    main()
