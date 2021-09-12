import sys #Importando uma blibioteca pronta em python

'''
Operators in python:
    + addition
    - subtraction
    * multiplication
    / division
    ** exponentiation
    % modulo
    // interger division

Variables in python:
    Mutiple assignment in line:
        x, y, z = 1, 2, 3

Variables self operations
    x += 2 (x = x + 2)
    x -= 2 (x = x - 2)
    x *= 2 (x = x * 2)
    .
    .
    .

Types int, float
    x = int(4.7)   # x is now an integer 4
    y = float(4)   # y is now a float of 4.0

Good practices:
    print(3 + 4)
    print(3*7 -4)
    You should limit each line of code to 80 characters,
        though 99 is okay for certain use cases.

Comparisson:
    < less than
    > greater than
    <= less than or equal to
    >= greater than or equal to
    == equal to
    != not equal to

Logical operators:
    and evaluates if both sides are true
    or evaluates if at least one side is true
    not inverses a boolean type

Strings:
    my_string = 'this is a string!'
    my_string2 = "this is also a string!!!"
    this_string = 'Simon\'s skateboard is in the garage.'
    first_word = 'Hello'

Operations with strings:
    print(first_word * 5) (Will print: 'HelloHelloHelloHelloHello')

String Methods:
    A method in Python behaves similarly to a function. Methods actually are functions
    that are called using dot notation. For example, lower() is a string method
    that can be used like this, on a string called "sample string": sample_string.lower().

    my_string.islower()
    True
    my_string.count('a')
    2
    my_string.find('a')
    3

    print("Mohammed has {} balloons".format(27))
    animal = "dog"
    action = "bite"
    print("Does your {} {}?".format(animal, action))

    maria_string = "Maria loves {} and {}"
    print(maria_string.format("math", "statistics"))

    new_str = "The cow jumped over the moon."
    new_str.split()
    ['The', 'cow', 'jumped', 'over', 'the', 'moon.']
    new_str.split(' ', 3)
    Here the separator is space, and the maxsplit argument is set to 3.
    ['The', 'cow', 'jumped', 'over the moon.']

Lists:
    Data structures are containers that organize and group data types together in
     different ways.
    A list is one of the most common and basic data structures in Python.

    You saw here that you can create a list with square brackets.
    Lists can contain any mix and match of the data types you have seen so far.

    list = ['a', 'b', 'c']
    list[0] == 'a'
    list[-1] == 'c' in pyhon you can acess the last index of a list by using -1
    list[1] == list[-2] == 'b' using negatives numbers ypu can acess the list
        in decresing order

Slice and dice with lists:
    You saw that we can pull more than one value from a list at a time by using slicing.
    When using slicing, it is important to remember that the lower index is inclusive
     and the upper index is exclusive.

    list_of_random_things = [1, 3.4, 'a string', True]
    list_of_random_things[1:2]
    -> [3.4]
    will only return 3.4 in a list. Notice this is still different than just indexing
     a single element, because you get a list back with this indexing. The colon tells
     us to go from the starting value on the left of the colon up to, but not including,
     the element on the right.

     list_of_random_things[:2]
      ->[1, 3.4]
     If you know that you want to start at the beginning,
      of the list you can also leave out this value.

     list_of_random_things[1:]
     ->[3.4, 'a string', True]
     or to return all of the elements to the end of the list, we can
      leave off a final element.

     This type of indexing works exactly the same on strings, where the returned
      value will be a string.

Are you in OR not in?
    You saw that we can also use in and not in to return a bool of whether an
     element exists within our list, or if one string is a substring of another.

    'this' in 'this is a string'
     ->True
    'in' in 'this is a string'
     ->True
     'isa' in 'this is a string'
     ->False
     5 not in [1, 2, 3, 4, 6]
     ->True
     5 in [1, 2, 3, 4, 6]
     ->False

Lists != Strings, because of mutability:
    lists are mutable
    strings are immutable
    But lists and strings are both ordered

    Mutability is about whether or not we can change an object once it has been created.
     If an object (like a list or string) can be changed (like a list can), then it
     is called mutable. However, if an object cannot be changed with creating a
     completely new object (like strings), then the object is considered immutable.

    Order is about whether the position of an element in the object can be used to
     access the element. Both strings and lists are ordered. We can use the order
     to access parts of a list and string.

Useful Functions for Lists I:
    len() returns how many elements are in a list.
    max() returns the greatest element of the list. How the greatest element is determined
     depends on what type objects are in the list. The maximum element in a list of numbers
     is the largest number. The maximum elements in a list of strings is element that
     would occur last if the list were sorted alphabetically. This works because the the
     max function is defined in terms of the greater than comparison operator.
     The max function is undefined for lists that contain elements from different,
     incomparable types.
    min() returns the smallest element in a list. min is the opposite of max, which returns
     the largest element in a list.
    sorted() returns a copy of a list in order from smallest to largest, leaving the list
     unchanged.
     join method
    join() is a string method that takes a list of strings as an argument,
     and returns a string consisting of the list elements joined by a separator string.
        new_str = "\n".join(["fore", "aft", "starboard", "port"])
            In this example we use the string "\n" as the separator so that there is
             a newline between each element. We can also use other strings as
             separators with .join.
        print(new_str)
        >>>fore
        >>>aft
        >>>starboard
        >>>port
    append() A helpful method called append adds an element to the end of a list.

Tuple: A data type for immutable ordered sequences of elements, a tple can be indexed
    and sliced like a list.
Set: A data type for mutable unordered colections of unique elements.
    pop() can be used in sets but as sets don't have an order it will
     be a random element
    add() also cna be used is sets
Dictionary: A data type for mutable objects that store mappings
 of unique keys to values
 A dictionary is a mutable, unordered data structure that contains mappings of keys to
  values. Because these keys are used to index values, they must be unique and immutable.
  For example, a string or tuple can be used as the key of a dictionary, but if you try to
  use a list as a key of a dictionary, you will get an error.
 population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.3, 'Mumbai': 12.5}

get() with a Default Value
    Dictionaries have a related method that's also useful, get(). get() looks up values in
     a dictionary, but unlike looking up values with square brackets, get() returns
     None (or a default value of your choice) if the key isn't found. If you expect
     lookups to sometimes fail, get() might be a better tool than normal square bracket
     lookups.

    >>> elements.get('dilithium')
    None
    >>> elements['dilithium']
    KeyError: 'dilithium'
    >>> elements.get('kryptonite', 'There\'s no such element!')
    "There's no such element!"
        In the last example we specified a default value (the string 'There's no such
        element!') to be returned instead of None when the key is not found.

When to use Dictionaries?
    As you can see, data structures are very useful in collecting,
     storing and working with more information than simple strings
     or integers.

Control flow:
    - conditional statements
    - for and while lookps
    - break and continue
    - useful built-in functions
    - list comprehensions

Iterating Through Dictionaries with For Loops
    When you iterate through a dictionary using a for loop, doing it the normal way
     (for n in some_dict) will only give you access to the keys in the dictionary -
     which is what you'd want in some situations. In other cases, you'd want to
     iterate through both the keys and values in the dictionary.
     Let's see how this is done in an example. Consider this dictionary that uses
     names of actors as keys and their characters as values.

    cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

    print("Iterating through keys:")
    for key in cast:
        print(key)

    print("\nIterating through keys and values:")
    for key, value in cast.items():
        print("Actor: {}    Role: {}".format(key, value))

    Another example:
        # You would like to count the number of fruits in your basket.
        # In order to do this, you have the following dictionary and list of
        # fruits.  Use the dictionary and list to count the total number
        # of fruits, but you do not want to count the other items in your basket.

        result = 0
        basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
        fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

        #Iterate through the dictionary

        #if the key is in the list of fruits, add the value (number of fruits) to result
        for key, value in basket_items.items():
                if key in fruits:
                    result += value


        print(result)

For Loops Vs. While Loops
    Now that you are familiar with both for and while loops, let's consider when it's
     most helpful to use each of them.

    for loops are ideal when the number of iterations is known or finite.

    Examples:

    When you have an iterable collection (list, string, set, tuple, dictionary)
    for name in names:
    When you want to iterate through a loop for a definite number of times, using range()
    for i in range(5):
    while loops are ideal when the iterations need to continue until a condition is met.

    Examples:

    When you want to use comparison operators
    while count <= 100:
    When you want to loop based on receiving specific user input.
    while user_input == 'y':

Zip and Enumerate:
    zip and enumerate are useful built-in functions that can come in handy when dealing
     with loops.

    Zip:
        zip returns an iterator that combines multiple iterables into one sequence of
         tuples. Each tuple contains the elements in that position from all the iterables.

        list(zip(['a', 'b', 'c'], [1, 2, 3])) would output [('a', 1), ('b', 2), ('c', 3)].

        Like we did for range() we need to convert it to a list or iterate through it with
         a loop to see the elements.

        You could unpack each tuple in a for loop like this:
        letters = ['a', 'b', 'c']
        nums = [1, 2, 3]

        for letter, num in zip(letters, nums):
            print("{}: {}".format(letter, num))

        In addition to zipping two lists together, you can also unzip a list into tuples
         using an asterisk.

        some_list = [('a', 1), ('b', 2), ('c', 3)]
        letters, nums = zip(*some_list)

        This would create the same letters and nums tuples we saw earlier.

    Enumerate:
        enumerate is a built in function that returns an iterator of tuples containing
         indices and values of a list. You'll often use this when you want the index
         along with each element of an iterable in a loop.

        letters = ['a', 'b', 'c', 'd', 'e']
        for i, letter in enumerate(letters):
            print(i, letter)

        This code would output:
            0 a
            1 b
            2 c
            3 d
            4 e

List Comprehensions:
    This code:
        squares = []
        for x in range(9):
            squares.append(x**2)
        print(squares)

    is equal to:
        squares =  [x**2 for x in range(9)]
        print(squares)

    In Python, you can create lists really quickly and concisely with list comprehensions. This example from earlier:

    capitalized_cities = []
    for city in cities:
        capitalized_cities.append(city.title())
    can be reduced to:

    capitalized_cities = [city.title() for city in cities]
    List comprehensions allow us to create a list using a for loop in one step.

    You create a list comprehension with brackets [], including an expression to evaluate
     for each element in an iterable. This list comprehension above calls city.title()
     for each element city in cities, to create each element in the new list,
     capitalized_cities.

    Conditionals in List Comprehensions
    You can also add conditionals to list comprehensions (listcomps). After the iterable,
     you can use the if keyword to check a condition in each iteration.

    squares = [x**2 for x in range(9) if x % 2 == 0]
    The code above sets squares equal to the list [0, 4, 16, 36, 64], as x to the power
     of 2 is only evaluated if x is even. If you want to add an else, you will get a
     syntax error doing this.

    squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3]
    If you would like to add else, you have to move the conditionals to the beginning
     of the listcomp, right after the expression, like this.

    squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
    List comprehensions are not found in other languages, but are very common in Python.

Functions:
    Function scope:
    Python doesn't allow functions to modify variables that are outside the function's
     scope. A better way would be to pass the variable as an argument and reassign
     it outside the function.
        - However functions can call global variables inside the scope.

    This trows an error:
        egg_count = 0

        def buy_eggs():
            egg_count += 12 # purchase a dozen eggs

        buy_eggs()

    You should use:
        egg_count = 0

        def buy_eggs(count):
            return count + 12  # purchase a dozen eggs

        egg_count = buy_eggs(egg_count)

Documentation:
    Documentation is used to make your code easier to understand and use. Functions
     are especially readable because they often use documentation strings, or docstrings.
     Docstrings are a type of comment used to explain the purpose of a function,
     and how it should be used. Here's a function for population density with a docstring.

     def population_density(population, land_area):
        """Calculate the population density of an area. """
        return population / land_area

Lambda Expressions:
    You can use lambda expressions to create anonymous functions. That is, functions
     that don’t have a name. They are helpful for creating quick functions that aren’t
     needed later in your code. This can be especially useful for higher order functions,
     or functions that take in other functions as arguments.

     With a lambda expression, this function:
        def multiply(x, y):
        return x * y

        can be reduced to:

        multiply = lambda x, y: x * y

        Both of these functions are used in the same way. In either case, we can call
         multiply like this:

        multiply(4, 7)

Iterators And Generators:
    Iterables are objects that can return one of their elements at a time, such as a list.
     Many of the built-in functions we’ve used so far, like 'enumerate,'
     return an iterator.

    An iterator is an object that represents a stream of data. This is different from a
     list, which is also an iterable, but not an iterator because it is not a stream
     of data.

    Generators are a simple way to create iterators using functions. You can also
     define iterators using classes.

     "Generators == functions that produce an iterator"

     Ex:

        def my_range(x):
            i = 0
            while i < x:
                yield i
                i += 1

    "Generators are a lazy way to build iterables. They are useful when the fully realized
     list would not fit in memory, or when the cost to calculate each list element is
     high and you want to do it as late as possible. But they can only be iterated over
     once."

Generator Expressions:
    Here's a cool concept that combines generators and list comprehensions! You can
     actually create a generator in the same way you'd normally write a list comprehension,
     except with parentheses instead of square brackets. For example:

         sq_list = [x**2 for x in range(10)]  # this produces a list of squares

         sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

Try Statement:
    We can use try statements to handle exceptions. There are four clauses you can use
     (one more in addition to those shown in the video).

    try: This is the only mandatory clause in a try statement. The code in this block is
     the first thing that Python runs in a try statement.
    except: If Python runs into an exception while running the try block, it will jump to
     the except block that handles that exception.
    else: If Python runs into no exceptions while running the try block, it will run
     the code in this block after running the try block.
    finally: Before Python leaves this try statement, it will run the code in this finally
     block under any conditions, even if it's ending the program. E.g.,
     if Python ran into an error while running code in the except or else block, this
     finally block will still be executed before stopping the program.

     try:
        # some code
    except ValueError:
        # some code
    except KeyboardInterrupt:
        # some code
    except Exception as e:
       # some code
       print("Exception occurred: {}".format(e))
    finally:
        # some code

    -Exception is just the base class for all built-in exceptions.

Using files:

    How to grab files:
        f = open('/my_path/my_file.txt', 'r')

    Reading the file content:
        file_data = f.read()
        -There's a limit of max open files depending on your OS

    Writing to a File:
        f = open('my_path/my_file.txt', 'w') - the 'w' means write
        f.write("Hello there!")
        f.close()

    Closing: (Always remember to close your files)
        f.close()

Using "With" and files:
    This with keyword allows you to open a file, do operations on it, and automatically
     close it after the indented code is executed, in this case, reading from the file.
     Now, we don’t have to call f.close()! You can only access the file object, f,
     within this indented block.

    with open('my_path/my_file.txt', 'r') as f:
        file_data = f.read()

Calling the read Method with an Integer
    In the code you saw earlier, the call to f.read() had no arguments passed to it.
     This defaults to reading all the remainder of the file from its current position
     - the whole file. If you pass the read method an integer argument, it will read
     up to that number of characters, output all of them, and keep the 'window' at that
     position ready to read on.

    Example:
    camelot.txt:
        "We're the knights of the round table
        We dance whenever we're able"

    with open("camelot.txt") as song:
        print(song.read(2))
        print(song.read(8))
        print(song.read())

    output:
        We
        're the
        knights of the round table
        We dance whenever we're able

Importing Local Scripts:
    We can actually import Python code from other scripts, which is helpful if you are
     working on a bigger project where you want to organize your code into multiple
     files and reuse code in those files. If the Python script you want to import is
     in the same directory as your current script, you just type import followed by
     the name of the file, without the .py extension.

     Ex:
     import useful_functions

    We can add an alias to an imported module to reference it with a different name.
     import useful_functions as uf
     uf.add_five([1, 2, 3, 4])

Using a main block:
    To avoid running executable statements in a script when it's imported as a module in
     another script, include these lines in an if __name__ == "__main__" block.
     Or alternatively, include them in a function called main() and call this in the if
     main block.

    Whenever we run a script like this, Python actually sets a special built-in variable
     called __name__ for any module. When we run a script, Python recognizes this
     module as the main program, and sets the __name__ variable for this module to
     the string "__main__". For any modules that are imported in this script,
     this built-in __name__ variable is just set to the name of that module.
     Therefore, the condition if __name__ == "__main__"is just checking whether this
     module is the main program.

    def mean(num_list):
    return sum(num_list) / len(num_list)

    def add_five(num_list):
        return [n + 5 for n in num_list]

    def main():
        print("Testing mean function")
        n_list = [34, 44, 23, 46, 12, 24]
        correct_mean = 30.5
        assert(mean(n_list) == correct_mean)

        print("Testing add_five function")
        correct_list = [39, 49, 28, 51, 17, 29]
        assert(add_five(n_list) == correct_list)

        print("All tests passed!")

    if __name__ == '__main__': This line indicates that the code below here
        main()                  will only run if you execute this file!

Modules can be imported:
    They work as libraries
    The Python Standard Library has a lot of modules! To help you get familiar with
     what's available, here are a selection of our favourite Python Standard
     Library modules and why we use them!

    csv: very convenient for reading and writing csv files
    collections: useful extensions of the usual data types including OrderedDict,
     defaultdict and namedtuple
    random: generates pseudo-random numbers, shuffles sequences randomly and chooses
     random items
    string: more functions on strings. This module also contains useful collections
     of letters like string.digits (a string containing all characters which are
     valid digits).
    re: pattern-matching in strings via regular expressions
    math: some standard mathematical functions
    os: interacting with operating systems
    os.path: submodule of os for manipulating path names
    sys: work directly with the Python interpreter
    json: good for reading and writing json files (good for web work)

Techniques for Importing Modules:
    To import an individual function or class from a module:
        from module_name import object_name
    To import multiple individual objects from a module:
        from module_name import first_object, second_object
    To rename a module:
        import module_name as new_name
    To import an object from a module and rename it:
        from module_name import object_name as new_name
    To import every object individually from a module (DO NOT DO THIS):
        from module_name import *
    If you really want to use all of the objects from a module, use the standard import
     module_name statement instead and access each of the objects with the dot notation.
        import module_name

Third-Party Libraries:
    There are tens of thousands of third-party libraries written by independent developers!
     You can install them using pip, a package manager that is included with Python 3.
     pip is the standard package manager for Python, but it isn't the only one.
     One popular alternative is Anaconda which is designed specifically for data science.

    To install a package using pip, just enter "pip install" followed by the name of the
     package in your command line like this: pip install package_name.
     This downloads and installs the package so that it's available to import in
     your programs. Once installed, you can import third-party packages using the
     same syntax used to import from the standard library.

    You can use pip to install all of a project's dependencies at once by typing
     pip install -r requirements.txt in your command line.

Useful Third-Party Packages:
    Being able to install and import third party libraries is useful, but to be an
     effective programmer you also need to know what libraries are available
     for you to use. People typically learn about useful new libraries from online
     recommendations or from colleagues. If you're a new Python programmer you may
     not have many colleagues, so to get you started here's a list of packages that
     are popular with engineers at Udacity.

    IPython - A better interactive Python interpreter
    requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
    Flask - a lightweight framework for making web applications and APIs.
    Django - A more featureful framework for making web applications. Django is particularly good for designing
     complex, content heavy, web applications.
    Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
    pytest - extends Python's builtin assertions and unittest module.
    PyYAML - For reading and writing YAML files.
    NumPy - The fundamental package for scientific computing with Python. It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
    pandas - A library containing high-performance, data structures and data analysis tools. In particular, pandas provides dataframes!
    matplotlib - a 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments.
    ggplot - Another 2D plotting library, based on R's ggplot2 library.
    Pillow - The Python Imaging Library adds image processing capabilities to your Python interpreter.
    pyglet - A cross-platform application framework intended for game development.
    Pygame - A set of Python modules designed for writing games.
    pytz - World Timezone Definitions for Python

Why Object-Oriented Programming?
    Object-oriented programming has a few benefits over procedural programming, which
     is the programming style you first learned.

    Object-oriented programming allows you to create large, modular programs that can
     easily expand over time.
    Object-oriented programs hide implementation from the end-user

Objects:
    Objects have characteristics and actions

    Characteristics and actions in English grammar:
        You can also think about characteristics and actions is in terms of English grammar.
         A characteristic corresponds to a noun and an action corresponds to a verb.

        Let's pick something from the real world: a dog. Some characteristics of the
         dog include the dog's weight, color, breed, and height. These are all nouns.
         Some actions a dog can take include to bark, to run, to bite, and to eat.
         These are all verbs.

Object-oriented programming (OOP) vocabulary:
    Class: A blueprint consisting of methods and attributes.
    Object: An instance of a class. It can help to think of objects as something in
     the real world like a yellow pencil, a small dog, or a blue shirt.
     However, as you'll see later in the lesson, objects can be more abstract.
    Attribute: A descriptor or characteristic. Examples would be color, length, size, etc.
     These attributes can take on specific values like blue, 3 inches, large, etc.
    Method: An action that a class or object could take.
    OOP: A commonly used abbreviation for object-oriented programming.
    Encapsulation: One of the fundamental ideas behind object-oriented programming
     is called encapsulation: you can combine functions and data all into a single entity.
     In object-oriented programming, this single entity is called a class. Encapsulation
     allows you to hide implementation details, much like how the scikit-learn package
     hides the implementation of machine learning algorithms.
    In English, you might hear an attribute described as a property, description, feature,
     quality, trait, or characteristic. All of these are saying the same thing.

Function versus method:
    A function and a method look very similar. They both use the def keyword.
     They also have inputs and return outputs. The difference is that a method is
     inside of a class whereas a function is outside of a class.

Class example:
    class Shirt:
        def __init__ (self, shirt_color, shirt_size, shirt_style, shirt_price):
            self.color = shirt_color
            self.size = shirt_size
            self.style = shirt_style
            self.price = shirt_price

        def change_price(self, new_price):
            self.price = new_price

        def discount(self, discount):
            return self.price * (1 - discount)

    Instantiating and using an object might look like the following code:

    shirt_one = Shirt('yellow', 'M', 'long-sleeve', 15)
    print(shirt_one.get_price())
    shirt_one.set_price(10)

    Attributes:
        There are some drawbacks to accessing attributes directly versus writing a method
         for accessing attributes.

         In terms of object-oriented programming, the rules in Python are a bit looser
          than in other programming languages. As previously mentioned, in some
          languages, like C++, you can explicitly state whether or not an object should
          be allowed to change or access an attribute's values directly. Python does not
          have this option.

          Why might it be better to change a value with a method instead of directly?
           Changing values via a method gives you more flexibility in the long-term.
           What if the units of measurement change, like if the store was originally
           meant to work in US dollars and now has to handle Euros?

           If you had used a method, then you would only have to change the method
            to convert from dollars to Euros.

    Modularized code:
        If you were developing a software program, you would want to modularize this code.
         You would put the Shirt class into its own Python script, which you might call
         shirt.py. In another Python script, you would import the Shirt class with a line
         like from shirt import Shirt.

    Docstrings and object-oriented code:
        The following example shows a class with docstrings. Here are a few things to
         keep in mind:

        - Make sure to indent your docstrings correctly or the code will not run.
         A docstring should be indented one indentation underneath the class or method
         being described.
        - You don't have to define self in your method docstrings. It's understood that
         any method will have self as the first method input.

         class Pants:
            """The Pants class represents an article of clothing sold in a store
            """

            def __init__(self, color, waist_size, length, price):
                """Method for initializing a Pants object

                Args:
                    color (str)
                    waist_size (int)
                    length (int)
                    price (float)

                Attributes:
                    color (str): color of a pants object
                    waist_size (str): waist size of a pants object
                    length (str): length of a pants object
                    price (float): price of a pants object
                """

                self.color = color
                self.waist_size = waist_size
                self.length = length
                self.price = price

            def change_price(self, new_price):
                """The change_price method changes the price attribute of a pants object

                Args:
                    new_price (float): the new price of the pants object

                Returns: None

                """
                self.price = new_price

            def discount(self, percentage):
                """The discount method outputs a discounted price of a pants object

                Args:
                    percentage (float): a decimal representing the amount to discount

                Returns:
                    float: the discounted price
                """
                return self.price * (1 - percentage)

Inheritance:
    Instead of rewrintg codes you can use inheritance in python for defining children
     classes, like kinds of dogs.

    Example:
    class Clothing:
        def __init__ (self, color, size, style, price):
            self.color = color
            self.size = size
            self.style = style
            self.price = price

        def change_price(self, new_price):
            self.price = new_price

        def discount(self, discount):
            return self.price * (1 - discount)

    class Shirt(Clothing):
        def __init__ (self, color, size, style, price, long_or_short):
            Clothing.__init__(self, color, size, style, price)
            self.long_or_short = long_or_short

        def double_price(self):
            self.price *= 2

    class Pants(Clothing):
        def __init__ (self, color, size, style, price, waist):
            Clothing.__init__(self, color, size, style, price)
            self.waist = waist

        def calculate_discount(self discount):
            return self.price * (1 - discount / 2)

You've seen so far:
    Classes and objects
    Attributes and methods
    Magic methods
    Inheritance

    Knowing these topics is enough to start writing object-oriented software.
     What you've learned so far is all you need to know to complete this OOP lesson.
     However, these are only the fundamentals of object-oriented programming.






 '''

