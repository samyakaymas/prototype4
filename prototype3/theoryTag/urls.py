from django.urls import path 
from . import views

urlpatterns=[
    path("add/",views.TheoryCreateView.as_view(),name="add"),
    path("ajax/load/subConcepts",views.loadSubConcepts,name="ajaxLoadSubConcepts"),
    # path("",views.index,name="index"),

    path("ajax/load/concepts",views.loadConcepts,name="ajaxLoadConcepts"),

    path('show/<int:pk>', views.TheoryDetailView.as_view(), name='theory-details'),
    path('update/<int:pk>',views.TheoryUpdateView.as_view(), name='theory-update'),
    path('', views.TheoryListView.as_view(), name='theorys'),
    path('subConceptName/',views.loadSubConceptName,name='subConcept-Name'),
]