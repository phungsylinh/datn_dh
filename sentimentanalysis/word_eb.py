from gensim.models import Word2Vec
model_path = "word2vec.model"
model = Word2Vec.load(model_path)

word = "rất_tệ"
vector = model.wv[word]
print(vector)
sim_words = model.wv.most_similar(word)
print(sim_words)
