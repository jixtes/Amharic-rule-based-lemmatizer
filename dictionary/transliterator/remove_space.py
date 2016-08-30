
import re

"""
This is the code used to minify the transliterator producing a python readable
json file

"""

def main():
	source = open('transliterator.json','r')
	data = source.read()
	source.close()

	source = open('transliterator.min.json','w')
	data = re.sub(r'[\n\s]','',data)
	data = re.sub(r'\'\'','\'[]\'',data)
	
	data = source.write(data)
	source.close()

main()