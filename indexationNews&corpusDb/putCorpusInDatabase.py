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
             (author text, book text , sentence text,phrase text)''')
    
    tree = ET.parse(filename).getroot() #read in the XML
    for item in tree.findall("news"):
        for author in item.findall("news-title"):
            for book in author.findall("category"):
                for sentence in book.findall("sentence"):
                    try:
                        words=araby.tokenize(sentence.text)
                        word=' '.join(words)
                        c.execute("INSERT INTO stock VALUES ('"+str(author.attrib.get('id'))+"','"+str(book.get('id'))+"','"+str(sentence.get('id'))+"','"+word+"')")
                    except:
                        pass                
                conn.commit()
    
    conn.close()
    
header("corpus_news_العصر الحديث.xml","corpus_data_base_news_العصر الحديث.db")#CHANGE
   