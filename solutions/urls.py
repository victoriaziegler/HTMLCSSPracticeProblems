from django.urls import path
from solutions.views import show_solution, show_solution_list

urlpatterns = [
    path("", show_solution_list, name="show_solution_list"),
    path("<int:solution_number>/", show_solution, name="show_solution"),
]
