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

## Lesson 3 — Counts to probabilities (MLE) (2026-11-15)
- Built `03_counts_to_probabilities.ipynb`: `prob()` (count / context count) and a `suggest_next()` autocomplete.
- Key numbers: P(coffee | morning) = P(train | morning) = 0.125 (2/16). After 'the' → morning 0.103, weekend 0.088, park 0.074; after 'good' → book 0.6, coffee 0.4 (all match course exactly).
- Learned: I learned that maximum likelihood is just "count the pair, divide by the context count". There's no training loop, and anything unseen gets exactly zero.

## Lesson 4 — Make it write (2026-11-15)
- Built `04_make_it_write.ipynb`: `generate()` samples word by word from `<s>` until `</s>`, for a bigram and a trigram (seeds 0–3).
- Key numbers: bigram seed 0 → "he enjoys a good book make strong"; trigram seed 0 → "he enjoys a long walk on sunny weekends" (all 8 sentences match course exactly).
- Learned: I learned that generation is the same sample → append → slide-window loop a GPT uses, and that the trigram's fluent text is mostly copied corpus phrases because its contexts are so sparse.

## Lesson 5 — The zero-probability problem (2026-11-15)
- Built `05_zero_probability.ipynb`: `prob_mle()` vs add-k `prob_addk()` over a vocabulary of |V| = 170.
- Key numbers: MLE P(coffee | drinks) = 0.0; add-1 P(coffee | drinks) = 0.00581 (1/172); add-1 P(green | drinks) = 0.01163 (2/172) (all match course exactly).
- Learned: I learned that one unseen pair zeroes a whole sentence's probability, and add-k fixes it by adding k fake counts to every word, but add-1 takes far too much mass from the words actually seen.
