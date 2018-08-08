import requests
from behave import *


@when("I request solution for problem {problem:d}")
def step_impl(context, problem):
    context.response = requests.get(f"{context.base_url}/problem/{problem}/")
    context.test.assertEqual(
        context.response.headers["content-type"], "application/json"
    )
    context.test.assertEqual(context.response.status_code, 200)


@then("The result contains '{key}'")
def step_impl(context, key):
    context.test.assertEqual(key in context.response.json(), True)