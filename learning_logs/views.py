#-*- coding: UTF-8 -*-
from django.shortcuts import render
from .models import Topic,Entry,Software,Tip
from .forms import TopicForm,EntryForm
from django.http import HttpResponseRedirect,Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
num = 0
def check_topic_owner(request,topic):
    if topic.owner != request.user:
        raise Http404
# Create your views here.
def index(request):
    """主页"""
    tips = Tip.objects.all().order_by('-date_added')
    global num
    num = num + 1
    context = {'tips':tips,'num':num}
    return render(request,'learning_logs/index.html',context)
@login_required
def topics(request):
    """所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)
@login_required
def topic(request,topic_id):
    """主题的条目"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request,topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    return render(request,'learning_logs/topic.html',context)
@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
    """在特定的主题添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request,topic)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)
@login_required
def edit_entry(request,entry_id):
    """编辑条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request,topic)
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context = {'topic':topic,'entry':entry,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)
def software(request):
    """软件资源"""
    softwares = Software.objects.all().order_by('-date_added')
    context = {'softwares':softwares}
    return render(request,'learning_logs/software.html',context)
