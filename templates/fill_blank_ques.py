import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

text = "Reading several decades of gruesome shrike papers, Sustaita first believed the real killing power came from the bird’s bill. It has bumps on the side. As it dives into the neck, it wedges that beak between neck vertebrae, biting into the prey’s spine. Shrikes definitely bite. However, based on videos, Sustaita now proposes that shaking may help immobilize, or even kill, the prey."
this_dict = {'reading': 1591, 'several': 311, 'decades': 50002, 'of': 0, 'gruesome': 50002, 'shrike': 50002, 'papers': 50002, ',': 0, 'sustaita': 50002, 'first': 2064, 'believed': 50002, 'the': 0, 'real': 306, 'killing': 3311, 'power': 272, 'came': 50002, 'from': 0, 'bird': 1126, '’': 50002, 's': 0, 'bill': 809, '.': 0, 'it': 0, 'has': 0, 'bumps': 50002, 'on': 0, 'side': 249, 'as': 0, 'dives': 50002, 'into': 0, 'neck': 1529, 'wedges': 50002, 'that': 0, 'beak': 50002, 'between': 0, 'vertebrae': 50002, 'biting': 50002, 'prey': 50002, 'spine': 4959, 'shrikes': 50002, 'definitely': 2005, 'bite': 3890, 'however': 285, 'based': 50002, 'videos': 50002, 'now': 0, 'proposes': 50002, 'shaking': 50002, 'may': 119, 'help': 881, 'immobilize': 50002, 'or': 0, 'even': 484, 'kill': 425}

q = Q.PriorityQueue()
for w in this_dict:
	q.put((-this_dict[w],w))

#sents = sent_tokenize(text)
#for sent in sents:
#	words = word_tokenize(sent.lower())
#	tagged = nltk.pos_tag(words)
#	index = 0 #needed in case a word is repeated
#	possible_words = {}
#	for t in tagged:
#		#print(t[1])
#		if t[1] in 'NN NNS NNP NNPS' and (this_dict[t[0]] > 400):
#			possible_words[t[0]] = index
#		index +=1
#	print(possible_words)

	#print(tagged)
