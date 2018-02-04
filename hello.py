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

  def secondFunction():
    eggs = 12
    return eggs
          
  print secondFunction()

  """say what!?
  another line thats cool
  wow"""

  from datetime import datetime
  now = datetime.now()

  print '%s/%s/%s' % (now.year, now.month, now.day)

  print '%s:%s:%s' % (now.hour, now.minute, now.second)

  def usingIf():
      if 5>1 or 4>1:    # Start coding here!
          print "this"
          return True
      elif 1 != 1:
          print "that"
          return False
      else: 
          print "the other"
      return True

  usingIf()

