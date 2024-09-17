from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#preparing datasets of text and corresponding labels for testing:
texts = [
  'I love programming.', 'Python is amazing.',
  'I enjoy machine learning.', 'The weather is nice today.', 'I like algo.',
  'Machine learning is fascinating.', 'Natural Language Processing is a part of AI.'
]

labels = [
  'tech', 'tech', 'tech', 'non-tech', 'tech', 'tech', 'tech'
]

#convert the data into a matrix of tokens:
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(texts)

#split the data into training and testing sets:
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

#train the model on our training data:
model = MultinomialNB()
model.fit(x_train, y_train)

#make predictions on test sets (used trained model to predict the labils for test sets):
y_pred = model.predict(x_test)

#evaluate model's accuracy:
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)