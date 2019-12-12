#!/usr/bin/python3
#Chris Huffman
#12/9/19

import pickle

credentials = {'admin':['secret',' what is 1 plus 1?', '42'], 'ghopper': ['cricket','What is your favorite animal?','42']}

pickle_jar = open("./pmsaves/dictionary.pickle", "wb")
pickle.dump(credentials, pickle_jar)
pickle_jar.close()
pickle_jar = open("./pmsaves/dictionary.pickle", "rb")
credentials = pickle.load(pickle_jar)
pickle_jar.close()

print(credentials)
