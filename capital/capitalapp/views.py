from django.shortcuts import render
from django.http import HttpResponse
import requests, json

# Create your views here. code here
def index(request):
    return render(request, "index.html")

def test(request):
    path = "https://gist.githubusercontent.com/avseksingh/3c28f23b7a47847d398f25aaa7da6515/raw/a42c02cb7c21d6be87114e587d88e25980250743/questions.json"
    url = requests.get(path)
    data = json.loads(url.text)
    print(data)

    return render(request, "test.html", {"data": data})
    # return HttpResponse(data["Python"])

def pythonquiz(request):
    questions='''
    {
  "Python": [
    {
      "questionno": 1,
      "question" : "Who developed Python Programming Language?" ,
      "a":  "Wick van Rossum",
      "b": "Rasmus Lerdorf",
      "c": "Guido van Rossum",
      "d": "Niene Stom" ,
      "correctanswer": "c" 
    },
    {
      "questionno": 2,
      "question" : "Which type of Programming does Python support?",
      "a": "object-oriented programming",
      "b": "structured programming",
      "c": "functional programming",
      "d": "all of the mentioned" ,
      "correctanswer":  "d"
    },

    {
      "questionno": 3,
      "question" : "Is Python case sensitive when dealing with identifiers?" ,
      "a": "no",
      "b":  "yes",
      "c": "machine dependent",
      "d":  "none of the mentioned",
      "correctanswer": "b" 
    },

    {
      "questionno": 4,
      "question" :  "Which of the following is the correct extension of the Python file?",
      "a": ".python",
      "b":  ".pi",
      "c": ".py",
      "d":  ".p",
      "correctanswer": "c" 
    },

    {
      "questionno": 5,
      "question" : "Is Python code compiled or interpreted?",
      "a": "Python code is both compiled and interpreted",
      "b": "Python code is neither compiled nor interpreted",
      "c": "Python code is only compiled",
      "d":  "Python code is only interpreted",
      "correctanswer":  "a"
    },

    {
      "questionno": 6,
      "question" : "Which of the following is used to define a block of code in Python language?",
      "a": "Indentation",
      "b":  "Key",
      "c": "Brackets",
      "d":  "All of the mentioned",
      "correctanswer": "a"
    },

    {
      "questionno": 7,
      "question" :  "Which keyword is used for function in Python language?",
      "a": "Function",
      "b": "Def",
      "c": "Fun",
      "d":  "Define",
      "correctanswer":"b" 
    },

    {
      "questionno": 8,
      "question" : "Which of the following character is used to give single-line comments in Python?",
      "a": "//",
      "b": "#",
      "c": "!",
      "d": "/*",
      "correctanswer": "a" 
    },

    {
      "questionno": 9,
      "question" : "Which of the following functions can help us to find the version of python that we are currently working on?",
      "a":  "sys.version(1)",
      "b":  "sys.version(0)",
      "c": "sys.version()",
      "d":  "sys.version",
      "correctanswer":  "a"
    },

    {
      "questionno": 10,
      "question" :  "Python supports the creation of anonymous functions at runtime, using a construct called __________",
      "a": "pi",
      "b": "anonymous",
      "c": "lambda",
      "d":  "non of the mentioned",

      "correctanswer": "c" 
    }
       
  ]
}

    
    '''
    return HttpResponse(questions, content_type='application/json')