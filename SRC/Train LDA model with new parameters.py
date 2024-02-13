# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:19:29 2024

@author: Taraneh
"""

import re
import json
import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# Improved preprocessing function
def preprocess_texts(texts):
    stop_words = stopwords.words('english')
    # Additional stopwords can be added to this list
    stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
    texts_out = []
    for text in texts:
        text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)  # Remove URLs
        text = re.sub(r'@\w+', '', text)  # Remove mentions
        text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
        text = re.sub(r"\'", "", text)  # Remove single quotes
        text = gensim.utils.simple_preprocess(str(text), deacc=True)  # De-accent and simple preprocess
        texts_out.append([word for word in text if word not in stop_words and len(word) > 3])  # Remove stopwords and short words
    return texts_out


preprocessed_texts = preprocess_texts(tweets)

# Create Dictionary and Corpus, including filtering extremes
id2word = corpora.Dictionary(preprocessed_texts)
id2word.filter_extremes(no_below=5, no_above=0.5)  # Filter out words in less than 5 documents or in more than 50% of the documents
corpus = [id2word.doc2bow(text) for text in preprocessed_texts]

# Train LDA model with new parameters
lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                       id2word=id2word,
                                       num_topics=5,  # Trying a different number of topics
                                       random_state=100,
                                       chunksize=100,
                                       passes=10,  # Reduced number of passes for quicker iteration
                                       alpha='asymmetric',  # Different alpha setting
                                       eta='auto')  # Auto-tune eta

# Compute Coherence Score
coherence_model_lda = CoherenceModel(model=lda_model, texts=preprocessed_texts, dictionary=id2word, coherence='c_v')
coherence_lda = coherence_model_lda.get_coherence()
print('\nCoherence Score:', coherence_lda)

# Explore the topics
for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))