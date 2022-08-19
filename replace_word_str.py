def highlight_word(sentence, word):
	return(' '.join([words.replace(word, word.upper()) for words in sentence.split()]))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
