from django.shortcuts import render

from django.http.response import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio',
        'description': 'This was a project where I built out my portfolio'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am still working on it'
    },

]


def projects(request):
    msg = 'asdasdasd, you are on the projects page!'
    number = 10
    context = {'message': msg, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project' : projectObj})
