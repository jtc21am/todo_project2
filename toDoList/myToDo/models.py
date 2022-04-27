from django.db import models
import datetime


class Tags(models.Model):
    """Tags defining a ToDoItem"""
    tags = models.CharField(max_length=50, help_text="Tag for Task", default=True)
    def __str__(self) -> str:
        return self.tags


class ToDoItem(models.Model):
    """Item on To-Do list"""
    list_item = models.CharField(max_length=150, help_text="Add Task to list", default=True)
    complete = models.BooleanField(help_text="Is Task completed or not", default = False)
    tags = models.ManyToManyField(Tags, through='TodoTags')
    def __str__(self) -> str:
        return self.list_item


class TodoTags(models.Model):
    """ToDoItems Tags"""
    todoitem = models.ForeignKey(ToDoItem, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE)


class Note(models.Model):
    """Note on an item"""
    note = models.TextField(help_text="Note regarding selected task")
    task = models.ForeignKey(ToDoItem, on_delete=models.CASCADE,help_text="Attach a note for this task")
    date_created = models.DateTimeField(default=datetime.datetime.now, help_text="Date & Time Stamp")

    def __str__(self) -> str:
        return self.note