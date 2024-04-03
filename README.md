# Pong Game

## Introduzione
Il programma "Pong Game" è una semplice implementazione del classico gioco Pong sviluppato da Agnello Renato Nicolae in occasione della quarta giornata del percorso svolto in classe con il tutoraggio dell'Università Politecnica delle Marche (UNIPM). Utilizza la libreria Pygame in linguaggio di programmazione Python.

## Requisiti
Per eseguire correttamente il programma sono necessari i seguenti requisiti:
- Python 3.x ([Python.org](https://www.python.org/))
- Pygame ([Pygame.org](https://www.pygame.org/))

## Avvio del programma
Per avviare il programma, seguire questi passaggi:
1. Assicurarsi di avere Python e Pygame installati correttamente sul proprio sistema operativo.
2. Scaricare tutti i file del progetto, inclusi eventuali file audio necessari (ad esempio, il file "boing.mp3").
3. Aprire un terminale o una finestra di comando.
4. Navigare nella directory in cui sono presenti i file del progetto.
5. Eseguire il file `pong.py` con Python utilizzando il seguente comando:

```bash
python pong.py
```


## Funzionamento
Il gioco "Pong" è un classico gioco arcade in cui due giocatori controllano delle piattaforme e devono rimandare una palla avanti e indietro, cercando di far passare la palla oltre la piattaforma avversaria per ottenere un punto.

Nella versione implementata in questo programma, il giocatore controlla una sola piattaforma e deve far rimbalzare una palla all'interno dell'area di gioco. I controlli sono i seguenti:
- Utilizzare le frecce direzionali destra e sinistra (o i tasti WASD) per muovere la piattaforma orizzontalmente.
- La palla rimbalza sui bordi dello schermo e sulla piattaforma.
- Ogni volta che la palla colpisce la piattaforma, il punteggio aumenta di uno.
- Il gioco continua finché la palla non supera il bordo inferiore dello schermo.
- È possibile cambiare il colore dello sfondo premendo i seguenti tasti:
- `R` per impostare lo sfondo di colore rosso.
- `G` per impostare lo sfondo di colore verde.
- `M` per disabilitare il suono.
- `U` per abilitare il suono.

## Crediti
Il programma è stato sviluppato da Agnello Renato Nicolae.
L'Università Politecnica delle Marche (UNIPM) ha fornito il tutoraggio e l'ambiente per lo sviluppo del progetto.
