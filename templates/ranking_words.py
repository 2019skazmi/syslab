import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

import queue as Q
import math

punc = """ .,/';[]}{|"-_!?#@$%^&*()+=:' """

#example_sent = "This is an example showing off stop word filtration. People use many common words when speaking, and I do not want test questions to be centered around a common word."
example_text = "Reading several decades of gruesome shrike papers, Sustaita first believed the real killing power came from the bird’s bill. It has bumps on the side. As it dives into the neck, it wedges that beak between neck vertebrae, biting into the prey’s spine. Shrikes definitely bite. However, based on videos, Sustaita now proposes that shaking may help immobilize, or even kill, the prey."

stop_words = set(stopwords.words("english"))

questions = {}
for sent in sent_tokenize(example_text):
	words = word_tokenize(sent)
	tagged = nltk.pos_tag(words)
	POS_tags = {}
	for w, pos in tagged:
		POS_tags[w] = pos
	print(POS_tags)
	numbers = "0123456789"
	top5000_text = open("top5000words.txt", "r")
	top_dict = {}
	for w in top5000_text:
		w = w.replace(" ", "") #just spaces
		w = w.replace("	", "") #tabs
		w = w.replace("\n", "")
		num = ""
		count = 0
		while w[count] in numbers:
			num = num + w[count]
			count += 1
		#print(num)
		word = w[count::]
		#print(word)
		top_dict[word] = int(num)
	#print(top_dict)
	this_dict = {}
	for w in words:
		w2 = w.lower()
		if w2 in stop_words or w2 in punc:
			this_dict[w] = 0
		elif w2 in top_dict:
			this_dict[w] = top_dict[w2]
		else:
			this_dict[w] = 50002
	q = Q.PriorityQueue()
	for w in this_dict:
		q.put((-this_dict[w],w))
	print(q)
	#while not q.empty():
	#	tup = q.get()
	#	rank = abs(tup[0])
		#if rank != 0:
	#	print(tup[1] + ": " + str(rank))
	rank, key_word = q.get()
	while POS_tags[key_word] not in 'NN NNS NNP NNPS':
		rank, key_word = q.get()
	fill_in_blank = sent.replace(key_word, "__________")
	questions[fill_in_blank] = key_word
print(questions)


