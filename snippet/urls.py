from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import snippet_list, snippet_detail

urlpatterns = [
    path('', snippet_list),
    path('<int:pk>', snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)