Feature: Verify Target Circle

  Scenario: Verify benefit boxes in target circle page
    Given Open target.com
    When  Click on Target circle
    Then Verify there are 5 benefit boxes


  Scenario: User can click through Circle tabs
    Given Open Circle page
    Then Verify that clicking through Circle tabs works