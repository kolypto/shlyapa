Источники:

* [Диахронический частотный словарь русской лексики](https://kpfu.ru/diahronicheskij-chastotnyj-slovar-russkoj-leksiki.html)
* [Русский частотный словарь Шарова](https://www.slovorod.ru/freq-sharov/)

See also:

* <https://github.com/Harrix/Russian-Nouns>
* <https://github.com/danakt/russian-words> (со склонениями)
* <https://github.com/LussRus/Rus_words>

Prepare:

```console
$ python prepare.py > words.txt
$ cat words-freq.txt words-unfreq-harrix.txt words-unfreq-lussruss.txt | sort | uniq > words-all.txt
```
