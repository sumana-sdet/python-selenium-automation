Feature: Test for Main Page UI

  Scenario: User can see signin arrow
    Given Open target.com
    When Hover over signin
    Then Verify signin arrow shown