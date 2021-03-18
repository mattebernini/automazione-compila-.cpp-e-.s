import os
import subprocess
import sys

file_cpp = []
file_s = []
file_exe = []
quanti_exe = 1
comando = "g++ "

os.chdir(sys.argv[1])

# nome all'exe 
for cartella, sottocartelle, files in os.walk(os.getcwd()):
    for file in files:
        if file.startswith("exe"):
            file_exe.append(file)
for e in file_exe:
    quanti_exe += 1
comando += "-o exe" + str(quanti_exe) + " "


for cartella, sottocartelle, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".cpp"):
            file_cpp.append(file)
        if file.endswith(".s"):
            file_s.append(file)

include = []
include = file_s
for c in file_cpp:
    esiste = False
    for s in include:
        if c.replace(".cpp", "") == s.replace(".s", ""):
            esiste = True
    if esiste == False:
        include.append(c)

for i in include:
    comando += i + " "


os.system("cd '" + sys.argv[1] + "'")
os.system(comando)
print(comando)