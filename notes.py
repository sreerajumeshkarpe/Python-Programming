from easygui import *
import sys
while 1:
    msgbox("ONLINE SHOPPING")

    msg ="Which site would youlike to choose?"
    title="ONLINE SHOPPING"
    choices = ["Amazon", "Flipkart", "Shopclues", "Myntra"]
    choice = choicebox(msg, title, choices)

    choice=buttonbox(msg='what would you like to shop',title='',choices=("clothes","electronics","furniture"), image=None)
    if choice=="clothes":
       msgbox("CLOTHES")
       msg="Which brand ?"
       title="clothes"
       choices = ["Levis", "Flying Machine", "spykar",]
       choice = choicebox(msg, title, choices)

    elif choice=="electronics":
       msgbox("ELECTRONICS")
       msg="Which brand ?"
       title="ELECTRONICS"
       choices = ["Apple", "Samsung", "Sony",]
       choice = choicebox(msg, title, choices)

    else :
       msgbox("ELECTRONICS")
       msg="Which brand ?"
       title="ELECTRONICS"
       choices = ["Apple", "Samsung", "Sony",]
       choice = choicebox(msg, title, choices)
    sys.exit(0)
