import importlib
import time

from django.http import JsonResponse


def problem(request, num):
    try:
        module = importlib.import_module(f".solutions.problem_{num}", "problems")
    except ModuleNotFoundError:
        return JsonResponse({"error": "Problem does not exist or has not been solved"}, status=404)

    start = time.time()
    solution = getattr(module, "solve")()
    response = {"problem": num, "solution": solution, "timeToSolve": time.time() - start}
    return JsonResponse(response)