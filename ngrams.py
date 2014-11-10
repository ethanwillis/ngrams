def ngramsProgram(corpus, n):
	# Input comes from our parameters

	# process our input to find ngrams 
	ngrams = findNGrams(corpus, n)
	
	# Output our ngrams.
	outputNGrams(ngrams)

def findNGrams(corpus, n):
	# Tokenize our corpus, which also gives us all of our unigrams
	tokenizedCorpus = corpus.split(' ')
	# initialize our set of "windows", ngrams.
	ngrams = []
	# find windows of size n and add them to our set of windows.
	for i in range(0, len(tokenizedCorpus)-(n-1)):
		# initialize an empty ngram
		curNGram = []
		# find the ngram in our current window, starting with the
		# xth unigram.
		for x in range(i, i+n):
			# build our current ngram from the current unigram
			curNGram.append(tokenizedCorpus[x])
		# add this ngram to our list of ngrams.
		ngrams.append(curNGram)
	return ngrams	

def outputNGrams(ngrams):
	for ngram in ngrams:
		print(str(ngram))

ngramsProgram("The quick brown fox jumped over the lazy dog.", 4)