print('Hello python') #A função print é usada para exibir informação no console
print('___________________________')
#Tipos
a = 2 #Isto é um inteiro
b = 3.0 #Isto é um float
c = a + b #Isto é uma soma
booleano  = True #Isto é um booleano
booleano2 = False #Isto também é um booleano
string = 'Hello world' #Isto é uma string
string_type = type(string) #você pode usar a função 'type' para identificar o tipo de uma variável
print(string_type)
print('___________________________')
#Concatenação
print(a, b, c, " virgula") #Virgula na função print concatena as variáveis você também pode usar o '+'
print('___________________________')
#Concatenação de strings
print('A vale: ' + str(a) + ' e B vale: ' + str(b) + ' e C vale: ' + str(c))
#Para concatenar usando '+' as variáveis precisam ser todas strings
#A função 'str()' é usada para converter tipos distintos em strings
print('___________________________')
#Entrada em python
nome = input('Qual seu nome? ') #A função input recebe dados do console, a string passada como
#parâmetro é exibida no lugar de entrada.
print('Seu nome: ' + nome)
#Variáveis de entrada são sempre do tipo string, é necessária a tipagem
print('___________________________')
#Operações matemáticas
# '+' mais, '-' menos, '*' vezes, '/' dividio, '**' elevado
quadrado = 10.0 ** 2
raiz = quadrado ** (1/2) #Para calcular a raiz quadrada basta elevar a '1/2'
print( 'Dez ao quadrado: ' + str(quadrado))
print( 'Raiz quadrada de Cem: ' + str(raiz))
#Existem outras formas de calcular a raiz mas é preciso importar bibliotecas
print('___________________________')
'''
    Este é um comentário de  mais de uma linha
    Você pode escrever várias coisas
    em várias linhas é será desconsiderado

    Exercício prático:
    Crie um formulário que pergunte nome, idade, altura cpf, endereço, email e telefone e
    os imprima em um formulário organizado.

 '''
