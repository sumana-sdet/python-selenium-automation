Feature: Verify Target Circle

  Scenario: Verify benefit boxes in target circle page
    Given Open target.com
    When  Click on Target circle
    Then Verify there are 5 benefit boxes


  Scenario: User can click through Circle tabs
    Given Open Circle page
    Then Verify that clicking through Circle tabs works

  Scenario: User is able to navigate to Google Play Target page
    Given Open Circle page
    And Store original window
    When Click Google Play button
    And Switch to new window
    Then Verify Google Play Target page opened
    And Close current page
    And Return to original window