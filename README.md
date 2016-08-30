# Amharic-rule-based-lemmatizer

Stemming is the process of reducing affixes to the stem of the word that can serve different
inflictions and sometimes derivation the word can possibly go through, producing different
morph   variations. Lemmatization is reduction upto a dictionary form.

This program works on python3.

The lemmatizer consists of 3 distinct stages; Transliteration, Stemming and Disambiguation.
The unicode input first gets transliterated and then goes through a series of predefined rule
checks for affixes and stemming, after the stemming we may have maximum of 10 and
minimum 1 stem candidates. These candidates will then be searched in the MRD(machine readable dictionary) in­order
to   disambiguate   and   choose   the   right   stem.   The   longest   string   length   matched   will   be
chosen automatically. 

This occurrence data is important in the disambiguation process of the stemmer when two
matches are found in the dictionary with the same string length.
