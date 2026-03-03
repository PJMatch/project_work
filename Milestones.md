# MILESTONE 1

## Dataset
1. 500 nagranych zdań

## text-to-PJM
* Stworzenie przynajmniej 10 animacji leksykalnych znaków.
* UE5 poprawnie odtwarza sekwencję minimum 3 znaków bez przerwania animacji.
* Płynność animacji ≥ 30 FPS na sprzęcie testowym.
* Poprawne lematyzowanie zdania na poziomie powyżej 80%.

## PJM-to-text
* Stworzenie szkieletów na podstawie How2Sign i Phoenix14t
* Pretraining na Phoenix14T, How2Sign
* WER < 25% (TEST) na Phoenix14-t

# MILESTONE 2

## Dataset
2. 5000 nagranych zdań

## text-to-PJM
* Minimum 30 unikalnych animacji znaków leksykalnych.
* Obsługa alfabetu palcowego (32 litery) oraz liczb od 0 do 20.
* Rozróżnianie 3 typów zdań: oznajmujące, pytające, przeczące
* Co najmniej 70% zdań z posiadanych animacji jest poprawnie zinterpretowanych przez osobę testującą.
* Czas blendu między animacjami ≤ 0.8 sekundy.

## PJM-to-text
* Adaptacja sieci do naszego datasetu
* Fine-tuning sieci na naszym datasecie osiągając skuteczność WER < 60%

# MILESTONE 3

## Dataset

## text-to-PJM
* Minimum 90 unikalnych animacji znaków leksykalnych.
* Każda animacja zaczyna się i kończy w zdefiniowanej pozycji neutralnej.
* Co najmniej 80% zdań z posiadanych animacji jest poprawnie zinterpretowanych przez osobę testującą.
* Czas blendu między animacjami ≤ 0.5 sekundy.
* Dla tego samego zdania system generuje identyczny wynik w 95% przypadków


## PJM-to-text
* WER < 30%
* Vram < 1GB
* < 150ms latency
* > 15fps


# FINAL PROJECT
