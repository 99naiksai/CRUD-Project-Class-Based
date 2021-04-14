from django.urls import path
from enroll import views
urlpatterns = [

    path('delete/<int:id>/' , views.UserDeleteView.as_view() , name = "deletedata"),
    path('<int:id>/' , views.UserUpdateView.as_view() , name = "updatedata"),
    path('' , views.UserAddShowView.as_view() , name = "addandshow")
]
