Feature: Tests for product page

#  Scenario: User can select colors
#    Given Open target product A-88063497 page
#    Then Verify user can click through colors

  Scenario Outline: User can select colors
    Given Open target product <product_id> page
    Then Verify user can click through <list_of_colors>
    Examples:
    |product_id|list_of_colors|
    |A-88063497|Black,Brown,Cream,Dark Gray,Green,Light Green,Tan|
    |A-81540287|Black,Deep Olive,White|
    |A-54551690|Blue Tint,Denim Blue,Marine,Raven|


  Scenario: User verify the product name and image
    Given Open target.com
    When Enter the item in the search field and click
    Then Verify search page is displayed
    Then Verify every product on Target Search results page has product name and product image