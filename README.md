# ReverseProxy by Gregorio Maria Vallé 5^C Informatica 27/11/2023

File di configurazione per una struttura dockerizzata che permette di hostare un servizio web con una scalabilità orizontale, attraverso il load-balance di nginx. 
All'interno della cartella web, troveremo le configurazioni che permettono di creare l'immagine del container per il server js e dentro nginx i file di configurazione per il bilanciamento di carico.
Il programma in python: "test.py" server per testare il che il nostro nginx faccia il proprio lavoro, attraverso il comando: "docker stats" possiamo andare a verificare ciò.
