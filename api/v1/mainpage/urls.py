from django.urls import path
from .views import ApartmentListCreateView, ApartmentDetailView, ProjectsListCreateView, ProjectsDetailView

urlpatterns = [
    path(
        'apartments/', 
        ApartmentListCreateView.as_view(),
        name='apartment-list-create'
        ),
    path(
        'apartments/<uuid:pk>/', 
        ApartmentDetailView.as_view(),
        name='apartment-detail'
        ),
    path(
        'projects/',
        ProjectsListCreateView.as_view(),
        name='projects-list-create'
        ),
    path(
        'projects/<uuid:pk>/',
        ProjectsDetailView.as_view(),
        name='projects-detail'
        ),
]