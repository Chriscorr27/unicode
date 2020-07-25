from django.shortcuts import render
from .forms import MovieForm
import requests

def detail(request,imdbId):
    form = MovieForm()
    err_msg=''
    Movies=[]
    url='http://www.omdbapi.com/?i={}&apikey=146f6525'
    imdbURL='https://m.imdb.com/title/{}/'
    r = requests.get(url.format(imdbId)).json()
    print(r)
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
    if(request.method=='POST'):
        url='http://www.omdbapi.com/?s={}&apikey=146f6525'
        movie_name = request.POST['movie']
        r=requests.get(url.format(movie_name)).json()
        
        if(r['Response']=='True'):
            err_msg=''
            search=True
            Movies=[]
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
            err_msg='Movie Not Found'
    content={'form':form,'err_msg':err_msg}
    return render(request,'MovieHome.html',content)
