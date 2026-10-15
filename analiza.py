import pandas as pd


def wczytaj_dane(sciezka):
    return pd.read_csv(sciezka, sep=";")


def wyczysc_dane(df):
    wynik = df.copy()
    wynik["kanal"] = wynik["kanal"].str.strip().str.lower()
    return wynik


def podsumowanie(df):
    return {
        "liczba": len(df),
        "suma": df["wartosc"].sum(),
        "srednia": df["wartosc"].mean(),
        "mediana": df["wartosc"].median(),
    }


def sprzedaz_wg_kanalu(df):
    wynik = df.groupby("kanal", as_index=False)["wartosc"].sum()
    return wynik.rename(columns={"wartosc": "suma_sprzedazy"})