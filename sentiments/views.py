from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
import os
from joblib import load
BASE_DIR = Path(__file__).resolve().parent.parent
loaded_svm=load(os.path.join(BASE_DIR,'ml-sent-svm.joblib'))
def home(request):
    return render(request,'home.html',{'name':'India'})


def senti(request):
    v=[str(request.POST['string1'])]
    pre=str(loaded_svm.predict(v))
    return render(request,"result.html",{'result':pre})
