Feature: Login Page

    # Scenario Outline: Scenario Outline name: A
    #     Given I am on the Fibers Digitalization Platform login page
    #     When I enter <username> on username textbox
    #     When I enter <password> on password textbox
    #     When I click Log in button
    #     Then Users are taken to Slide List page

    #     Examples:
    #         | username | password |
    #         | test     | test123  |

    Scenario: Google page
        Given I am on Google page
        When I search trang google


    Scenario Outline: Scenario Outline name: Google page2
        Given I am on Google page
        When I search <keyword> google

        Examples:
            | keyword |
            | trang   |

    Scenario: Google page3
        Given I am on Google page
        When I search google with keyword as value below
            | value |
            | trang |
