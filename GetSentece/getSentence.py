import sqlite3,re
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

def GetSentenceNethr(mot,indexedb,corpusdb):
    fil=open("text.txt",encoding='utf-8',mode='w')
    ListeBalise=[]
    conn = sqlite3.connect(indexedb)
    cursor=conn.execute('SELECT mot FROM stocks')
    for row in cursor:
        if(deNoise(row[0])==mot):
            devocalizedWord=deNoise(row[0])

    t = (devocalizedWord,)
    cursor=conn.execute('SELECT balises FROM stocks WHERE mot=?',t)
    
    for row in cursor:
        ListeBalise=row[0].split(",")
    ListSentence=[]
    conn = sqlite3.connect(corpusdb) 
    for element in ListeBalise:
        cursor=conn.execute('SELECT phrase FROM stock WHERE author=? and book=? and sentence=?', (element.split("/")[1].split("=")[1],element.split("/")[2].split("=")[1], element.split("/")[3].split("=")[1]))
        for row in cursor:
            ListSentence.append(row[0])
    for el in ListSentence:
        fil.write(str(el))
        fil.write("\n")
    conn.close()


GetSentenceNethr("بسم","indexe_عصر الدول المتتابعة.db","corpus_data_base_عصر الدول المتتابعة.db",)#CHANGE
