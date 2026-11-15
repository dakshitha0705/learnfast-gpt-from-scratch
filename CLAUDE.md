# CLAUDE.md — Learn Fast drill: "Language Modeling from First Principles — a Predictive-Text Engine"

I'm Dakshitha. This repo is my template copy of `thili-ai/learnfast-workbench` and it is what I submit
(`E:\projects\learnfast-gpt-from-scratch` → `github.com/dakshitha0705/learnfast-gpt-from-scratch`).
The full text of every lesson is in `course/`. My commit history is assessed: one clean commit per lesson.

## The lessons, in order
| # | Title | Course text | Notebook |
|---|-------|-------------|----------|
| 0 | Overview (course map) | course/00_overview.txt | — (no notebook; just read it) |
| 1 | What a language model is | course/01_what_is_lm.txt | work/01_what_is_lm.ipynb |
| 2 | Count the n-grams | course/02_count_ngrams.txt | work/02_count_ngrams.ipynb (also writes work/corpus.txt) |
| 3 | Counts to probabilities (MLE) | course/03_counts_to_probabilities.txt | work/03_counts_to_probabilities.ipynb |
| 4 | Make it write | course/04_make_it_write.txt | work/04_make_it_write.ipynb |
| 5 | The zero-probability problem | course/05_zero_probability.txt | work/05_zero_probability.ipynb |
| 6 | How good is it? Perplexity | course/06_perplexity.txt | work/06_perplexity.ipynb |
| 7 | Ship your predictive-text engine | course/07_ship_engine.txt | work/07_ship_engine.ipynb + work/ngram_lm.py |

## Environment
- Pure Python standard library (`re`, `math`, `random`, `collections`). No PyTorch needed.
- Runs in the `lfllm` workbench: `docker compose -f lfllm/docker-compose.yml up`, container `lfllm-workbench`,
  Jupyter at http://127.0.0.1:8889/?token=learnfast, `work/` mounted at `/home/learnfast/work`.
- Git Bash on Windows: `export MSYS_NO_PATHCONV=1` before any `docker exec` with Linux paths.
- Run a notebook (keeps outputs, which I submit):
  `docker exec -w /home/learnfast/work lfllm-workbench jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=-1 <file>.ipynb`
  (working directory = work/, so `open("corpus.txt")` finds work/corpus.txt).
- Write notebook builder scripts with the Write tool, not long shell heredocs (quoting breaks).

## One-time setup (first commit)
Append to `.gitignore`: `course/` (askThili's lesson text is not committed). Commit with `CLAUDE.md`, `work/README.md`, `work/LOG.md` as "Setup: drill plan and ignore course text".

## How to build each lesson
1. Read its text in `course/`. Build the notebook: the course's code in small cells, short plain-English markdown
   notes between them in MY words (don't paste the lesson prose). Keep the course's names, seeds and parameters.
2. Execute it in the container until it runs top to bottom.
3. **Reference check:** this drill has no reference package, but every output is deterministic. Compare every
   printed line with the course text; they must match exactly (the plain-Python check before this run already
   reproduced lessons 2, 4 and 6 exactly). List any difference and explain it.
4. End the notebook with `## Test yourself` (3 questions + 2–4 line answers) and `## My notes` (first person, 1–2
   lines: the key idea + anything surprising).
5. Update `work/LOG.md` (date, what was built, key numbers, `- Learned:` line in first person) and tick the lesson
   in `work/README.md`.
6. Commit only that lesson's files and push:
   `git add work/ && git commit -m "Lesson N: <title> — <one-line result>" && git push`
7. Print, then go straight on to the next lesson WITHOUT waiting:
   ```
   ✅ LESSON N COMPLETE — <title>
   Mark it complete on askThili.
   Result: <check + key numbers>
   Summary: <4–6 plain lines>
   Test yourself: <3 questions>
   Answers: <short answers>
   Try it: <one change and what to expect>
   ```
Only stop and ask me if something is truly blocked.

## Lesson 7 engine
Put the `NgramLM` class (and `to_sentences`, `to_tokens`, `build`) in `work/ngram_lm.py` so it's reusable later. The lesson 7 notebook must reproduce the course output exactly.

## Portfolio project — NOT part of this run
The portfolio project at the end of lesson 7 is out of scope for now. Don't build it; I'll do it
separately later. Lesson 7 is complete once the notebook and work/ngram_lm.py reproduce the course output.

## Don'ts
- Don't commit `course/`. Don't edit outside `work/`, `.gitignore`, `CLAUDE.md` unless needed.
- Commit messages end with the usual Co-Authored-By trailer (keep it — honest about AI help).

## Finish
Print a table of all lessons with their commit hashes, confirm `git status` is clean and pushed,
and that `git ls-files` shows no `course/` files.
