from flask import Flask, render_template
app = Flask(__name__)

class Item:
    def __init__(self, name):
        self.name = name

nimi = "Essi Esimerkki"

lista = [1, 1, 2, 3, 5, 8, 11]

esineet = []
esineet.append(Item("Eka"))
esineet.append(Item("Toka"))
esineet.append(Item("Kolmas"))
esineet.append(Item("Neljäs"))

#Luodaan render_template funktion avulla näkymä index.html:stä
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/demo")
def content():
    return render_template("demo.html", nimi=nimi, lista=lista, esineet=esineet)

#ohjeistavat sovelluksen käynnistymään kun se suoritetaan komentoriviltä
#debug=True: debug-moodi muuntaa sovelluksen toimintaa muunmuassa siten, että sovelluksen uudelleenkäynnistäminen muutosten yhteydessä ei ole tarpeellista
#debug tila ei saa olla päällä, kun sovellus on viety tuotantoon!! Kun se on kaikkien käytettävissä!
if __name__ == "__main__":
    app.run(debug=True)