from konlpy.corpus import kobill
from konlpy.corpus import kolaw
from konlpy.tag import Komoran
from gensim.models import Word2Vec
import re
import multiprocessing

def generate_ko_stopwords(filename):
  fin = open(filename, "r", encoding="utf-8")
  l = fin.readlines()
  fin.close()
  s = set(l)

  fout = open("ko_stopwords.txt", "w", encoding="utf-8")
  for stpwrd in s:
    fout.write(stpwrd)
  fout.close()

def load_ko_stopwords(filename):
  with open(filename, "r", encoding="utf-8") as f:
    s = set([line.rstrip() for line in f])
  return s

def tokenize(txt):
  tokens = Komoran().morphs(txt)
  hangul = re.compile('[^\uac00-\ud7a3]+')
  stpwrds = load_ko_stopwords("ko_stopwords.txt")
  tokens = [hangul.sub('', i) for i in tokens]
  tokens = [i for i in tokens if len(i) > 0 and i not in stpwrds]
  return tokens

#main
tokens = []
for i in kobill.fileids(): tokens.append(tokenize(kobill.open(i).read()))

for i in kolaw.fileids(): tokens.append(tokenize(kolaw.open(i).read()))

config = {
  'min_count': 2,
  'size': 100,
  'sg': 1,
  'batch_words': 10000,
  'iter': 20,
  'workers': multiprocessing.cpu_count(),
}

embedding_model = Word2Vec(tokens, **config)

print(embedding_model.most_similar(positive=tokenize('육아휴직'), topn=50))
print(embedding_model.most_similar(positive=tokenize('법률'), topn=50))
print(embedding_model.most_similar(positive=tokenize('결혼'), topn=50))