# automazione-compila-.cpp-e-.s
Compila tutti i file .s in una cartella, quelli .cpp che hanno nome diverso dai file .s e li esegue creando un file eseguibile.

PREREQUISITI:
OS Linux (Ubuntu o Debian, per le altre distro non ho verificato)
interprete Python

SETUP:
1. sostituire nel file compila.sh l'indirizzo di dove viene salvato il file c++.py
2. inserire il contenuto del file compila.sh in fondo al file .bashsr (/home/nomeUtente/.bashrc)
3. da terminale > $ source ~/.bashrc
4. per compilare basta andare nella cartella contenente i file interessati e scrivere da terminale compila, verrà creato un file exe0
5. per vedere il risultato > $ ./exe0

*il comando si chiama compila ma in realtà compila ed esegue i file della cartella corrente*
*utilizzare soltanto se si è interessati a compilare ed eseguire TUTTI i file della cartella, con precedenza ai file .s*(tra due file main.cpp e main.s il programma compila ed esege main.s)
