from flask import Flask, redirect, url_for, request,jsonify
import warnings
import nltk
from nltk.tag.stanford import StanfordNERTagger
import os, string

warnings.filterwarnings('ignore')


app = Flask(__name__)


@app.route('/cari', methods = ['POST','GET'])
def cari():
	if request.method == 'POST':
		sentence = request.form['kalimat']

		sentence = sentence.strip()
		#return "Kode Barang "+kode
		java_path = "/usr/lib/jvm/java-1.11.0-openjdk-amd64"
		os.environ['JAVA_HOME'] = java_path

		#sentence = "klinik uteri di amerika "

		jar = './stanford-ner-tagger/stanford-ner.jar'
		model = './stanford-ner-tagger/my-ner-model-indo-bio.ser.gz'

		ner_tagger = StanfordNERTagger(model, jar, encoding='utf8')

		#sentence = sentence.lower()
		sentence = sentence.translate(str.maketrans('','',string.punctuation)).lower()

		words = nltk.word_tokenize(sentence)
		#print(ner_tagger.tag(words))

		hasil = ner_tagger.tag(words) 

		# mydict = {}

		# for i in hasil:
		# 	if(str(i[1]) == 'O'):
		# 		continue
		# 	#print(i[0], ':', i[1] )
		# 	if i[1]=="I-PENYAKIT":
		# 		keyword = "Spesialis"
		# 	elif i[1]=="I-LOKASI":
		# 		keyword = "Lokasi"

		# 	mydict[keyword] = i[0]

		
		mydict = {}

		for i in hasil:
			if(str(i[1]) == 'O'):
				continue
			
			mydict[i[1]] = i[0]

		#print(ner_tagger.tag(words))

		#hasil adalah object data json
	return jsonify(mydict)

if __name__ == '__main__':
	app.run(debug = True)
