Источники:

* [Диахронический частотный словарь русской лексики](https://kpfu.ru/diahronicheskij-chastotnyj-slovar-russkoj-leksiki.html)
* [Русский частотный словарь Шарова](https://www.slovorod.ru/freq-sharov/)

See also:

* <https://github.com/Harrix/Russian-Nouns>
* <https://github.com/danakt/russian-words> (со склонениями)
* <https://github.com/LussRus/Rus_words>

Подготовка:

```console
$ python words-freq.py > words-freq.txt
$ cat words-unfreq-harrix.txt words-unfreq-lussruss.txt > words-unfreq.txt
$ cat words-freq.txt words-unfreq.txt | sort | uniq > words-all.txt
```

На выходе:

* `words-freq.txt`: частотный словарь русского языка
* `words-unfreq.txt`: все слова, независимо от частотности
* `words-all.txt`: вообще все слова вместе, по алфавиту
