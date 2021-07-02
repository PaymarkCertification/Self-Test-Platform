Feature: TestCaseManagement webpage content verification

    As a user,
    I want to visit the  Self-Test platform web application page,
    So that I can verify all the functions still works post deployment

    Scenario: Login verification is working.
        Given I am on the login page.
        Then I logon with my credentials
        Then the my details have been authenticated.