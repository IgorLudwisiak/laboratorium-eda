# Analiza sprzedazy

Projekt wykonany w ramach laboratorium z eksploracji danych.

## Dane
Fikcyjne zamowienia (12 wierszy): kanal sprzedazy, segment i wartosc w zl.

## Analizy
Czyszczenie nazw kanalow, liczba zamowien, suma, srednia i mediana, sprzedaz wedlug kanalu.

## Uruchomienie lokalne
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

## Technologie
Python, pandas, Jupyter, Streamlit, GitHub, Render

## Aplikacja
https://laboratorium-eda-jekb.onrender.com

## Wnioski
1. Kanal internetowy daje wieksza sprzedaz (1490 zl) niz sklep (760 zl).
2. Liczba zamowien jest taka sama (po 6), wiec przewaga internetu wynika z wyzszej sredniej wartosci zamowienia.