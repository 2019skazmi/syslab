import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords, state_union
from nltk.stem import PorterStemmer

#tokeizing
	#word tokenizer: separates by word
	#sentence tokenizers: separates by sentence
#lexicon and corporas
	#corpora: body of text (ex: medical journals, 
	#	presidential speeches, English language)
	#lexicon: words and their meanings (ex: dictionary for English language,
	#	'bull' = someone who is positive about the market for investor speak)

#example_text = "Hello Mrs. Lina, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."
 
#print(sent_tokenize(example_text)) #returns list of sentences
#print(word_tokenize(example_text)) #returns list of words with punc considered a word

#example_sent = "This is an example showing off stop word filtration"
#stop_words = set(stopwords.words("english"))

#words = word_tokenize(example_sent)
#filtered_sent = [w for w in words if not w in stop_words]

#print(filtered_sent)

#ps = PorterStemmer()

#example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]
#for w in example_words:
#	print(w)
#	print(ps.stem(w))

#train_text = state_union.raw("2005-GWBush.txt")
#sample_text = state_union.raw("2006-GWBush.txt")

#custom_sent_tokenizer = PunktSentenceTokenizer(sample_text)

#tokenized = custom_sent_tokenizer.tokenize(sample_text)

#def process_content():
#	try:
#		for i in tokenized:
#			words = nltk.word_tokenize(i)
#			tagged = nltk.pos_tag(words)
#			print(tagged)
#
#	except Exception as e:
#		print(str(e))

#process_content()

sent = "This is an example sentence, in this sentence Sarah is a proper noun."

words = word_tokenize(sent)
tagged = nltk.pos_tag(words)
print(tagged)

## OUTPUT w/lower: [('this', 'DT'), ('is', 'VBZ'), ('an', 'DT'), ('example', 'NN'), ('sentence', 'NN'), (',', ','), ('in', 'IN'), ('this', 'DT'), ('sentence', 'NN'), ('sarah', 'NN'), ('is', 'VBZ'), ('a', 'DT'), ('proper', 'JJ'), ('noun', 'NN'), ('.', '.')]
## OUTPUT w/normal: [('This', 'DT'), ('is', 'VBZ'), ('an', 'DT'), ('example', 'NN'), ('sentence', 'NN'), (',', ','), ('in', 'IN'), ('this', 'DT'), ('sentence', 'NN'), ('Sarah', 'NNP'), ('is', 'VBZ'), ('a', 'DT'), ('proper', 'JJ'), ('noun', 'NN'), ('.', '.')]




