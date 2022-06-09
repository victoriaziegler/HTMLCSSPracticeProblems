from django.urls import path
from problems.views import show_problem,show_problem_list

urlpatterns = [
    path("", show_problem_list, name="show_problem_list"),
    path("<int:problem_number>/", show_problem, name="show_problem")
]