# Tvým úkolem je vytvořit program, který bude získávat data z obchodního rejstříku s využitím jeho REST API.

#část1
#V této části vyhledej informace o konkrétním subjektu na základě jeho identifikačního čísla (IČO).
# Toto číslo je jedinečným identifikátorem subjektu, pro každé číslo tedy rejstřík vrátí informace pouze o jednom subjektu.
# Nejprve se pomocí funkce input() zeptej uživatele nebo uživatelky, o kterém subjektu chce získat informace.
# S využitím modulu requests odešli GET požadavek na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/ICO,
# kde ICO nahraď číslem, které zadal(ka) uživatel(ka).
# S adresou pracuj jako s obyčejným řetězcem, tj. můžeš využívat formátované řetězce, metodu .replace(), operátor + atd.
# Text, který API vrátí, převeď na JSON a zjisti z něj obchodní jméno subjektu a adresu jeho sídla (můžeš využít podle textovaAdresa).
# Získané informace vypiš na obrazovku.
#Například pro IČO  by 22834958 tvůj program měl vypsat následující text.

import requests

ico = input("Zadej IČO subjektu: ")
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/"

response = requests.get(url+ico)
subject = response.json()

print(subject["obchodniJmeno"])
print(subject["sidlo"]["textovaAdresa"])

#část2
#Často se stane, že neznáme IČO subjektu, ale známe například jeho název nebo alespoň část názvu.
# Napiš program, který se zeptá uživatele(ky) na název subjektu, který chce vyhledat.
# Následně vypiš všechny nalezené subjekty, které ti API vrátí.
#V případě vyhledávání musíme odeslat požadavek typu POST na adresu https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat.
# Request typu POST pošleme tak, že namísto funkce requests.get() použijeme funkci requests.post(). 
#K requestu musíme přidat hlavičku (parametr headers), který určí formát výstupních dat. Použij slovník níže.
#headers = {
#    "accept": "application/json",
#   "Content-Type": "application/json",
#}
#Dále přidáme parametr data, do kterého vložíme řetězec, který definuje, co chceme vyhledávat.
# Data vkládáme jako řetězec, který má JSON formát. Pokud chceme například vyhledat všechny subjekty,
# které mají v názvu řetězec "moneta", použijeme následující řetězec.
#data = '{"obchodniJmeno": "moneta"}'

#Tentokrát API vrátí počet nalezených subjektů (pocetCelkem) a seznam nalezených subjektů ekonomickeSubjekty.
# Tvůj program by měl vypsat obchodní jména všech nalezených subjektů a jejich identifikační čísla, výstupy odděluj čárkou.
# Příklad výstupu pro "moneta" je níže.

import requests
import json

nazev = input("Zadej název subjektu: ").strip()
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}
data = json.dumps({"obchodniJmeno" : nazev})
url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

response = requests.post(url, headers=headers, data=data)
data = response.json()

print(len(data ["ekonomickeSubjekty"]))
#nebo
print(data["pocetCelkem"])


for subjekt in data["ekonomickeSubjekty"]:
    print(f'{subjekt["obchodniJmeno"]}, {subjekt["ico"]}')
