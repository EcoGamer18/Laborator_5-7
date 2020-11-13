<h3>Documentatie - Laborator 5-7 Program pentru gestionarea unui inventar </h3>

**Enunt**

  ***B.Scrieți un program pentru gestionarea unui inventar  dintr-o instituție.***

  Vor  fi  suportate operațiile:

  1. Adăugare / ștergere / modificareobiect: se efectuează pe bază de număr de inventar/ ID. Un obiect conține: ID, nume, descriere (nenule), preț achiziție, locație (4 caractere). 
  2. Mutarea tuturor obiectelor dintr-o sală în alta.
  3. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
  4. Determinarea celui mai mare preț pentru fiecare locație.
  5. Ordonarea obiectelor crescător după prețul de achiziție.
  6. Afișarea sumelor prețurilor pentru fiecare locație.
  7. Undo.

**Functionalitati**

Functionalitate|Descriere
---------------|----------
adaugarea_obiect|Adaugarea unui obiect la lista cu obiecte.
sterge_obiect|Stergerea unui obiect cu id dat din lista de obiecte.
modificare_obiect|Modificarea unui obiect cu id dat din lista de obiecte.
mutare_locatie|Mutarea tuturor obiectelor dintr-o sală în alta.
concatenare_descriere|Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citită.
cel_mai_mare_pret_per_locatie|Afisarea celui mai mare preț pentru fiecare locație.
ordonare_crescatoare_pret|Ordonarea obiectelor crescător după prețul de achiziție.
suma_preturi_per_locatie|Afișarea sumelor prețurilor pentru fiecare locație.


**Lista de activitati**

Functionalitate|Activitate|Descriere|Cazuri de testare
---------------|----------|---------|-----------------
mutare_locatie|A1|Citirea salii din care vrem sa mutam obiectele|E1S2(caz bun)<br>EPrS55(caz care da eroare)
<br>|A2|Citirea salii in care vrem sa mutam obiectele|E2S5(caz bun)<br>ERRs54(caz de eroare)
<br>|A3|Modificarea locatiei obiectelor din lista
<br>|A4|Updatarea listei de obiecte cu varianta noua a lor
concatenare_descriere|A1|Citirea unui pret|1598(caz bun)<br>sad554(caz care da eroare)
<br>|A2|Citire sirului care va fi concatenat obiectelor cu pret mai mare decat valoarea data|"dsdsa"(caz bun)
<br>|A3|Modificarea obiectelor din lista care indeplinesc conditia data
<br>|A4|Updatarea liste de obiecte cu varianta noua a obiectelor
cel_mai_mare_pret_per_locatie|A1|Crearea unei liste de dictionare de forma{"locatie":"str locatie","pret_maxim" : pret}|
<br>|A2|Introducerea in lista dictionare cu locatiile obiectelor si pretului maxim aflat la locatia respectiva|
<br>|A3|Afisarea listei de dictionare|
ordonare_crescatoare_pret|A1|Ordonarea listei de obiecte dupa pret|
<br>|A2|Updatarea listei de obiecte cu lista ordonata|
suma_preturi_per_locatie|A1|Crearea unei liste de dictionare de forma{"locatie":"str locatie","suma_preturi" : preturi}|
<br>|A2|Introducerea in lista dictionare cu locatiile obiectelor si pretului aflat la locatia respectiva|
<br>|A3|Sumarea preturilor din fiecare locatie|
<br>|A4|Afisarea listei de dictionare|


