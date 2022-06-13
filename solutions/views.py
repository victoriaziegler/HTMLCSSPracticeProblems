from django.shortcuts import render
from problems.models import Person

from prettyprinter import cpprint, install_extras

install_extras()

# solution lists
show_information_solutions = [4]
names_solutions = list(range(5, 12)) + list(range(19, 23))
people_solutions = list(range(23, 42))
user_solutions = [12]

# /solutions
def show_solution_list(request):
    """View for showing the list of solutions"""
    context = {"solutions": range(1, 42)}
    return render(request, "solution_list.html", context)


# /solutions/<int:solution_number>
def show_solution(request, solution_number):
    """View for displaying a specific solution"""
    print(f"Trying to load solution {solution_number}")
    template_name = f"solution_{str(solution_number).zfill(3)}.html"

    context = {}

    # Context for solution 4
    if solution_number in show_information_solutions:
        context["show_information"] = True

    # Context for solutions 5 through 11 and 19 through 22
    if solution_number in names_solutions:
        context["names"] = [
            "Kim",
            "Paz",
            "Talia",
            "Anima",
        ]

    # Context for solutions 23 through 41
    if solution_number in people_solutions:
        context["people"] = Person.objects.all()

    # This prints out the context in a pretty way.
    print("=" * 10, "Context", "=" * 10)
    cpprint(context)

    return render(request, f"solutions/{template_name}", context)
