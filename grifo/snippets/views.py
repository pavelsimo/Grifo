from django.shortcuts import render


def snippets_index(request):
    context = {}
    return render(request, 'snippets/index.html', context)