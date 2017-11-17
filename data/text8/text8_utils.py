import nlpu

# global variables
voca = nlpu.Vocabulary()
data_index = 0
_onlyalpha = True
_stopwords = True
_stemmer = False

def set_preprocessor(onlyalpha, stopwords, stemmer):
	global _onlyalpha, _stopwords, _stemmer
	_onlyalpha = onlyalpha
	_stopwords = stopwords
	_stemmer = stemmer

def build_voca(tokens, filename):
	voca.addall(tokens)

def save_voca(filename):
	voca.save(filename)

def load_voca(filename):
	voca.load(filename)

def get_text8(datapath):
	f = open(datapath, 'r')
	lines = f.readlines()
	f.close()

	tokens = []
	for line in lines:
		tokens += nlpu.tokenize(line, _onlyalpha, _stopwords, _stemmer)

	return tokens

def next_batch(data, batch_size, one_hot = False):
	global data_index

	ret = []
	size = 0
	
	if data_index == len(data):
		data_index = 0

	for i in range(batch_size):
		if data_index >= len(data):
			data_index = 0
			break
		if len(data[data_index]) > 0:
			if one_hot:
				ret.append(voca.word2vec(data[data_index]))
			else:
				ret.append(data[data_index])
			size += 1
		data_index += 1

	return ret, size

