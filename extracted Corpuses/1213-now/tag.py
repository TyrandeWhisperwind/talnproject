import re,os,fnmatch,glob

def split_sentences(st):
    sentences = re.split(r'[.?!]\s*', st)
    if sentences[-1]:
        return sentences
    else:
        return sentences[:-1]
###############################################################################################
os.chdir("C:/Users/HP/Desktop/TAL/Projet/scond step/1213-now")#all the files of that phase
corpus=open("C:/Users/HP/Desktop/TAL/Projet/scond step/corpus_العصر الحديث.txt",encoding="utf-8",mode="w")#create a new tagged curpos
corpus.write("<t>")
corpus.write("<text id=\"العصر الحديث\">")#tag of the phase (656-1213 hidjri)
corpus.write("\n")
liste=[]
listeSentences=[]
for Name_file in glob.glob("*.txt"):
    i=0
    liste=Name_file.split('_')#exemple : my files r named like this : نهاية الأرب في فنون الأدب_النويري_721هـ .txt, so....
    corpus.write("<author id=\""+liste[1]+"\">"+"\n")
    corpus.write("<book_title id=\""+liste[0]+"\">"+"\n")

    with open(Name_file,encoding="utf-8", mode='r') as myfile:#for each file:
        data=myfile.read().replace('\n', ' ')#i'v got the file in a sting named data
    
    listeSentences=split_sentences(data)#file splited by sentence with the fucntion split_sentence
    for sentence in listeSentences:
        corpus.write("<sentence id=\""+str(i)+"\">")
        corpus.write(sentence)
        corpus.write("</sentence>")
        i+=1
    corpus.write("\n")
    corpus.write("</book_title>"+"\n")
    corpus.write("</author>"+"\n")
    
corpus.write("</text>")
corpus.write("</t>")
