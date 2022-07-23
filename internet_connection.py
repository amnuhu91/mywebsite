import urllib.request
#from myblog.settings import BASE_DIR

def check_internet(host="https://www.google.com"):
    DATABASE ={}
    try:
        urllib.request.urlopen(host)
        
        # DATABASE= {
        #     'ENGINE': 'django.db.backends.postgresql',
        
        
        # 'NAME':'ddtekq1s61dsid',
        # 'USER':'lrnvrotvqdhdol',
        # 'PASSWORD':'3559911b6b0f980dc17b2381a5156416a043ac3e17b0caed8827ce504b958938',
        # 'HOST':'ec2-34-225-159-178.compute-1.amazonaws.com',
        # 'PORT':5432
        # }
        print("there is internet the database is set to heroku postgress")
        return True
    except:
        # DATABASE ={
        #      'ENGINE': 'django.db.backends.sqlite3',
        
        # 'NAME': BASE_DIR / 'db.sqlite3',
        # }
        print("no internet the adabase is set to default sqlite")
        return False

    


#check_internet()
