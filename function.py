def book (name, pages):
    '''
    name : a string
    pages : any positive integer
    '''
    if pages <= 50:
        return(f'The book {name} is a small book of {pages} pages')
    elif pages<= 100:
        return(f'The book {name} is a medium book of {pages} pages')
    else:
        return(f'The book {name} is a big book of {pages} pages')