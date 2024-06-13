# Inizializzazione del progetto

Questo file fornisce istruzioni su come inizializzare il progetto utilizzando `docker-compose` e migrare le tabelle.

## Prerequisiti

Assicurati di avere installato Docker e Docker Compose sul tuo sistema.

## Passaggi

1. Clona il repository del progetto:

    ```bash
    git clone <URL_DEL_REPOSITORY>
    ```

2. Naviga nella directory del progetto:

    ```bash
    cd GestionaleLuca
    ```

3. Esegui il comando `docker-compose up --build` per avviare i container Docker:

    ```bash
    docker-compose up --build
    ```

4. Apri un nuovo terminale e naviga nella directory del progetto.

5. Esegui il comando `docker-compose exec app php artisan migrate` per eseguire la migrazione delle tabelle:

    ```bash
    docker-compose exec app python manage.py migrate
    ```

Ora il progetto è stato inizializzato correttamente e le tabelle sono state migrate.

## Risoluzione dei problemi

- Se incontri problemi durante l'esecuzione dei comandi `docker-compose`, assicurati di avere i privilegi di amministratore o di essere un utente nel gruppo `docker`.

- Se riscontri errori durante la migrazione delle tabelle, verifica la configurazione del database nel file `.env` e assicurati che sia corretta.

- Per ulteriori informazioni su come utilizzare il progetto, consulta la documentazione nel repository del progetto.
