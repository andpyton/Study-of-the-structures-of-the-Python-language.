# Exercie : Website Access Counter

# Given Data

# You receive a list representing pages accessed during the day:

# pages = [
#     "home",
#     "login",
#     "home",
#     "products",
#     "home",
#     "login",
#     "checkout",
#     "login"
# ]

# Your Goal

# Create an empty dictionary called page_counter
# Loop through the list using a for loop
# For each page:
# If the page is already in the dictionary, increase its count
# If it is not, add it with count 1
# Print the final dictionary

# Data given: 

pages = [
    
     "home",
     "login",
     "home",
     "products",
     "home",
     "login",
     "checkout",
     "login",
     "checkout",
     "products",
     "products",
     "home"

]

def access_counter(pages):

  page_counter = {}

  for item in pages:

    if item in page_counter:

      page_counter[item] += 1
    
    else:

      page_counter[item] = 1
  
  return page_counter

print(f'Page counter is {access_counter(pages)}')






