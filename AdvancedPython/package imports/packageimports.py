# from Bear.Cub import deez_nuts # Bear and Cub are parents, while deez_nuts is a function

# this import allows you to ditch the file structure
from Bear.Cub import * # you can also just import everything
deez_nuts()

# from Bear import *
# deez_nuts() #this will not work. Import wildcards only work one directory deep

# this import requires you to acknowledge the file stucture
import Bear.Cub  #you can't directly import a funtion
Bear.Cub.deez_nuts()

import Bear.Cub as animal
animal.deez_nuts()

# you go deeper using an "__init__.py" configuration (see that file)
from Fish import *
tuna_salad() #ignore the linting; this is correct

# valid if we call this file directly
if __name__ == "__main__":
	print("yes!")
