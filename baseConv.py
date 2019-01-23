# Change conversionAlphabet to contain the conversion alphabet for the base you 
# are converting to, starting at the equivalent 0
# The following algorithm was adapted from here: http://interactivepython.org/courselib/static/pythonds/Recursion/pythondsConvertinganIntegertoaStringinAnyBase.html

def changeBase(n, base):
   conversionAlphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   if n < base:
      return conversionAlphabet[n]
   else:
      return toStr(n // base, base) + conversionAlphabet[n % base]

# To use: print(changeBase(number to convert, base to convert to))
