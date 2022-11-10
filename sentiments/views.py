from django.http import HttpResponse
from django.shortcuts import render
import os
from joblib import load
loaded_svm=load(os.path.join("../catsreadminds\ml-sent-svm.joblib"))
def home(request):
    return render(request,'home.html',{'name':'India'})


def senti(request):
    v=[str(request.POST['string1'])]
    pre=str(loaded_svm.predict(v))
    return render(request,"result.html",{'result':pre})
