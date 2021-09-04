from spacy.matcher import Matcher
import spacy
nlp = spacy.load("en_core_web_sm")

def check_mail(text):
	email = []
	pattern = [{"TEXT":{"REGEX":"[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+"}}]
	matcher = Matcher(nlp.vocab)
	matcher.add("Email",None,pattern)
	doc = nlp(text)
	matches = matcher(doc)
	for macth_id, start, end in matches:
		span = doc[start:end]
		email.append(span.text)
	return email

