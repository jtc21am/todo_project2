from django.shortcuts import render
from django.views import View
from .models import ToDoItem, Note, Tags

def handler404(request, exception=None):
    return render(request, '404.html')

def displayTask(self, request):
    self.all_todo_items = ToDoItem.objects.all()
    incompleted = [task for task in self.all_todo_items if not task.complete]
    completed = [task for task in self.all_todo_items if task.complete]

    return render(request=request,template_name='list.html', context={"incompleted": incompleted,"completed": completed,})

class Index(View):
    '''My main landing page'''
   
    def get(self, request):
        return displayTask(self, request)
   
    def post(self, request):
        '''User is adding their task here as well as the tagging, the tag value then passed'''
        print(request.POST)
        todo_item = request.POST['content']
   
        tags = {}
        if 'Urgent' in request.POST: tags['urgent'] = True
        if 'Personal' in request.POST: tags['personal'] = True
        if 'Work' in request.POST: tags['work'] = True
        if 'Other' in request.POST: tags['other'] = True
        if 'None' in request.POST: tags['none'] = True

        new_item = ToDoItem.objects.create(list_item = todo_item)
        
        for tag in tags.keys():
            if tag == 'urgent': new_item.tags.add(1)
            if tag == 'personal': new_item.tags.add(2)
            if tag == 'work': new_item.tags.add(3)
            if tag == 'other': new_item.tags.add(4)
            if tag == "None": new_item.tags.add(5) 
        new_item.save()
        return displayTask(self, request)


class Task(View):
    '''Task page'''
    def get(self, request, id):
        try:
            # RECALLING THE TASKS
            task = ToDoItem.objects.get(id=id)
            notes = ''
            # NOTES
            notes = Note.objects.filter(task_id = id)
            # SORTING THE TASKS IN ASCENTING ORDER
            notes = sorted(notes, key=lambda note: note.date_created, reverse=True)
        except:
            return render(request=request,template_name='404.html')
        return render(request=request, template_name='details.html', context={"task": task, "notes": notes})

    def post(self, request, id):
        task = ToDoItem.objects.get(id=id)
        # UPDATE TASK
        if 'update' in request.POST:
            update_item = request.POST['content']
            task = ToDoItem( id = id, list_item = update_item)
        # DELETE TASK
        if 'delete' in request.POST:
            task.delete()
            return displayTask(self, request)
        # MARKING THE TASK AS COMPLETE
        if 'complete' in request.POST:
            task = ToDoItem(id = id , list_item = task.list_item, complete = True)
        # MARKING THE TASK AS INCOMPLETE
        if 'incomplete' in request.POST:
            task = ToDoItem(id = id , list_item = task.list_item, complete = False)
        # ADDING NOTES
        if 'note' in request.POST:
            note_text = request.POST.getlist('note')[0]
            task = ToDoItem.objects.get(id= id)
            note = Note(task = task, note = note_text)
            note.save()

        task.save()
        return displayTask(self, request)

