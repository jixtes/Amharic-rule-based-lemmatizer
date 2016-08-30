
# Amharic stemmer
"""
Group members
- Jigsa Tesfaye
- Bersisa Diro
- Mekonnen Molla
"""
import sys,os,re,json

def transliterate(user_input):
	trans_file = open('dictionary/transliterator/transliterator.min.json','r')
	trans_data = json.loads(trans_file.read())
	trans_file.close()
	trans_data = eval(trans_data)

	characters = re.findall('\w',user_input)

	for char in characters:
		
		if char in trans_data:
			print(char+' = '+trans_data[char])
			user_input = re.sub(char,trans_data[char],user_input)

	return user_input


def stem(input1):
	
	# RULE 1 - Take input as it is
	print(input1)
	collection = [input1]

	# RULE 2 - Take out the right most suffix - From input 1
	input2 = re.match("(.+)(iwu|wu|wi|awī|na|mi|ma|li|ne|ache)",input1)
	if input2:
		print(input2.group(1)+'-'+input2.group(2)) 
		input2 = input2.group(1); 
		collection.append(input2)
	else:
		input2 = input1

	# RULE 3 - Take out the inner most suffix
	input3 = re.match('(.+)(ochi|bache|wache)',input2)	
	input3 = re.match('(.+)(chi|ku|ki|ache|wal)',input2) if not input3 else input3
	if input3:
		print(input3.group(1)+'-'+input3.group(2))
		input3 = input3.group(1)
		collection.append(input3)
	else:
		input3 = input2	
	
	# RULE 4 - Take out the most left prefix - From input 1
	input4 = re.match('(yete|inide|inidī|āli)(.+)',input1)
	input4 = re.match('(ye|yi|masi|le|ke|inid|be|sile)(.+)',input1) if not input4 else input4
	if input4:
		print(input4.group(1)+'-'+input4.group(2))
		input4 = input4.group(2)
		collection.append(input4)
	else:
		input4 = input1	
	
	# RULE 5 - Take out the right most suffix - From input 4
	input5 = re.match('(.+)(iwu|wu|w|awī|na|mi|ma|li|ne|che)',input4)
	if input5: 
		print(input5.group(1)+'-'+input5.group(2))
		input5 = input5.group(1)
		collection.append(input5)
	else:
		input5 = input4

	# RULE 6 - Take out the inner most suffix - From input 4
	input6 = re.match('(.+)(ochi|bache|wache)',input5)	
	input6 = re.match('(.+)(chi|ku|ki|che|wal)',input5) if not input6 else input6
	if input6:
		print(input6.group(1)+'-'+input6.group(2))
		input6 = input6.group(1)
		collection.append(input6)
	else:
		input6 = input5
	
	# RULE 7 - Take out the inner most prefix - From input 1
	input7 = re.match('(te|mī|mi|me|mayit|ma|bale|yit)(.+)',input4)
	if input7:
		print(input7.group(1)+'-'+input7.group(2))
		input7 = input7.group(2)
		collection.append(input7)
	else:
		input7 = input4

	# RULE 8 - Take out the right most suffix - From input 7
	input8 = re.match('(.+)(iwu|wu|w|awī|na|mi|ma|li|ne)',input7)
	if input8: 
		print(input8.group(1)+'-'+input8.group(2)); 
		input8 = input8.group(1)
		collection.append(input8)
	else: 
		input8 = input4
	

	# RULE 9 - Take out the innermost suffix - From input 8
	input9 = re.match('(.+)([^iīaeou])’?',input8)
	if input9:
		print(input9.group(1)+'-'+input9.group(2)); 
		input9 = input9.group(1)
		collection.append(input9)
	else:
		input9 = input4

	print(collection)

	return collection

def disambuigate(stems):
	dictionary = open('dictionary/amh_lex_dic.trans.txt','r')
	lexical_data = dictionary.read()
	dictionary.close()
	
	match = None
	string_size = 0
	for stem in stems:
		temp = re.search('('+stem+') {(.+)}',lexical_data)
		if temp:
			print(temp.group(1))
			if(len(stem) > string_size):
				string_size = len(stem)
				match = temp
		else:
			# Rule 10
			stem = re.match(r'(.+)[īaou]\b',stem)
			if stem:
				stems.append(re.sub(r'(.+)[īaou]\b',r'\1e',stem.group()))
				stems.append(re.sub(r'(.+)[īaou]\b',r'\1i',stem.group()))

	return match

def main():
	user_input = input("Input an Amharic Word to be stemmed: ")
	
	print('\nNormalize and transliterate...')
	user_input = transliterate(user_input)

	print('\nStemming...')
	stems = stem(user_input)

	if (len(stems) > 1):
		print('\nDisambuigating...')
		output = disambuigate(stems)

		if output:
			print('\n'+output.group())
		else:
			print(stems)
	else:
		print('\n'+stems)




main()