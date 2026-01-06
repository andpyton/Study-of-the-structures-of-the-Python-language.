# Exercise: Website Traffic Analyzer.

# You are given the following dictionary:

# page_visits = {
    
#     "home": 1200,
#     "products": 850,
#     "about": 300,
#     "contact": 150,
#     "blog": 620
# }

# Tasks: 
# Use a for loop to print each page name and its number of visits
# Calculate the total number of visits across all pages.
# Find and print:
# The page with the highest number of visits
# The page with the lowest number of visits
# Print only the pages that have more than 500 visits.

page_visits = {
    
     "home": 1200,
     "products": 560,
     "about": 300,
     "contact": 150,
     "blog": 3
}

total_of_visits = 0
highest_number_of_visits=0
lowest_number_of_visits=float("inf")

for key, value in page_visits.items():
  
  total_of_visits += value
  visits = value

  if value > 500:
    print(key, value)

  if (visits > highest_number_of_visits ):
    highest_number_of_visits = visits
    index_high = key
    bigger_visits = value

  elif (visits < lowest_number_of_visits):
    index_low = key
    lowest_number_of_visits = visits
    index_low = key
    lowest_visits = value

print(f'Page with  highest number of visits is {index_high} with {bigger_visits} visits')
print(f'Page with lowest number of visits is {index_low} with {lowest_visits} visits')
