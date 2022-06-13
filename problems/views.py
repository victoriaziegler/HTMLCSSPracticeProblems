from django.shortcuts import render
from problems.models import Person
from django.contrib.auth.models import User

from prettyprinter import cpprint, install_extras

install_extras()

# problem lists
show_information_problems = [4]
names_problems = list(range(5, 12)) + list(range(19, 23))
people_problems = list(range(23, 42))
user_problems = [12]

# /problems
def show_problem_list(request):
    """View for showing the list of problems"""
    context = {"problems": range(1, 42)}
    return render(request, "problem_list.html", context)


# /problems/<int:problem_number>
def show_problem(request, problem_number):
    """View for displaying a specific problem"""
    print(f"Trying to load problem {problem_number}")
    template_name = f"problem_{str(problem_number).zfill(3)}.html"

    context = {}

    # Context for Problem 4
    if problem_number in show_information_problems:
        context["show_information"] = False

    # Context for Problems 5 through 11 and 19 through 22
    if problem_number in names_problems:
        context["names"] = [
            "Kim",
            "Paz",
            "Talia",
            "Anima",
        ]

    # Context for Problems 23 through 41
    if problem_number in people_problems:
        context["people"] = Person.objects.all()

    # This prints out the context in a pretty way.
    print("=" * 10, "Context", "=" * 10)
    cpprint(context)

    return render(request, f"problems/{template_name}", context)
