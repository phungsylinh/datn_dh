import spacy
from spacy.matcher import PhraseMatcher
from replace import replaces
nlp = spacy.load("en_core_web_sm")
def check_name_phone(text):
	text = text.lower()
	for i, j in replaces.items():
		text = text.replace(i,j)
	name_phone = []
	matcher = PhraseMatcher(nlp.vocab)
	terms = ['iphone 12', 'samsung a5 2017', 'nokia','xaomi mi10','iphone 6','iphone 8','samsung s20']
	pattern = [nlp.make_doc(text) for text in terms]
	matcher.add('term', None, *pattern)
	doc = nlp(text)
	matches = matcher(doc)
	for match_id, start, end in matches:
		span = doc[start:end]
		name_phone.append(span.text)
	return name_phone
	