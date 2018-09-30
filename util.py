import sys
import numpy as np
from keras.preprocessing.text import text_to_word_sequence
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.recurrent import LSTM
from keras.utils import to_categorical
from keras.models import load_model

def words2ids(input, dict_glove):
    seq = np.zeros((1, 39, 200))

    for i, word in enumerate(input):
        if i <39:
            if word in dict_glove:
                seq[0][i] = dict_glove[word]
    return seq

def _function(sentence):
    d = np.load('Dict_3.npy').item()
    sentence = sentence.split()
    ids = words2ids(sentence, d).reshape(-1, 39, 200)

    result = 0
    model_list = ["model_submission/model-007-0.8171.h5", "model_submission/model-026-0.8177.h5", "model_submission/model-026-0.8200.h5", "model_submission/model-015-0.8214.h5", "model_submission/model-041-0.8205.h5", "model_submission/model-029-0.8202.h5", "model_submission/model-021-0.8204.h5"]
    for models in model_list:
        model = load_model(models)
        result = model.predict(ids) + result
    result = result / len(model_list)

    return result

    