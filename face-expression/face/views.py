from django.shortcuts import render
from tensorflow.keras.models import load_model
import cv2
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from django.conf import settings


# Create your views here.


def get_img(filename):
    img=cv2.imread(filename)
    img=cv2.resize(img,(48,48))
    img=img/255.0
    return img[:,:,0].reshape(1,48,48,1)


def index(request):
    if request.method == 'GET':
        return render(request,'index.html')

    if request.method=='POST':
        try:
            temp=[]
            uploaded_file=request.FILES['document']
            fs=FileSystemStorage()
            name=fs.save(uploaded_file.name,uploaded_file)
            url=fs.url(name)
            temp.append(url)
            model=load_model('face/model_filter.h5')
            predicted=model.predict(get_img('face/media/'+name)).argmax()
            print(tf.__version__)
            label_map = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
            print(label_map[int(predicted)-1])
            emotion=label_map[int(predicted)-1]
            

            return render(request,'index.html',{'ans':emotion})
        except Exception:
            return render(request,'index.html',{'ans':"error occured"})












    # if request.method =='GET':
    #     model=load_model('face/model_filter.h5')
    #     predicted=model.predict(get_img('face/me.jpg')).argmax()
    #     print(predicted)
    #     label_map = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
    #     print(label_map[int(predicted)-1])
    #     emotion=label_map[int(predicted)-1]
    #     return render(request,"index.html",{'msg':emotion})