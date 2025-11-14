@T04
Feature: Verificare buton „Add to Cart”
  Scop: Verificarea funcționalității butonului „Add to Cart” pentru primul produs

  Scenario: T04 – Adăugare produs în coș
    Given utilizatorul deschide pagina "https://adoring-pasteur-3ae17d.netlify.app/mens.html"
    Then pagina se încarcă complet fără erori
    And primul produs este vizibil
    When utilizatorul derulează până la primul produs
    And utilizatorul dă click pe butonul "Add to Cart"
    Then mesajul de confirmare apare sau icon-ul coșului se actualizează
    When utilizatorul accesează coșul ("Cart")
    Then produsul adăugat este vizibil cu nume, preț și imagine
    And totalul prețurilor din coș este corect
    When utilizatorul dă click de 2 ori pe același buton "Add to Cart"
    Then cantitatea produsului se actualizează corect sau apare mesaj "Already in cart"
