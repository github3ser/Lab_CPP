@T02
Feature: Navigare prin header
  Scop: Verificarea funcționării corecte a meniului principal

  Scenario: T02 – Navigare prin header
    Given utilizatorul este pe pagina de start
    When click pe primul item din meniu
    Then pagina se încarcă fără eroare
    When click pe al doilea item din meniu
    Then pagina se încarcă fără eroare
    When click pe fiecare link din meniu și apoi Back
    Then utilizatorul revine pe homepage
    When utilizatorul face click pe meniuri cu submeniuri
    Then submeniurile sunt vizibile și funcționează
