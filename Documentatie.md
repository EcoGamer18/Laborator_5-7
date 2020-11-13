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
  8. Redo.

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


**Scenarii de rulare**

Functionalitate|Program|Utilizator
---------------|-------|----------
mutare_locatie|Introduceti din ce sala vreti sa mutati obiectele.|
<br>|<br>|ddd55
<br>|Sala trebuie sa aiba 4 caractere.|<br>
mutare_locatie|Introduceti din ce sala vreti sa mutati obiectele.|
<br>|<br>|ddd5
<br>|Introduceti in care sala vreti sa mutati obiectele.|<br>
<br>|<br>|d445
<br>|Obiectele au fost mutate in sala data!|
concatenare_descriere|Introduceti un pret.|
<br>|<br>|1547
<br>|Introduceti sirul pe care vreti sa il atasati obiectelor cu pret mai mare decat valoare data.|
<br>|<br>| Apartine din clasa 1 de calitate.
<br>|Sirul dat a fost concatenat la obiectele cu pret mai mare decat cel dat!|
adaugare_obiect|Introduceti id-ul:|
<br>|<br>|5
<br>|Introduceti numele:|
<br>|<br>|Dictionar
<br>|Introduceti descrierea:|
<br>|<br>|Roman
<br>|Introduceti pretul:|
<br>|<br>|452
<br>|Introduceti locatia:|
<br>|<br>|E1S8
<br>|Obiectul a fost adaugat listei.|
sterge_obiect|Introduceti id-ul obiectului pe are vreti sa il stergeti:|
<br>|<br>|4
<br>|Obiectul cu id-ul dat a fost sters din lista.|
modificare_obiect|Introduceti id-ul obiectului pe are vreti sa il modificati:|
<br>|<br>|2
<br>|Introduceti un nume nou sau nimic pentru a nu schimba:|
<br>|<br>|
<br>|Introduceti o descriere noua sau nimic pentru a nu schimba:|
<br>|<br>|Cu coperta din piele
<br>|Introduceti un pret nou sau -1 pentru a nu schimba:|
<br>|<br>|486
<br>|Introduceti o locatie noua sau nimic pentru a nu schimba:|
<br>|<br>|
<br>|Obiectul cu id-ul dat a fost modificat.|



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


