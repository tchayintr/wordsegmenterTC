# Word Segmenter using PyICU

# Prerequisite
 - Python3.5 or later
 - PyICU >= 1.9.7

# Installation
```
    >> pip3 install https://github.com/tchayintr/wordsegmenterTC/archive/master.zip
```
# Example
```
    >> from wordsegmenterTC import wordsegmenter
    >> wordsegmenter("ผมหิวข้าว")
```

The `wordsegmenter()` function will return a word-segmented line as a string e.g. "ฉัน หิว ข้าว"