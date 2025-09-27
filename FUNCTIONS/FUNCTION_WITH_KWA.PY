# CRAETE A FUNCTION THAT ACCESPTS ANY NUMBER OF KEYWORD ARGUMENTS AND PRINT THEM IN THE FORMAT
def print_kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}:{value}")
    
print_kwargs(university="far-western",name="Bikash",faculty="computer")
print_kwargs(country="Nepal",continent="asia ")