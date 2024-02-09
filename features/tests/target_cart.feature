Feature: Verify the Target Items

  Scenario: Verify the cart is empty
        Given Open target.com
        When Click on Cart icon
        Then Verify "Your cart is empty" message is shown

Scenario: Verify single item in the cart added
        Given Open target.com
        When Enter the item in the search field and click
        Then Verify search page is displayed
        When Click on Add to cart
        And  Click on side navigation add to cart button
        And  Click of View Cart and Checkout
        Then Verify the item is added to the cart
