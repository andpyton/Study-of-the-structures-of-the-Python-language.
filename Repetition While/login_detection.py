# Exercise: Suspicious Login Detection (Lookahead Pattern)

# You are given a list of system events ordered by time.

# events = [
#     "LOGIN",
#     "FAILED_LOGIN",
#     "FAILED_LOGIN",
#     "LOGIN",
#     "FAILED_LOGIN",
#     "FAILED_LOGIN",
#     "FAILED_LOGIN",
#     "LOGOUT"
# ]

# Use a while loop with lookahead to detect when two consecutive failed logins happen.

# Rules
# Use a while loop (not for)
# Use current + next element
# When two "FAILED_LOGIN" events appear in sequence, print: "Warning: consecutive failed logins detected"
# Do not print duplicates for overlapping pairs
# (example: three failed logins in a row → print only once)
# Hints (important)
# You need to skip an index after detection to avoid duplicates
# Think carefully about when to increment i by 1 or 2

events = [
     "LOGIN",
     "FAILED_LOGIN",
     "FAILED_LOGIN",
     "LOGIN",
     "FAILED_LOGIN",
     "FAILED_LOGIN",
     "FAILED_LOGIN",
     "LOGOUT"
]

count_consecutive_failures = 0
i = 0

while i < (len(events)-1):

  if events[i]=="FAILED_LOGIN" and events[i+1] == "FAILED_LOGIN":
    print(f'Warning: consecutive failed logins detected at index {i}.')
    break
  i+=1


