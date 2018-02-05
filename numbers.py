import sys

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    name = 'World'
  print 'Hello', name

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

def biggest_number(*args):
  print max(args)
  return max(args)
    
def smallest_number(*args):
  print min(args)
  return min(args)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)

  from datetime import datetime
  now = datetime.now()

  print '%s/%s/%s' % (now.year, now.month, now.day)

  print '%s:%s:%s' % (now.hour, now.minute, now.second)


