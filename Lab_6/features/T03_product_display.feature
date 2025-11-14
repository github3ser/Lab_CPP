@T03
Feature: Verificare afișare produs
  Scop: Verificarea corectitudinii afișării unui produs selectat

  Scenario: T03 – Verificare afișare primul produs
    Given utilizatorul deschide pagina "https://adoring-pasteur-3ae17d.netlify.app/mens.html"
    When utilizatorul da click pe primul produs din grid
    Then pagina produsului se deschide
    And titlul produsului este vizibil și corect
    And prețul produsului este vizibil și corect
    When utilizatorul accesează URL-ul invalid al produsului
    Then se afișează mesaj de eroare sau 404