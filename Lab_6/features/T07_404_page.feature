@T07
Feature: Verificare afișare pagină 404 pentru URL invalid
  Scop: Validarea comportamentului site-ului atunci când este accesat un URL inexistent.

  Scenario: T07 – Verificare afișare pagină 404 la URL invalid
    Given browserul Chrome este deschis pentru testul T07
    When utilizatorul introduce un URL invalid
    Then pagina afișează eroare 404 sau mesaj Page not found
    Then mesajul 404 sau Page not found este vizibil în pagină
    When utilizatorul caută opțiunea de întoarcere la homepage
    Then site-ul oferă un link sau buton pentru revenirea la homepage
    When utilizatorul apasă pe linkul de revenire
    Then utilizatorul este redirecționat spre homepage fără erori
