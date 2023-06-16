from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import uvicorn
import requests
import numpy as np
import re

app = FastAPI()

class FakeNewsClassifier:
  def __init__(self, model, vectorizer):
    self.stopwords = stopwords.words('english')
    self.stopwords.remove('not')
    self.model = model
    self.port_stem = PorterStemmer()
    self.vectorizer = vectorizer

  def stemming(self, content):
    stemmed_content = re.sub('[^a-zA-Z]', ' ', content)
    stemmed_content = stemmed_content.lower()
    stemmed_content = stemmed_content.split()
    stemmed_content = [self.port_stem.stem(word) for word in stemmed_content if not word in self.stopwords]
    stemmed_content = ' '.join(stemmed_content)
    return stemmed_content
  
  def predict(self, author, title, text):
    # Create the content
    content = author + ' ' + title + ' ' + text

    # Stem the content
    stemmed_content = np.array([self.stemming(content)])

    # Vectorize the content
    vectorized_content = self.vectorizer.transform(stemmed_content)

    # Make prediction
    prediction = self.model.predict(vectorized_content)
    return prediction

class InputRequest(BaseModel):
	author: str
	title: str
	text: str

# Load the model from the file
with open('fake-news-classifier.pkl', 'rb') as file:
    model = pickle.load(file)

def predict(author: str, title: str, text):
	pass

@app.post(path = '/is-fake-news')
def is_fake_news(inputRequest : InputRequest):
	data = inputRequest.json()
	data_dictionary = json.loads(data)
	author = data_dictionary['author']
	title = data_dictionary['title']
	text = data_dictionary['text']

	prediction = model.predict(author, title, text)

	return 'News you provided has been classified as: ' + ('Fake' if prediction == 1 else 'Real')

if __name__ == "__main__":
	uvicorn.run(app, host = 'localhost', port = 1337)
	pass