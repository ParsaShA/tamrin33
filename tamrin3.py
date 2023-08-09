lst = [1,1,2,2,2,3,3,'a']
def do_bar(lst):
    i = 1
    elm = lst[i]
    while i < len(lst):
        if elm in lst:
            if lst.count(elm)==2:
                return elm
        i+=1
        
        
        
        
        
print((do_bar(lst)))
