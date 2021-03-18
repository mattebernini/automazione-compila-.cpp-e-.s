function compila()
{
    cartella_attuale="$PWD"     # $cartella da dove si chiama "compila"
    cd "# cartella col file c++.py"
    python3 c++.py "${cartella_attuale}" 
    cd "${cartella_attuale}"
}