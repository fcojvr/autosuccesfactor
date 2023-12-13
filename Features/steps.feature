Feature: Login

Scenario: Login to the system
    Given the user navigates to the login page
    When the user enters the username and password
    And clicks on the login button
    Then the user should be logged in

Scenario: View user profile
    Given the user is logged in
    When the user clicks on 'Ver Mi perfil'
    And enters the employee ID in the search input
    Then the user should see the employee information