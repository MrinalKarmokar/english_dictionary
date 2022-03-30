from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.

def index(request):
    if request.method == "GET":
        try:
            word = request.GET['word']
            dictionary = PyDictionary()
            meaning = dictionary.meaning(word)
            list_meaning = cleaning_dict_data(meaning)
        except:
            pass
    
    try:
        context = {
            'word':word,
            'meaning': list_meaning
        }
    except:
        context = {}
    return render(request, 'index.html', context)

def cleaning_dict_data(meanings):
    lst_op = []
    for key in meanings:
        for value in meanings[key]:
            lst_op.append(value)

    return lst_op