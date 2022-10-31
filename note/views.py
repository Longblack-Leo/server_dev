from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.views import View
from pydantic import Json

from .models import Notes
# Create your views here.

def index(request):
    note_list = Notes.objects.order_by('-created_at')
    context = {'note_list': note_list}
    return render(request, 'note/note_list.html', context)

def detail(request, note_id):
    note = Notes.objects.get(id=note_id)
    context = {'note': note}
    return render(request, 'note/note_detail.html', context)