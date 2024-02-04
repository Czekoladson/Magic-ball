import random 

wiadomosci = ["To pewne",
              "Niejasna odpowiedź, spróbój ponownie",
              "Zapytaj ponownie później",
              "Skoncentruj sie i zapytaj ponownie",
              "Moja odpowiedź brzmi nie",
              "To nie wygląda zbyt dobrze",]
print(wiadomosci[random.randint(0, len(wiadomosci) -1)])