print('Operadores e funções de comparação')
#Em python usamos >, <, <=, >=, !=, == , and, or
#Funções If ,elif else
if booleano:
    print('Seu nome não é Jhonny')

if a > b:
    print(a, ' é maior que ', b)
else:
    print(b, ' é maior que ', a)

#Em python você pode usar 'not' como operador de negação
if not False:
    print('Isso é Verdade!')

'''
    Exercício:
    Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide
    se ela está apta a entrar no exercíto (18 a 30 anos), pesar mais ou igual a 60kg
    e medir mais ou igual a 1,70 metros.

 '''

print('___________________________')
print('Strings e Listas')
#Phyton trata strings como lista de carácteres, ou seja, você pode acessar os caracteres
#por sua posição

texto = 'isto é uma string'
lista = ['isto é uma lista', 3, texto]
listaDeNumerosPares = range(0, 101, 2) #Cria uma lista de números de 0 a 100 pulando de 2 em dois, ou seja apenas os pares
listaDeNumerosImpares = range(1, 102, 2) #Cria uma lista de números de 0 a 101 apenas com números impáres

print(texto[4:16]) #Usando uma string como uma lista exibindo do índice 4 ao 15 pois o 16 não será exibido
print(texto[4:16:2]) #Usando um terceiro índice como escape
lista.append('Adiconado na última posição') #Adicionamos uma nova string a última posição da lista
print(lista) #Podemos usar a função lista.clear() para esaziar a lista

