from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from blog.models import BlogRecord


class BlogRecordListView(ListView):
    model = BlogRecord

    def get_queryset(self):
        return BlogRecord.objects.filter(is_published = True)

class BlogRecordCreateView(CreateView):
    model = BlogRecord
    fields = ['title', 'description', 'preview', 'is_published']
    success_url = reverse_lazy('blog:blogrecord_list')


class BlogRecordDetailView(DetailView):
    model = BlogRecord


    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views = self.object.count_views + 1
        self.object.save()

        return self.object


class BlogRecordUpdateView(UpdateView):
    model = BlogRecord
    fields = ['title', 'description', 'preview', 'is_published']

    def get_success_url(self):
        return reverse_lazy('blog:blogrecord_detail', kwargs={'pk': self.object.pk})


class BlogRecordDeleteView(DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('blog:blogrecord_list')

