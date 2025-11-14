@T06
Feature: Verificare funcționalitate logo pentru navigarea spre homepage
  Scop: Validarea redirecționării către homepage prin click pe logo.

  Scenario: T06 – Verificare link către homepage din logo
    Given utilizatorul deschide pagina mens pentru testul T06
    Then pagina mens se încarcă complet în T06
    When utilizatorul identifică logo-ul site-ului
    Then logo-ul este vizibil și activ
    When utilizatorul apasă pe logo
    Then browserul este redirecționat către homepage
    Then homepage-ul se încarcă complet și conține elementele principale
    When utilizatorul navighează înapoi la mens și verifică din nou logo-ul
    Then logo-ul redirecționează corect și consistent
