"""
Page objects for the app. Use in tests like:
  from pages import HomePage, LoginPage
  home = HomePage(page, base_url="http://localhost:3000")
  home.goto()
"""
from .base import BasePage
from .exercises import ExercisesPage
from .home import HomePage
from .login import LoginPage
from .performance_tests import PerformanceTestsPage
from .training_plans import TrainingPlansPage

__all__ = [
    "BasePage",
    "HomePage",
    "LoginPage",
    "TrainingPlansPage",
    "ExercisesPage",
    "PerformanceTestsPage",
]
