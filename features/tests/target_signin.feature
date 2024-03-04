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

  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened
    When Store original window
    And Click on Target Terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window

  Scenario: Verify incorrect login test case
      Given Open target.com
      When Click Sign In
      And From right side navigation menu, click Sign In
      Then Verify Sign In form opened
      When Input email and password on SignIn page
      And Click on Sign In Button
      Then Verify that “We can't find your account.” message is shown




