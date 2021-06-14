"""
W ramach obchodów miedzynarodowego swieta cyklistów organizatorzy przewidzieli górska
wycieczke rowerowa. Bedzie sie ona odbywac po bardzo waskiej sciezce, na której rowery moga
jechac tylko jeden za drugim. W ramach zapewnienia bezpieczenstwa kazdy rowerzysta bedzie
miał numer identyfikacyjny oraz małe urzadzenie, przez które bedzie mógł przekazac
identyfikator rowerzysty przed nim (lub -1 jesli nie widzi przed soba nikogo). Nalezy napisac
funkcje, która na wejsciu otrzymuje informacje wysłane przez rowerzystów i oblicza rozmiar
najmniejszej grupy (organizatorzy obawiaja sie, ze na małe grupy mogłyby napadac dzikie
zwierzeta). Dane sa nastepujace struktury danych:
struct Cyclist {
int id, n_id; // identyfikator rowerzysty oraz tego, którego widzi
};
Funkcja powinna miec prototyp int smallestGroup( Cyclist cyclist[], int n ), gdzie
cyclist to tablica n rowerzystów. Funkcja powinna byc mozliwie jak najszybsza. Mozna załozyc,
ze identyfikatory rowerzystów to liczby z zakresu 0 do 10^8 (osiem cyfr napisanych w dwóch
rzedach na koszulce rowerzysty) i ze pamiec nie jest ograniczona. Rowerzystów jest jednak duzo
mniej niz identyfikatorów (nie bez powodu boja sie dzikich zwierzat). Nalezy zaimplementowac
wszystkie potrzebne struktury danych.

"""
