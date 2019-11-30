s = "Natural-language processing (NLP) is an area of computer science\n and artificial intelligence concerned with the interactions\n between computers and human (natural) languages."
input = ["natural language","language processing","processing nlp","nlp is","is an","an area"]

import re

def generate_ngrams(s,n):
    s = s.lower()
    s = re.sub(r'[^a-zA-Z0-9\s]','',s)
    tokens = [token for token in s.split(" ") if token !=""]
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return[" ".join(ngram) for ngram in ngrams]

print(generate_ngrams(s,n=5))