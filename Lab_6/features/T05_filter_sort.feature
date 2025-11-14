@T05
Feature: Verificare filtrare și sortare a produselor
  Scop: Validarea funcționalității de filtrare și sortare din pagina mens.

  Scenario: T05 – Verificare filtrare / sortare produse
    Given utilizatorul deschide pagina de produse pentru testul T05
    Then pagina de produse se încarcă complet în T05
    When utilizatorul localizează secțiunea de filtre sau sortare
    Then elementul de filtrare sau sortare este vizibil și interactiv
    When utilizatorul selectează o opțiune de filtrare sau sortare
    Then lista de produse se actualizează conform filtrului ales
    Then produsele afișate respectă criteriul de filtrare selectat
    When utilizatorul resetează filtrarea sau selectează opțiunea implicită
    Then lista completă de produse revine pe ecran
