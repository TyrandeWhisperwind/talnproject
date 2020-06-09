import xml.etree.ElementTree as ET
import pyarabic.araby as araby
import re
import lxml
from lxml import etree
import xlwt
import codecs
import xlsxwriter
import sqlite3

def header(filename,dbname):   
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists stock 
             (author text, poem_title text , couple text,phrase text)''')
    
    tree = ET.parse(filename).getroot() #read in the XML
    for item in tree.findall("author"):
        for author in item.findall("poem-title"):
                for sentence in author.findall("couple"):
                    try:
                        words=araby.tokenize(sentence.text)
                        word=' '.join(words)
                        c.execute("INSERT INTO stock VALUES ('"+str(item.attrib.get('id'))+"','"+str(author.get('id'))+"','"+str(sentence.get('id'))+"','"+word+"')")
                    except:
                        pass                
                conn.commit()
    
    conn.close()
    
header("djahili.xml","corpus_data_base_poem_djahili.db")#CHANGE
   