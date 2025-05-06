r={}
l=[]
def add(menu,items):
    print(f"\n{menu.capitalize()}:menu")
    for a,b in items.items():
        print(a,b)
    try:
        c=int(input("how many items you want to add:"))
    except ValueError:
        print("plz enter the valid number")
    while c!=0:
        item=input("select food you want to eat:")
        if item in items.keys():
            if item not in l:
                l.append(item)
                no=input("quantity:")
                prize=items.get(item)
                item=item.capitalize()+"*"+no
                r[item]=int(prize)*int(no)
                c=c-1
            else:
                print("food is already added, try something else")
        else:
            print("food not in our menu")
    
        
def main():
    menus={"snacks":{"tea":200,"coffee":500,"cookies":450},
           "lunch":{"roti":200,"dal":500,"rice":450},
           "dinner":{"panner":200,"pizza":500,"noodles":450}}
    print("\t\tWELCOME TO XYZ RESTAURENT")
    while True:
       try:
          c=int(input("\n1.menu\n2.bill\n3.exit\nselect one these:"))
       except ValueError:
           print("wrong choice")
       if c==1:
           menu=input("snacks\nlunch\ndinner\nwhat you want:").lower()
           if menu in menus:
               add(menu,menus[menu])
           else:
               print("\ninvalid choice")
       elif c==2:
           print("your bill is :\n")
           i=1
           cost=sum(r.values())
           for a,b in r.items():
              print(f"{i}.{a}->{b}")
              i=i+1
           print("total=",cost)
       elif c==3:
           print("thank you")
           break
       else:
           print("wrong choice")

if __name__=="__main__":
    main()
    
        

    
