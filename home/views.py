from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest   
from django.template import loader
from .forms import VideoForm
from .models import Video

def index(request: HttpRequest) -> HttpResponse:
    template = loader.get_template('index.html')
    videos = Video.objects.exclude(video__endswith='.pdf')
    #print(videos.video.name)
    #rint(videos.video.path)
   # print(videos.video)
   # print(videos.video)
   
    list = Video.objects.values()
    
    for i in list:
        print(i)
    context = {"videos_data":videos}
    return HttpResponse(template.render(context,request=request))

def upload_video(request:HttpRequest)-> HttpResponse:
    template = loader.get_template('index.html')
    if request.method == "POST":
        title = request.POST.get("title")
        video = request.FILES.get("video")
        if  title and video:
            print(title)
            print(video)
            if Video.objects.filter(title=title).exists():
                print("This video already exist1 skipp processing")
                return redirect("/")
            if  ".mp4" not in video:
                print("Not an Mp4 file")
            form = VideoForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
            return redirect("/")
        else:
            print("Missing Value!")
        
      

        #
          #  
          #  return redirect("")
       # else:
         #   form = VideoForm()
          #  print(form)
    
    return HttpResponse(template.render(request=request))
