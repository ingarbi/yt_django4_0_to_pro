from django.urls import path
from myapp.views import index, indexItem, add_item, update_item

app_name = "myapp"

urlpatterns = [
    # http://127.0.0.1:8000/myapp/
    path("", index, ),
    path("<int:my_id>/", indexItem, name="detail"),
    # http://127.0.0.1:8000/myapp/
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item"),
]
