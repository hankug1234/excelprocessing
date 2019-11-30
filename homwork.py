from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import pandas as pd
import re

sentences = list()

with open("C:/Users/LG/analysis/resources/resources/beatles_biography.txt",encoding="UTF8") as file:
    for line in file:
        for l in re.split(r"\.\s|\?\s|\!\s|\n",line):
            if l:
                sentences.append(l)

cvec = CountVectorizer(stop_words="english",min_df=3,max_df=0.5,ngram_range=(1,2))
sf = cvec.fit_transform(sentences)

transformer = TfidfTransformer()
transformed_weights = transformer.fit_transform(sf)
weight = np.asarray(transformed_weights.mean(axis=0)).ravel().tolist()
weights_df = pd.DataFrame({'term':cvec.get_feature_names(),'weight':weight})

print(weights_df.sort_values(by='weight',ascending=False).head(10))