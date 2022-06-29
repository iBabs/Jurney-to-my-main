from django.urls import path
from .views import MyViews, MyList, MyDetailView, MyUpdateView,MyDeleteView

urlpatterns = [
    path('',MyViews.as_view(),name='story'),
    path('list/',MyList.as_view()),
    path('detail/<pk>/', MyDetailView.as_view()),
    path('<pk>/update/', MyUpdateView.as_view()),
    path('delete/<pk>', MyDeleteView.as_view())
]
