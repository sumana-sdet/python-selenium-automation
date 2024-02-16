Feature:Verify Target Help UI elements

  Scenario:User check for the Target Help Logo
     Given Open https://help.target.com/help
     Then  Verify Target Help page is opened
     And   Verify Target Help Logo is present

   Scenario:User check for the Search Text and search button
     Given Open https://help.target.com/help
     Then  Verify Target Help page is opened
     And   Verify Search Text field has 2 elements

   Scenario:User check for the UI element 'What would you like field'
     Given Open https://help.target.com/help
     Then  Verify Target Help page is opened
     And   Verify header 'What would you like field' displayed
     And   Verify 'What would you like field' has 7 elements

   Scenario:User check for the Target Help block elements
     Given Open https://help.target.com/help
     Then  Verify Target Help page is opened
     And   Verify Contact block has 2 elements

   Scenario:User check for the header 'Browse all Help pages'
    Given Open https://help.target.com/help
     Then  Verify Target Help page is opened
     And   Verify header 'Browse all Help pages'
