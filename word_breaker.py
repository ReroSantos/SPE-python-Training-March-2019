def breaker(statement):
    container = []
    holder=''
    
    for i in statement:
        if i != ' ':
            holder += i
        else:
            container.append(holder)
            holder = ''
            
    container.append(holder)
    
    return container
        
                