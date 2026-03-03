<<<<<<< dataset
## Dataset
1. Stworzenie datasetu z 500 zdań nagranych przez 10 osób (łącznie 5000 zdań)
2. Sprzęt do nagrywania: Telefony na statywach
3. Format nagrań:
- FHD,
- 30FPS,
- proporcje ekranu 1:1,
- maksymalnie 10 sekund nagrania.
4. Warunki nagrywania:
- światło dzienne lub sztuczne,
- źródło światła jest za kamerą,
- nagrywamy na wysokości barków,
- kamera ustawiona tak aby widoczna była cała sylwetka od pasa w górę,
- brak okrycia wierzchniego,
- dłonie osoby migającej widoczne przez cały czas nagrania.
=======
## PJM-to-text

- Accuracy: WER < 30% 
- Peak VRAM usage < 1GB 
- Throughput > 15fps
- time sign to text < 800ms

Tested on Hardware: ryzen 7 7600 rtx 4070
>>>>>>> main

## Text-to-PJM
1. Stworzenie przynajmniej 90 animacji leksykalnych znaków w blenderze z użyciem Open Mocap.
2. Aplikacja zaczyna wyświetlać animacje nie później niż 3 sekundy po wpisaniu pojedyńczego zdania.
3. Co najmniej 80% zdań z posiadanych animacji jest poprawnie zinterpretowanych przez osobę testującą.
4. Obsługa całego alfabetu (32 liter) + liczby (od 0 do 20).
5. Obsługa zdań pytających, oznajmujących i przeczących.
6. Płynność animacji na poziomie co najmniej 30 fps.
7. Czas blendu między animacjami na poziomie mniejszym niż 0.5 sekund.
8. Gdy w zdaniu pojawi się imię, możliwe jest wyliterowanie go.
10. System poprawnie lematyzuje i przekształca zdania o długości do 15 tokenów w sekwencję glossów w co najmniej 90% przypadków testowych.
11. Dla tego samego zdania system generuje identyczną sekwencję glossów w 95% przypadków.
12. Sprzęt testowy: 
- Procesor graficzny -> NVIDIA GeForce RTX 4060 Ti 
- Procesor CPU -> 13th Gen Intel(R) Core(TM) i7-13700KF 
- Pamięć RAM -> 64.00 GB
- System operacyjny -> Windows 11
