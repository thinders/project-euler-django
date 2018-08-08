import importlib
import time

from django.http import JsonResponse


def problem(request, num):
    try:
        module = importlib.import_module(f".solutions.problem_{num}", "problems")
    except ModuleNotFoundError:
        error = {"error": "Problem does not exist or has not been solved"}
        return JsonResponse(error, status=404)

    problem_title = getattr(module, "problem_title")
    problem_statement = getattr(module, "problem_statement")
    start = time.time()
    solution = getattr(module, "solve")()
    response = {
        "problemTitle": problem_title,
        "problemStatement": problem_statement,
        "problemNumber": num,
        "solution": solution,
        "timeToSolve": time.time() - start,
    }
    return JsonResponse(response)
