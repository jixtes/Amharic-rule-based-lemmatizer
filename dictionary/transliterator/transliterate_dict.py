import sys
import os
import re
import json

"""

This is the code used to transliterate the Amharic-Silte Dictionary
(presented in text file) to MRD(Machine readable dictionary)

"""
def main():	
	trans_file = open('transliterator.min.json','r')
	trans_data = json.loads(trans_file.read())
	trans_file.close()
	trans_data = eval(trans_data)

	dict_file = open('../amh_lex_dic.txt','r')
	dict_data = dict_file.read()	
	dict_file.close()

	characters = re.findall('\w',dict_data)

	print ('Transliterating...')

	for char in characters:
		
		if char in trans_data:
			print(char+' = '+trans_data[char])
			dict_data = re.sub(char,trans_data[char],dict_data)

	new_file = open('../amh_lex_dic.trans.txt','w')
	new_file.write(dict_data)
	new_file.close()

main()