import requests
from behave import *


@when("I request solution for problem {problem:d}")
def requestion_solution_for_problem(context, problem):
    context.response = requests.get(f"{context.base_url}/problem/{problem}/")
    context.test.assertEqual(
        context.response.headers["content-type"], "application/json"
    )
    context.test.assertEqual(context.response.status_code, 200)


@when("I request solution for a problem not yet sovled")
def requestion_solution_for_unknown_problem(context):
    context.response = requests.get(f"{context.base_url}/problem/{1738}/")
    context.test.assertEqual(
        context.response.headers["content-type"], "application/json"
    )


@then("The response contains '{key}'")
def verify_response_has_key(context, key):
    context.test.assertTrue(key in context.response.json(), f"Key: {key} was not found in response")


@step("The response contains '{key}' with value {value:d}")
def step_impl(context, key, value):
    response = context.response.json()
    context.test.assertTrue(key in response, f"Key: {key} was not found in response")
    context.test.assertEqual(response[key], value)


@then("The response is not found")
def step_impl(context):
    context.test.assertEqual(context.response.status_code, 404)