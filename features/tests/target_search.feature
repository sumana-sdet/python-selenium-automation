Feature: Test Scenarios for Target Search functionality

  Scenario Outline: User can search for a product
    Given Open target.com
    When Enter <search_word> into search field
    And  Click on the search icon
    Then Search results for <search_result> are shown
    And  Search result page URL has search term <expected_partial_url>
    Examples:
    |search_word|search_result|expected_partial_url|
    |coffee     |coffee       |coffee              |
    |coffee mug |coffee mug   |coffee+mug          |

