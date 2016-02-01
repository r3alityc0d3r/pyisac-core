Feature: Command Statup
    In order to get program execution status
    As a pyisac user
    I want to see output returned from the command

    Scenario: startup with no arguments
        Given the user runs pyisac from the command line
        When no arguments are given
        Then a banner should be shown

    Scenario: startup with no arguments
        Given the user runs pyisac from the command line
        When no arguments are given
        Then the GPL license should be shown
