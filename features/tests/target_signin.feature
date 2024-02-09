Feature: Sign in page

  Scenario: Verify that logged out user can access Sign In
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened
