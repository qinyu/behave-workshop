Feature: Wordpress Lover

  As a blog writer
  I want to manage my wordpress
  So that I can improve my influence

  Background: Open login page
    Given I open wordpress
    When I click "login"
    Then I can see login page


  Scenario: allow login with valid credential
    Given I open wordpress
    When I click "login"
    Then I can see login page
    When I login with credential "admin" and "123456"
    Then I can login successful

  @wip
  Scenario Outline: allow login with invalid credential
    When I login with credential "<user>" and "<password>"
    Then I should see error message "<error>"
    Examples:
      | user  | password | error                                                                                    |
      | admin | 111111   | ERROR: The password you entered for the username admin is incorrect. Lost your password? |
      | qinyu | 123456   | ERROR: Invalid username. Lost your password?                                             |
      | admin | N/A      | ERROR: The password field is empty.                                                      |

