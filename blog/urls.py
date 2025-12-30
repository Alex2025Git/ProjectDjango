from blog.views import BlogRecordListView, BlogRecordCreateView, BlogRecordDetailView, BlogRecordUpdateView, \
    BlogRecordDeleteView

from blog.apps import BlogConfig

from django.urls import path

app_name = BlogConfig.name

urlpatterns = [
    path("", BlogRecordListView.as_view(), name="blogrecord_list"),
    path("create/", BlogRecordCreateView.as_view(), name="blogrecord_create"),
    path("detail/<int:pk>/", BlogRecordDetailView.as_view(), name="blogrecord_detail"),
    path("update/<int:pk>/", BlogRecordUpdateView.as_view(), name="blogrecord_update"),
    path("delete/<int:pk>/", BlogRecordDeleteView.as_view(), name="blogrecord_delete"),

    ]
