import os
import csv
from string import maketrans

def ngramsProgram(directory, ngramQueries):
	# Input: get corpus from all text files within a directory
	# Step 1: Get list of files in a directory
	txtFileList = os.listdir(directory)	
	# Step 2: Process each text file in our list of files
	searchResults = []
	for txtFile in txtFileList:
		# create path to text file
		filePath = os.path.join(directory, txtFile)
		# open and read the text file
		openTxtFile = open(filePath, 'r')
		txtFileContents = openTxtFile.read()
		# close the file
		openTxtFile.close()
		# Process: process our input to find ngrams matching our
		# ngram queries. 
		queryResults = findNGramsMatching(txtFileContents, ngramQueries)
		# Prepend the filename to our result.
		queryResults.insert(0, txtFile)
		# Add our query results to our list of results.
		searchResults.append(queryResults)

	# Output: save our ngrams to disk.
	saveResultsAsCSV(searchResults)

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

def preprocess(corpus):
	# remove punctuation new lines and tabs
	# create translation table.
	translateTable = maketrans(',\'".-', '     ')
	corpus = corpus.translate(translateTable)
	# normalize for case
	corpus = corpus.lower()
	corpus = corpus.replace('\n', '').replace('\t', '').replace('\r', '');
	return corpus

def findNGramsMatching(corpus, ngramQueries):
	# preprocess our corpus
	corpus = preprocess(corpus)

	# find number of ngrams from our corpus that match the ngram
	# for our current ngramQuery
	queryResults = []
	for ngramQuery in ngramQueries:
		# get all ngrams in our corpus that are the size of our query
		ngrams = findNGrams(corpus, len(ngramQuery))
		numMatches = 0
		for ngram in ngrams:
			if cmp(ngram, ngramQuery) == 0:
				numMatches += 1
		queryResults.append(numMatches)
	return queryResults

# Function to save search rsults to disk as a comma delimited CSV file.
def saveResultsAsCSV(results):
	# open output file in current working directory
	with open('summary.csv', 'wb') as outputFile:
		fileWriter = csv.writer(outputFile, delimiter=',')
		# write csv file headers
		fileWriter.writerow(['filename', 'future', 'scientists say', 'The United States'])
		for result in results:
			fileWriter.writerow(result)

# Find these ngrams in the files in a given directory
ngramQueries = []
ngramQueries.append(['future'])
ngramQueries.append(['scientists', 'say'])
ngramQueries.append(['the', 'united', 'states'])
directoryPath = "Texts_4"
ngramsProgram(directoryPath, ngramQueries)
