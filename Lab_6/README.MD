## Cum rulezi testele

### 1. Rulează toate testele

Pentru a executa toate scenariile definite în proiect, din directorul rădăcină al proiectului (unde se află folderul `features`), folosește comanda:

```text
behave
```

### 2. Rulează un singur feature

Dacă vrei să rulezi doar un anumit feature, specifică calea către fișierul `.feature`:

```text
behave features/T01_home_page.feature
```

### 3. Rulează testele cu un anumit tag

Pentru a executa doar scenariile marcate cu un anumit tag (ex: `@T01`):

```text
behave --tags=@T01
```

### 4. Rulează testele cu mai multe tag-uri

Poți combina tag-uri pentru a rula mai multe scenarii simultan. Exemplu: rulează scenariile cu tag `@T01` sau `@T02`:

```text
behave --tags="@T01 or @T02"
```

> Notă: Asigură-te că ai activat mediul Python corespunzător și că toate dependențele (`selenium`, `behave`) sunt instalate înainte de rulare.
