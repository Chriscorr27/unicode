from django.shortcuts import render
from .forms import MovieForm
from .models import movie_search
from django.http import HttpResponse
import requests


    


def detail(request,imdbId):
    form = MovieForm()
    err_msg=''
    Movies=[]
    url='http://www.omdbapi.com/?i={}&apikey=146f6525'
    imdbURL='https://m.imdb.com/title/{}/'
    r = requests.get(url.format(imdbId)).json()
    #print(r)
    try:
        r['BoxOffice']
    except:
        r['BoxOffice']='N/A'
    if(r['Response']=='True'):

        movie={
            'Title': r['Title'],
            'Poster': r['Poster'],
            'BoxOffice' :r['BoxOffice'],
            'Released' :r['Released'],
            'Runtime' :r['Runtime'],
            'imdbRating' :r['imdbRating'],
            'Genre' :r['Genre'],
            'Director' :r['Director'],
            'Link':imdbURL.format(imdbId)
            
        }
        Movies.append(movie)
    else:
        err_msg='Wrong imdbId'

    content={'form':form,'err_msg':err_msg,'movies':Movies}
    return render(request,'MovieDetail.html',content)


def search(request):
    err_msg = ''
    search=False
    form = MovieForm()
    Movies=[]
    
    if(request.method=='POST'):
        url='http://www.omdbapi.com/?s={}&apikey=146f6525'
        movie_name = request.POST['movie']
        r=requests.get(url.format(movie_name)).json()
        
        if(r['Response']=='True'):
            
            movie_obj = movie_search.objects.get_or_create(search=movie_name)
            #print(movie_obj[0],movie_obj[1])
            
            movie_obj[0].count+=1
            movie_obj[0].save()
            
            search=True
            
            for movie in r['Search'] :
                #print(movie)
                
                movie_detail={
                   'Title': movie['Title'],
                   'Year' : movie['Year'],
                   'Poster': movie['Poster'],
                   'Type': movie['Type'],
                   'imdbID': movie['imdbID']
                }
                Movies.append(movie_detail)
                

            content={'form':form,'movies':Movies,'search':search}
            return render(request,'MovieHome.html',content)

        else:
            err_msg=movie_name+' Not Found'
    
    movies = movie_search.objects.order_by('-count')
    #movies = movie_search.objects.all()
    movie_count =  movie_search.objects.all().count()
    print(movie_count)
  
    if(movie_count>3):
        movie_count=3
    for i in range(movie_count):
        movie_obj=movies[i]
        movie_detail={
            'search':movie_obj.search,
            'count':movie_obj.count
        }
        Movies.append(movie_detail)
   
    content={'form':form,'err_msg':err_msg,'movies':Movies}
    return render(request,'MovieHome.html',content)


def Movie_search(request,search_movie):
    form = MovieForm()
    search = False
    Movies = []  
    err_msg='' 
    if movie_search.objects.filter(search=search_movie).exists():
    
        movie_obj = movie_search.objects.get(search=search_movie)
        movie_obj.count+=1
        movie_obj.save()
        search = True
        url='http://www.omdbapi.com/?s={}&apikey=146f6525'
        r=requests.get(url.format(search_movie)).json()
        
       
        if(r['Response']=='True'):
            for movie in r['Search'] :
                    #print(movie)
                    
                    movie_detail={
                    'Title': movie['Title'],
                    'Year' : movie['Year'],
                    'Poster': movie['Poster'],
                    'Type': movie['Type'],
                    'imdbID': movie['imdbID']
                    }
                    Movies.append(movie_detail)
        
    
    else:
        err_msg='movie doesnot exist in database'
            
    content={'form':form,'movies':Movies,'search':search,'err_msg':err_msg}
    return render(request,'MovieHome.html',content)