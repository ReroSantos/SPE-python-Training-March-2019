def square_of_sum(count):
    if count < 2:
        return count
    else:
        holder = 0
        for i in range (count+1):
            holder += i
        
        return holder**2



def sum_of_squares(count):
    holder = 0
    if count < 2:
        return count
    else:
        for i in range (count+1):
            holder += i**2
    
    return holder



    


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
