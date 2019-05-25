from urllib.parse import urlparse   ##URLs
from urllib.parse import urljoin    ##PATH
from urllib.parse import parse_qs   ##QUERY STRINGS

def start():
    print ("===============================")
    print ("        Nama Sub Bab           ")
    print ("===============================")
    print ("[1] URLs")
    print ("[2] Paths and relative URLs")
    print ("[3] Query Strings")

    pilih = input("Pilih : ")

    if pilih == '1':
        menu()
    if pilih == '2':
        path()
    if pilih == '3':
        query()
def menu():
    result = urlparse('http://www.python.org/dev/peps')
    print ("===============================")
    print ("      Modul Aplikasi Url       ")
    print ("===============================")
    print ("[1] Result")
    print ("[2] Result.netloc")
    print ("[3] Result.path")
    print ("[4] urlparse('http://www.python.org:8080/')")
    print ("[0] Home")

    pilih = input("Pilih : ")

    if pilih == '1':
        print (result)
        menu()
    if pilih == '2':
        print (result.netloc)
        menu()
    if pilih == '3':
        print (result.path)
        menu()
    if pilih == '4':
        print (urlparse('http://www.python.org:8080/'))
        menu()
    if pilih == '0':
        start()

def path():
    print ("==============================")
    print ("   PATHS AND RELATIVE URLs    ")
    print ("==============================")
    print ("[1] urlparse('http://www.python.org/')")
    print ("[2] urlparse('../images/tux.png')")
    print ("[3] urljoin('http://www.debian.org', 'intro/about')")
    print ("[4] urljoin('http://www.debian.org/intro/', 'about')")
    print ("[5] urljoin('http://www.debian.org/intro', 'about')")
    print ("[6] urljoin('http://www.debian.org/intro/about', '/News')")
    print ("[7] urljoin('http://www.debian.org/intro/about/', '../News')")
    print ("[8] urljoin('http://www.debian.org/intro/about/', '../../News')")
    print ("[9] urljoin('http://www.debian.org/intro/about', '../News')")
    print ("[10] urljoin('http://www.debian.org/about', 'http://www.python.org')")
    print ("[0] Back")

    pilih = input("Pilih : ")

    if pilih == '1':
        print (urlparse('http://www.python.org/'))
        path()
    if pilih == '2':
        print (urlparse('../images/tux.png'))
        path()
    if pilih == '3':
        print (urljoin('http://www.debian.org', 'intro/about'))
        path()
    if pilih == '4':
        print (urljoin('http://www.debian.org/intro/', 'about'))
        path()
    if pilih == '5':
        print (urljoin('http://www.debian.org/intro', 'about'))
        path()
    if pilih == '6':
        print (urljoin('http://www.debian.org/intro/about', '/News'))
        path()
    if pilih == '7':
        print (urljoin('http://www.debian.org/intro/about/', '../News'))
        path()
    if pilih == '8':
        print (urljoin('http://www.debian.org/intro/about/', '../../News'))
        path()
    if pilih == '9':
        print (urljoin('http://www.debian.org/intro/about', '../News'))
        path()
    if pilih == '10':
        print (urljoin('http://www.debian.org/about', 'http://www.python.org'))
        path()
    if pilih == '0':
        start()
        
    
def query():
    print ("==============================")
    print ("         QUERY STRINGS        ")
    print ("==============================")
    print ("[1] urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')")
    print ("[2] parse_qs(result.query)")
    print ("[3] parse_qs(result.query)")

    

    pilih = input("pilih: ")


    if pilih == '1':
        print(urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default'))
        query()
    if pilih  == '2':
        result = urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')
        print(parse_qs(result.query))
        query()
    if pilih == '3':
        result = urlparse('http://docs.python.org/3/search.html?q=urlparse&q=urljoin')
        print(parse_qs(result.query))
        query()
        

                  




