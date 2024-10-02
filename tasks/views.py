from django import forms
from django.shortcuts import render

tasks= ["eat", "sleep", "repeat"]
# Create your views here.
class NewTaskForm(forms.Form):
    task= forms.CharField(label="New task")
def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request,"tasks/add.html", {
        "form": NewTaskForm()
    })