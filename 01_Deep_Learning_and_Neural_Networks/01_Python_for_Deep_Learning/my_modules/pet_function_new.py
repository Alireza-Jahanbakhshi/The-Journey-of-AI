#p_cat and breed are Positional arguments
#owner and pet_age is Defalut arguments
#Annotation
def probe_to_cat(p_cat: float, breed: str, owner:str=None, pet_age:int=None) -> str:
    '''
    Predicte between cat and dog and print a massage
    '''
    if p_cat > 0.5:
        prediction = 'Cat'
    elif p_cat < 0.5:
        prediction = 'Dog'
    else:
        prediction = "Unknown"
    if owner is not None:    
        print(f"{owner} has a {breed} {prediction} who's {pet_age} years old!")    
    else:
        print(f"This {breed}  is {prediction} who's {pet_age} years old!")
        
    return prediction        