# Log

One entry per lesson: date, what was built, key numbers, what I learned.

## Lesson 1 — What a language model is (2026-11-15)
- Built `01_what_is_lm.ipynb`: a hand-made next-word probability table and a `suggest()` that ranks it.
- Key numbers: after 'the' → morning 0.3, train 0.2, park 0.15; after 'good' → book 0.5, coffee 0.5 (matches course exactly).
- Learned: I learned that a language model is just P(next word | context), and the Markov shortcut (keep only the last n-1 words) is what makes it possible to estimate by counting.

## Lesson 2 — Count the n-grams (2026-11-15)
- Built `02_count_ngrams.ipynb`: saved the 60-sentence corpus to `corpus.txt`, tokenized it, and counted bigrams with `build()`.
- Key numbers: 2528 characters, 60 sentences, 493 tokens, 169-word vocabulary. 'the' → morning 7, weekend 6, park 5; 'morning' → `</s>` 8; sentences start with 'the' 23 times (all match course exactly).
- Learned: I learned that the n-gram "model" is literally a dict of Counters, and that the `<s>`/`</s>` markers let it learn how sentences start and stop.
