def formate_name(f_name,l_name):
    """ Takes input from user """
    if f_name == "" or l_name == "":
        return 
    formate_f_name = f_name.title()
    formate_l_name = l_name.title()
    return f"Hello {formate_f_name} {formate_l_name}"
    
    
formate_string = formate_name("PriYanShu","NarEdi")
print(formate_string)

formate_string = formate_name("","")
print(formate_string)

print(""" 
      
      Hello
      
      """)

