import shutil
import fnmatch
import glob, os,re

liste=[]
os.chdir("C:/Users/HP/Desktop/step3/books")
for fil in glob.glob("*.txt"):
    liste.append(fil)

for fil in liste:
    string=fil.split("_")
    #get only digits
    string=re.sub("\D", "", string[2].replace(".txt",""))
    if string!="":
        if 1 <= int(string) <= 40:
            shutil.move("C:/Users/HP/Desktop/step3/books/"+fil, "C:/Users/HP/Desktop/step3/books/1-40/"+fil)
        if 40 <= int(string) <= 132:
            shutil.move("C:/Users/HP/Desktop/step3/books/"+fil, "C:/Users/HP/Desktop/step3/books/40-132/"+fil)
        if 132 <= int(string) <= 656:
            shutil.move("C:/Users/HP/Desktop/step3/books/"+fil, "C:/Users/HP/Desktop/step3/books/132-656/"+fil)
        if 656 <= int(string) <= 1213:
            shutil.move("C:/Users/HP/Desktop/step3/books/"+fil, "C:/Users/HP/Desktop/step3/books/656-1213/"+fil)
        if 1213 <= int(string):
            shutil.move("C:/Users/HP/Desktop/step3/books/"+fil, "C:/Users/HP/Desktop/step3/books/1213-now/"+fil)
        
            



