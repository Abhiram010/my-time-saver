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
    
if (open=="mail"): 
    a=input("(x)virtual mode or (y) default mail page:")
    if a=="y":
     a = "https://mail.google.com/mail/u/0//"
     webbrowser.open_new(a)
    if a=="x":
      a="https://mail.google.com/mail/u/0/"
      
      w=input("Do you want preffered content?(primary)(starred)(chats)(all)(drafts)(bin)(sent)(settings) : ")
      if w=="no":
        webbrowser.open_new(a+v)
      if w=="yes":
          w1=input("open only: ")
    if w1=="primary":
        w1=" #primary"
    
    if w1=="starred":
          a="https://mail.google.com/mail/u/0/"
          w1=" &starred"
    if w1=="chats":
        a="https://mail.google.com/mail/u/0/"
        
        w1="#chats"
    if w1=="all":
        a="https://mail.google.com/mail/u/0/"
        w1="#all"
    if w1=="drafts":
          a="https://mail.google.com/mail/u/0/"
          w1="#drafts"
    if w1=="bin":
          a="https://mail.google.com/mail/u/0/"
          w1="#trash"


    if w1=="sent":
         a="https://mail.google.com/mail/u/0/"
         w1=" #sent"
    if w1=="settings":
         a="https://mail.google.com/mail/u/0/"
         w1=" #settings/labels"   
    webbrowser.open_new(a+w1)
    

