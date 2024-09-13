# HTTP status codes program

# -------------------------
# Subprograms
# -------------------------
def http_status(status):
  if code == 400:
    return 'bad requsejf'
  elif code == 401 or code == 403:
    return 'Authentication Error'
  elif code == 404:
    return 'NOT FOUND'
  else:
    return 'NAH'  


# -------------------------
# Main program
# -------------------------

code = int(input())
print(http_status(code))

