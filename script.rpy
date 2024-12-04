# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    $ z = renpy.input("", "", allow="0123456789") # the same as $ z = renpy.input(prompt="", default="", allow="0123456789")
    $ z = int(z)
    "[z]"
    $ a = renpy.input("", "", allow="0123456789") # the same as $ a = renpy.input(prompt="", default="", allow="0123456789")
    $ a = int(a)
    "[a]"
    $ b = renpy.input("", "", allow="0123456789") # the same as $ b = renpy.input(prompt="", default="", allow="0123456789")
    $ b = int(b)
    "[b]"
    $ c = renpy.input("", "", allow="0123456789") # the same as $ c = renpy.input(prompt="", default="", allow="0123456789")
    $ c = int(c)
    "[c]"
    $ d = renpy.input("", "", allow="0123456789") # the same as $ d = renpy.input(prompt="", default="", allow="0123456789")
    $ d = int(d)
    "[d]"
    $ f = renpy.input("", "", allow="0123456789") # the same as $ f = renpy.input(prompt="", default="", allow="0123456789")
    $ f = int(f)
    "[f]"
    python :
      def heapify(arr, n, i):
         renpy.say(e,"[arr]")
         largest = i # Initialize largest as root
         l = 2 * i + 1 # left = 2*i + 1
         r = 2 * i + 2 # right = 2*i + 2
         if l < n and arr[i] < arr[l]:
            largest = l
         if r < n and arr[largest] < arr[r]:
            largest = r
         if largest != i:
            (arr[i], arr[largest]) = (arr[largest], arr[i]) # swap
            heapify(arr, n, largest)
            renpy.say(e,"[arr]")
      def heapSort(arr):
         n = len(arr)
         for i in range(n // 2, -1, -1):
            heapify(arr, n, i)
         for i in range(n - 1, 0, -1):
            (arr[i], arr[0]) = (arr[0], arr[i]) # swap
            heapify(arr, i, 0)
      arr = [z, a, b, c, d, f, ]
      heapSort(arr)
      renpy.say(e,"[arr]")
      n = len(arr)

    return
