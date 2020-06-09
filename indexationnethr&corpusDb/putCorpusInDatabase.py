import xml.etree.ElementTree as ET
import pyarabic.araby as araby
import re
import lxml
from lxml import etree
import xlwt
import codecs
import xlsxwriter

def header(filename,dbname):   
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    c.execute('''CREATE TABLE if not exists stock 
             (author text, book text , sentence text,phrase text)''')
    
    tree = ET.parse(filename).getroot() #read in the XML
    for item in tree.findall("text"):
        for author in item.findall("author"):import sqlite3

            for book in author.findall("book_title"):
                for sentence in book.findall("sentence"):
                    try:
                        words=araby.tokenize(sentence.text)
                        word=' '.join(words)
                        c.execute("INSERT INTO stock VALUES ('"+str(author.attrib.get('id'))+"','"+str(book.get('id'))+"','"+str(sentence.get('id'))+"','"+word+"')")
                    except:
                        pass                
                conn.commit()
    
    conn.close()
    
header("corpus_العصر الحديث.xml","corpus_data_base_العصر الحديث.db")#CHANGE
   