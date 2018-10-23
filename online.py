from easygui import *
import sys
sum=0
list=[]
while 1:
    msgbox("WELCOME !!!")
    msg ="Which site do you prefer?"
    title = "Online Shopping"
    choices = ["Amazon", "Flipkart", "Snapdeal", "Myntra"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    
    if choice=="Amazon":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice = choicebox(msg, title, choices)
          if choice=="Dell":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30000rs","vendor 2 40000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
          elif choice=="Lenovo":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30000rs","vendor 2 40000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
          else:
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30000rs","vendor 2 40000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
          if choice=="Forever 21":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 3000rs","vendor 2 4000rs","vendor 3 3000rs"]
              choice = choicebox(msg, title, choices)
          elif choice=="UCB":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 3400rs","vendor 2 4800rs","vendor 3 3500rs"]
              choice = choicebox(msg, title, choices)
          else:
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 3080rs","vendor 2 4009rs","vendor 3 3000rs"]
              choice = choicebox(msg, title, choices)
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
          if choice=="sofa":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 32000rs","vendor 2 42000rs","vendor 3 30200rs"]
              choice = choicebox(msg, title, choices)
          elif choice=="bed":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 34000rs","vendor 2 48000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
          else:
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30080rs","vendor 2 40009rs","vendor 3 30000rs"]
              choice = choicebox(msg, title, choices)

    elif choice=="Flipkart":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
          if choice=="Dell":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30000rs","vendor 2 40000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
          elif choice=="Lenovo":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30000rs","vendor 2 40000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
          else:
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30000rs","vendor 2 40000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
          if choice=="Forever 21":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 3000rs","vendor 2 4000rs","vendor 3 3000rs"]
              choice = choicebox(msg, title, choices)
          elif choice=="UCB":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 3400rs","vendor 2 4800rs","vendor 3 3500rs"]
              choice = choicebox(msg, title, choices)
          else:
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 3080rs","vendor 2 4009rs","vendor 3 3000rs"]
              choice = choicebox(msg, title, choices)
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
          if choice=="sofa":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 32000rs","vendor 2 42000rs","vendor 3 30200rs"]
              choice = choicebox(msg, title, choices)
          elif choice=="bed":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 34000rs","vendor 2 48000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
          else:
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30080rs","vendor 2 40009rs","vendor 3 30000rs"]
              choice = choicebox(msg, title, choices)

    elif choice=="Snapdeal":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
          if choice=="Dell":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30000rs","vendor 2 40000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
          elif choice=="Lenovo":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30000rs","vendor 2 40000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
          else:
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30000rs","vendor 2 40000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
      
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
          if choice=="Forever 21":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 3000rs","vendor 2 4000rs","vendor 3 3000rs"]
              choice = choicebox(msg, title, choices)
          elif choice=="UCB":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 3400rs","vendor 2 4800rs","vendor 3 3500rs"]
              choice = choicebox(msg, title, choices)
          else:
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 3080rs","vendor 2 4009rs","vendor 3 3000rs"]
              choice = choicebox(msg, title, choices)

      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
          if choice=="sofa":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 32000rs","vendor 2 42000rs","vendor 3 30200rs"]
              choice = choicebox(msg, title, choices)
          elif choice=="bed":
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 34000rs","vendor 2 48000rs","vendor 3 35000rs"]
              choice = choicebox(msg, title, choices)
          else:
              msg="Select vendor"
              title="vendors"
              choices=["vedor 1 30080rs","vendor 2 40009rs","vendor 3 30000rs"]
              choice = choicebox(msg, title, choices)
  
    elif choice=="Myntra":
      msg="What do you want to buy?"
      title="Shop items"
      choices=["Electronics","Clothing","Furniture"]
      choice = choicebox(msg, title, choices)
      if choice=="Electronics":
          msg="What do you want to buy?"
          title="Shop electronics"
          choices=["Dell","Lenovo","Apple"]
          choice=choicebox(msg, title, choices)
      elif choice=="Clothing":
          msg="What do you want to buy?"
          title="Shop clothing"
          choices=["Forever 21","UCB","Zara"]
          choice=choicebox(msg, title, choices)
      elif choice=="Furniture":
          msg="What do you want to buy?"
          title="Shop furniture"
          choices=["Sofa","bed","table"]
          choice=choicebox(msg, title, choices)
    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass 
    else:
         sys.exit(0)
