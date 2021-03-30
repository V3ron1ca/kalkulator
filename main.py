import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    return x / y

text = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

x= float(input("Podaj liczbe 1: "))
y = float(input("Podaj liczbe 2: "))

if text == '1':
    print("Dodaje", x , "i" , y )
    print("Wynik to" , dodawanie(x, y))
    logger.info("Teraz dodaje dwie liczby")

elif text == '2':
    print("Odejmuje", x , "i" , y )
    print("Wynik to" , odejmowanie(x,y))
    logger.info("Teraz odejmuje dwie liczby")

elif text == '3':
    print("Mnoże", x , "i" , y )
    print("Wynik to", mnozenie(x,y))
    logger.info("Teraz mnozy dwie liczby")

elif text == '4':
    print("Dziele", x , "i" , y )
    print("Wynik to" , dzielenie(x,y))
    logger.info("Teraz dzieli dwie liczby")