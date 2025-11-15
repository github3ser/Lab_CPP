Feature: Google Search basic checks

  Scenario: Pagina Google se deschide corect
    Given I open the Google homepage
    Then I should see the Google search box

  Scenario: Afișarea rezultatelor pe o singură pagină
    Given I open the Google homepage
    When I search for "Selenium WebDriver"
    Then I should see multiple search results

  Scenario: Apăsare Căutare fără input
    Given I open the Google homepage
    When I press search button without input
    Then The page should remain on Google homepage

  Scenario: Did you mean pentru un text irelevant
    Given I open the Google homepage
    When I search for "seleniun"
    Then I should see a Did You Mean suggestion
