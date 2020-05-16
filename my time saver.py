import webbrowser
print("(youtube- yt) (Gmail-mail)")

open=input("enter what you want= ")

if (open=="yt"):
    print("")
    a=input(" use [x,y](x)-search directly in youtube here anf filter or (y)-default home page:")
    if a=="home":
     a = "https://www.youtube.com/"
     webbrowser.open_new(a)
    if a=="x":
      a="https://www.youtube.com/results?search_query="
      v=input("search for:")
      w=input(" Do you want to filter ? yes/no: ")
      if w=="no":
        webbrowser.open_new(a+v)
      if w=="yes":
          w1=input("filter for: ")
    if w1=="hour":
        w1="&sp=EgQIARAB"
    
    if w1=="month":
        w1=" &sp=EgIIAQ%253D%253D"
    
    if w1=="year":
        w1=" &sp=EgQIBRAB"
    
    if w1=="week":
        w1=" &sp=EgQIAxAB"

    if w1=="today":
        w1=" &sp=EgQIAxAB"
    webbrowser.open_new(a+v+w1)
    

    