itensNaLista3 = lista.count(3) #Aqui guardamos a quantidade de itens 3 na lista
itensNaLista = len(lista) #Aqui guardamos a quantidade de itens na lista
print(itensNaLista3)
print(itensNaLista)

lista.pop() #Remove o último item de uma Lista
print(lista)
maiuscula = "STRING EM LETRAS MAIUSCULAS ou letras minusculas"
print(maiuscula)
print(maiuscula.lower()) #Passa o valro da string todo para minuscula
print(maiuscula.upper()) #Passa o valor da string toda para MAIUSCULA
#As funções acima não alteram o conteúdo da variável
separada = maiuscula.split('ou') #Criamos uma lista dividindo a string na variável maiuscula
#na string 'ou'
print(separada) #Note que 'ou' não é incluido.

print('___________________________')
print('Estruturas de laço, While e for')

nomes = ['Rodrigo', 'Yasmin', 'Timininha', 'Snarf', 'Keyla', 'Wilson']
#Tipos de for
#For item por item
for nome in nomes:
    print(nome + ' , bom dia!')

listaDeNumeros = range(10) #cria uma lista de 0 a 9 de inteiros
for i in listaDeNumeros:
    print(i)

#Usando range e for juntos
for i in range(6):
    print(i, '- ' + nomes[i])

