from django.contrib import admin
from tasks.forms import TaskForm
from tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'priority', 'done', 'last_date',)
    list_filter = ('category', 'priority', 'done', 'last_date',)
    list_editable = ('done',)
    search_fields = ('name',)
    exclude = ('user',)
    
    form = TaskForm
    
    def save_model(self, request, obj, form, change):
        try:
            obj.user
        except:
            obj.user = request.user

        obj.save()

    def queryset(self, request):
        """
        Returns a QuerySet of all model instances that can be edited by the
        admin site. This is used by changelist_view.
        """
        qs = self.model._default_manager.get_query_set()
        # TODO: this should be handled by some parameter to the ChangeList.
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs.filter(user = request.user)



admin.site.register(Task, TaskAdmin)