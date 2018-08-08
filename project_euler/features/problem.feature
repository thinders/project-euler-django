Feature: I got 99 problems
  Scenario: Heres problem 1
    When I request solution for problem 1
    Then The result contains 'answer'
    And The result contains 'timeToSolve'