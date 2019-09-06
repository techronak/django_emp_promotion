from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

urlpatterns = {
    path(r'employee_hire/', CreateView.as_view(), name="employee_hire"),
    # path(r'employee_hire/', CreateView.as_view(), name="employee_hire"),
    # path(r'employee_hire/', CreateView.as_view(), name="employee_hire"),

}

urlpatterns = format_suffix_patterns(urlpatterns)