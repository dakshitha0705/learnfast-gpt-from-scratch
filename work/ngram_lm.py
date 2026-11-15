"""A reusable smoothed n-gram language model (Learn Fast drill, Lesson 7).

    from ngram_lm import NgramLM
    lm = NgramLM(n=2, k=0.5).fit(open("corpus.txt").read())
    lm.suggest_next("i drink")   # -> ['coffee', 'tea']
    lm.generate(seed=3)          # -> sampled sentence
    lm.perplexity(held_out_text) # -> lower is better

Pure standard library.
"""
import re, math, random
from collections import Counter, defaultdict


def to_sentences(text):
    return [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]

def to_tokens(sentence):
    return re.findall(r"[a-z']+", sentence.lower())

def build(sents, n):
    """context (n-1 words) -> Counter of the words that follow it."""
    foll = defaultdict(Counter)
    for s in sents:
        toks = ["<s>"] * (n - 1) + to_tokens(s) + ["</s>"]
        for i in range(len(toks) - n + 1):
            foll[tuple(toks[i:i + n - 1])][toks[i + n - 1]] += 1
    return foll

class NgramLM:
    "A smoothed n-gram language model: fit -> suggest_next / generate / perplexity."
    def __init__(self, n=2, k=0.5):
        self.n, self.k = n, k

    def fit(self, text):
        self.sents = to_sentences(text)
        self.foll = build(self.sents, self.n)
        self.V = set(t for s in self.sents for t in to_tokens(s)) | {"</s>"}
        return self

    def _prob(self, ctx, w):
        c = self.foll.get(ctx, Counter()); total = sum(c.values())
        return (c[w] + self.k) / (total + self.k * len(self.V))

    def suggest_next(self, text, topk=3):
        ctx = tuple((["<s>"] * (self.n - 1) + to_tokens(text))[-(self.n - 1):])
        c = self.foll.get(ctx, Counter())
        words = [w for w, _ in c.most_common() if w != "</s>"]   # never suggest end-of-sentence
        return words[:topk] or ["(no idea)"]

    def generate(self, seed=0, max_len=25):
        rng = random.Random(seed); ctx = ("<s>",) * (self.n - 1); out = []
        for _ in range(max_len):
            c = self.foll.get(ctx)
            if not c: break
            words, wts = zip(*c.items())
            nxt = rng.choices(words, weights=wts)[0]
            if nxt == "</s>": break
            out.append(nxt); ctx = (ctx + (nxt,))[-(self.n - 1):]
        return " ".join(out)

    def perplexity(self, text):
        log_sum, N = 0.0, 0
        for s in to_sentences(text):
            toks = ["<s>"] * (self.n - 1) + to_tokens(s) + ["</s>"]
            for i in range(len(toks) - self.n + 1):
                ctx, w = tuple(toks[i:i + self.n - 1]), toks[i + self.n - 1]
                log_sum += math.log(self._prob(ctx, w)); N += 1
        return math.exp(-log_sum / N)


if __name__ == "__main__":
    lm = NgramLM(n=2, k=0.5).fit(open("corpus.txt").read())
    for phrase in ["i drink", "the morning", "on the", "she reads a"]:
        print(f"{phrase!r:15s}->  {lm.suggest_next(phrase)}")
    print("\ngenerated:", lm.generate(seed=3))