#Usando range, for e len junntos
for i in range(len(nomes)):
    print("indice", i, '-', nomes[i])

#Usando for em uma string
for i in nomes[0]:
    print(i)

#Exemplo de laço com while
i = 0
while i < 10:
    i += 1 #Outras opções para esta linha: 'i++' ou 'i = i + 1'
    print(i)

#Você pode usar loops
while True:
    print('Este loop executaria para sempre se não fosse o break')
    i += 1
    if i == 13:
        break #Break é uma palavra reservada que pode interromper a execução de um programa
'''
    Exercício: Criar um programa que receba nomes em uma lista e conte todos
    os convidados desta lista
'''
print('___________________________')
print('Estruturas de dados, tuplas, dicionários e conjuntos')
#Tuplas(tuple), são como listas, mas tem tamanho fixo, ou seja, não podem ser alteradas
umaTupla = ('Rodrigo', '36562178', 1.74, 120, 30) #As funções pop e append não funcionam
#Este tipo de estrutra de dados é boa para tamanho fixos e repetidos de informação

#Dicionário(dict)
#Uma lista com chave e valor, pode ser alterada.
umDicionario ={'nome': 'Rodrigo', 'telefone' : '36562178', 'altura' : 1.74, 'peso': 120, 'idade': 30}

#Para exibir os valores dentro de um diciário basta usar as chaves come índice
print(umDicionario['nome'])
#Exibindo todos os valores em um dicionário, sem exibir as chaves
for valores in umDicionario.values():
    print(valores)
