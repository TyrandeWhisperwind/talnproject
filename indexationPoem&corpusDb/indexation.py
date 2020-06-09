import xml.etree.ElementTree as ET
import pyarabic.araby as araby
import re
import lxml
import stopwordsallforms
from lxml import etree
import xlwt
import codecs
import xlsxwriter
import sqlite3


def deNoise(text):
    noise = re.compile(""" ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return text
def deNoiseTatwil(text):
    noise = re.compile("""   ـ     # Tatwil/Kashida
                         """, re.VERBOSE)
    text = re.sub(noise, '', text)
    return text
################################################################################################################
def header(filename,indexename):   
    words=[]
    dictionary = dict()
    conn = sqlite3.connect(indexename)
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists stocks 
             (mot text primary key, balises text, frequence integer)''')
    
    tree = ET.parse(filename).getroot() #read in the XML
    for item in tree.findall("author"):
        for author in item.findall("poem-title"):
                for sentence in author.findall("couple"):
                    balise="author id="+item.attrib.get('id')+"/poem-title id="+author.attrib.get('id')+"/couple id="+sentence.attrib.get('id')
                    words=araby.tokenize(sentence.text)
                    for kalima in words:
                        if( araby.is_arabicword(deNoiseTatwil(kalima)) and  deNoise(kalima) not in stopwordsallforms.STOPWORDS.keys() and kalima!=u"،" and kalima!=u'؛' and kalima!="؟"):
                            #put it in the database,if it doesnt existe otherwise add the tags to that existing word, to do so:
                                #use a dictionary of key as word and value as list of tags 
                                #when finishin making the dictionary, write it in the database
                                if kalima in dictionary:
                                    dictionary[kalima].append(balise)
                                else:
                                    dictionary[kalima] = [balise]

    for key, value in dictionary.items():
        c.execute("INSERT INTO stocks VALUES ('"+key+"','"+','.join(value)+"','"+str(len(value))+"')")
    # Save (commit) the changes
    conn.commit()
    conn.close()
################################################################################################################
header("AsrHadith.xml",'indexe_poem_AsrHadith.db')#CHANGE
