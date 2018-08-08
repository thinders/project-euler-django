Feature: I got 99 problems
  Scenario: Unsolved problem
    When I request solution for a problem not yet sovled
    Then The response is not found
    And The response contains 'error'

  Scenario: Heres problem 1
    When I request solution for problem 1
    Then The response contains 'solution' with value 233168
    And The response contains 'timeToSolve'
    And The response contains 'problem' with value 1