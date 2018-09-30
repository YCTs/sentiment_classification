import tensorflow as tf
import sys
import numpy as np
from keras.preprocessing.text import text_to_word_sequence
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.recurrent import LSTM
from keras.utils import to_categorical
from keras.models import load_model
from util import _function
def input_from_stdin(input, dict_glove):
	seq = np.zeros((1, 39, 200))

	for i, word in enumerate(input):
		if i <39:
			if word in dict_glove:
				seq[0][i] = dict_glove[word]
	return seq

def main(args):
    

	print(_function("thank you"))
	'''
	d = np.load('Dict_3.npy').item()
	input = None
	while(True):
		print("Sentence: ")
		input = sys.stdin.readline().strip('\n')
		if input == "exit":
			break	
		input_ = input.split()
		seq = input_from_stdin(input_, d).reshape(-1, 39, 200)
		
		result = 0
		for models in args[1:8]:
			model = load_model(models)
			result = model.predict(seq) + result
		result = result / len(args[1:8])

		print("Score: ", result)
	'''



if __name__ == '__main__':
	main(sys.argv)