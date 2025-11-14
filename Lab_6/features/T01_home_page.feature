@T01
Feature: Testare homepage
  Scop: Verificarea încărcării corecte a paginii principale și a elementelor principale

  Scenario: T01 – Verificare încărcare homepage
    Given utilizatorul deschide pagina "https://adoring-pasteur-3ae17d.netlify.app/mens.html"
    Then pagina se încarcă complet fără erori
    And header-ul și meniul sunt vizibile
    And sunt afișate cel puțin 3 produse
    And footer-ul conține linkul "Contact"
