Feature: Sign in page

  Scenario: Verify that logged out user can access Sign In
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened

    Scenario: Verify login test case
      Given Open target.com
      When Click Sign In
      And From right side navigation menu, click Sign In
      Then Verify Sign In form opened
      When Input email and password on SignIn page
      And Click on Sign In Button
      Then Verify user is logged in