#Exibindo todos as chaves em um dicionário, sem exibir os valores
for valores in umDicionario.keys():
    print(valores)

#Você pode alterar os valores usando as chaves
umDicionario['nome'] = 'Rodrigo Montebello Saboya Brito'
print(umDicionario['nome'])

#Conjunto(set)
#Não existem itens repetido em um conjunto assim como em um conjunto matemático,
#Conjuntos são dinâmicos como as listas.
#Conjuntos não são ordenados, não existe índice nos valores
umConjunto = {'Rodrigo', 'Yasmin'}

#Usando operador in para verificar os valores dentro de estruturas de dados,
# este modelo de consulta funciona para todas as estruturas
if 'Rodrigo' in umConjunto and 'Yasmin' in umConjunto:
    print('Somos um casal muito feliz')

umConjunto.add('Tinininha')
print(umConjunto) #Lembrando que esta exibição pode não ser na ordem declarada
# pois conjuntos não tem índices
#IMPORTANTE, conjuntos não aceitam valores repetidos

print('___________________________')
print('Funções e Métodos')
#Entre programadores existe um concenso de que métodos não retornam valores
# apenas tratam entradas, enquanto funções retornam valores.
#Esta é a definição de uma função simples que realiza a soma de dois inteiros
def somar (numero1, numero2):
    resp = int(numero1) + int(numero2)
    return resp

print(somar(20,30))

#Você pode usar funções como argumentos condicionais
if somar(20,30) >= 50:
    print('soma maior que 50')

'''
    Exercício: escreva uma fun;'ao que recebe um objeto de coleção e retorne
    o maior entre eles
 '''
