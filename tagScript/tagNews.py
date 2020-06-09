import re,os,fnmatch,glob

def split_sentences(st):
    sentences = re.split(r'[.?!]\s*', st)
    if sentences[-1]:
        return sentences
    else:
        return sentences[:-1]
###############################################################################################
corpus=open("C:/Users/HP/Desktop/TAL/Projet/scond step/corpus_العصر الحديث.txt",encoding="utf-8",mode="w")#create a new tagged curpos
corpus.write("<t>")
corpus.write("<news id=\"العصر الحديث\">")
corpus.write("\n")
liste=[]
listeSentences=[]
#change this!
for x in os.listdir('.'):#list all the dir of current folder
    if os.path.isdir(x): 
        corpus.write("<news-title id=\""+x+"\">"+"\n")
        for y in os.listdir(x):
            corpus.write("<category id=\""+y+"\">"+"\n")
            os.chdir("C:/Users/HP/Desktop/TAL/Projet/scond step/1213-now/"+x+"/"+y)#all the files 
            
            data=""
            for Name_file in glob.glob("*.txt"):
                with open(Name_file,encoding="utf-8", mode='r') as myfile:#for each file:
                    data=data+" "+myfile.read().replace('\n', ' ')#i'v got the files in a sting named data
                    myfile.close()
            i=0
            listeSentences=split_sentences(data)#file splited by sentence with the fucntion split_sentence
            for sentence in listeSentences:
                corpus.write("<sentence id=\""+str(i)+"\">")
                filtredPage= re.sub(r"<.*>", '', sentence, flags=re.IGNORECASE)
                corpus.write(filtredPage)
                corpus.write("</sentence>")
                i+=1

            corpus.write("\n")
            corpus.write("</category>"+"\n")
        corpus.write("</news-title>"+"\n")
corpus.write("</news>")
corpus.write("</t>")
