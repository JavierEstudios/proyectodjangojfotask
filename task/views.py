from django.shortcuts import render, get_object_or_404
from django.views import View
from task.models import Task

# Create your views here.

class TaskListView (View):

    def get(self,request):
        tasks=Task.objects.all()
        return render(request,'task/task_list.html',{'tasks':tasks})
    
class TaskDetailView (View):

    def get(self,request,pk):
        task=  get_object_or_404(Task, pk=pk)
        return render(request,'task/task_detail.html',{'task':task})