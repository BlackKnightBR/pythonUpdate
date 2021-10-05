'''
    Even though Python lists are great on their own, NumPy has a number of key features
     that give it great advantages over Python lists. Below are a few convincingly
     strong features:
    1.Speed
    2.Multidimensional array data structures
    3.Optimized built-in mathematical functions.

    These are just some of the key features that have made NumPy an essential package
    for scientific computing in Python. In fact, NumPy has become so popular that a
    lot of Python packages, such as Pandas, are built on top of NumPy.

    Good to Read
        You can read how to use NumPy for efficient computation, from the research article
        titled The NumPy array: a structure for efficient numerical computation by Walt et.
        al., 2011. The article is available here.

    Supporting Official Resource
        If you are new to NumPy, we recommend you develop the practice of referring to the
        official NumPy User Guide, whenever you are looking for any numerical utility
        function.
 '''

# Why use NumPy?
import time
# We can import packages into Python using the import command and it has become a
#    convention to import NumPy as np.
import numpy as np
x = np.random.random(100000)

# Case 1
start = time.time()
sum(x) / len(x)
print(time.time() - start)

# Case 2
start = time.time()
np.mean(x)
print(time.time() - start)

'''
    There are several ways to create ndarrays in NumPy. In the following lessons we will
    see two ways to create ndarrays:
        Using regular Python lists
        Using built-in NumPy functions

    In this section, we will create ndarrays by providing Python lists to the NumPy
    np.array() function. This can create some confusion for beginners, but it is
    important to remember that np.array() is NOT a class, it is just a function that
    returns an ndarray. We should note that for the purposes of clarity, the examples
    throughout these lessons will use small and simple ndarrays. Let's start by
    creating 1-Dimensional (1D) ndarrays.

 '''

# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

# Let's print the ndarray we just created using the print() command
print('x = ', x)

'''
    Rank of an Array (numpy.ndarray.ndim)
    Syntax:

    ndarray.ndim
    It returns the number of array dimensions.

    Let's pause for a second to introduce some useful terminology. We refer to 1D arrays as
    rank 1 arrays. In general N-Dimensional arrays have rank N. Therefore, we refer to a
    2D array as a rank 2 array.

 '''

# 1-D array
x = np.array([1, 2, 3])
x.ndim

# 2-D array
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
Y.ndim

# Here the`zeros()` is an inbuilt function that you'll study on the next page.
# The tuple (2, 3, 4( passed as an argument represents the shape of the ndarray
y = np.zeros((2, 3, 4))
y.ndim

'''
    numpy.ndarray.shape
    Syntax:

    ndarray.shape
    It returns a tuple representing the array dimensions. Refer more details here.

    Another important property of arrays is their shape. The shape of an array is the
    size along each of its dimensions. For example, the shape of a rank 2 array
    will correspond to the number of rows and columns of the array. As you will see,
    NumPy ndarrays have attributes that allow us to get information about them in a
    very intuitive way. For example, the shape of an ndarray can be obtained using the
    .shape attribute. The shape attribute returns a tuple of N positive integers that
    specify the sizes of each dimension.

    numpy.dtype
    The type tells us the data-type of the elements. Remember, a NumPy array is
    homogeneous, meaning all elements will have the same data-type. In the example
    below, we will create a rank 1 array and learn how to obtain its shape, its type,
    and the data-type (dtype) of its elements.

 '''

# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

# We print information about x
print('x = ', x)
# We can see that the shape attribute returns the tuple (5,) telling us that x is of
#    rank 1 (i.e. x only has 1 dimension ) and it has 5 elements.
print('x has dimensions:', x.shape)
# The type() function tells us that x is indeed a NumPy ndarray.
print('x is an object of type:', type(x))
# Finally, the .dtype attribute tells us that the elements of x are stored in memory as signed 64-bit integers.
print('The elements in x are of type:', x.dtype)

'''
Another great advantage of NumPy is that it can handle more data-types than Python lists.

As mentioned earlier, ndarrays can also hold strings. Let's see how we can create a rank 1 ndarray of strings in the same manner as before, by providing the np.array() function a Python list of strings.

Example 1.b - Using 1-D Array of Strings
    '''

# We create a rank 1 ndarray that only contains strings
x = np.array(['Hello', 'World'])

# We print information about x
print('x = ', x)
# As we can see the shape attribute tells us that x now has only 2 elements
print('x has dimensions:', x.shape)
# and even though x now holds strings, the type() function tells us that x is still
#   an ndarray as before.
print('x is an object of type:', type(x))
# In this case however, the .dtype attribute tells us that the elements in x are
#   stored in memory as Unicode strings of 5 characters.
print('The elements in x are of type:', x.dtype)

'''
    It is important to remember that one big difference between Python lists and
     ndarrays, is that unlike Python lists, all the elements of an ndarray must be
     of the same type. So, while we can create Python lists with both integers
     and strings, we can't mix types in ndarrays. If you provide the np.array()
     function with a Python list that has both integers and strings, NumPy
     will interpret all elements as strings. We can see this in the next example:

    Example 1.c - Using a 1-D Array of Mixed Datatype
 '''

# We create a rank 1 ndarray from a Python list that contains integers and strings
x = np.array([1, 2, 'World'])

# We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

'''
    Using a 1-D Array to Demonstrate Upcasting in Numeric datatype
    Up till now, we have only created ndarrays with integers and strings.
    We saw that when we create an ndarray with only integers, NumPy will
    automatically assign the dtype int64 to its elements. Let's see what
    happens when we create ndarrays with floats and integers.

    Example 1.d - Using a 1-D Array of Int and Float
 '''

# We create a rank 1 ndarray that contains integers
x = np.array([1,2,3])

# We create a rank 1 ndarray that contains floats
y = np.array([1.0,2.0,3.0])

# We create a rank 1 ndarray that contains integers and floats
z = np.array([1, 2.5, 4])

# We print the dtype of each ndarray
print('The elements in x are of type:', x.dtype)
print('The elements in y are of type:', y.dtype)
print('The elements in z are of type:', z.dtype)

'''
    We can see that when we create an ndarray with only floats, NumPy stores the elements
     in memory as 64-bit floating point numbers (float64). However, notice that when
     we create an ndarray with both floats and integers, as we did with the z ndarray
     above, NumPy assigns its elements a float64 dtype as well. This is called upcasting.
     Since all the elements of an ndarray must be of the same type, in this case NumPy
     upcasts the integers in z to floats in order to avoid losing precision in numerical
     computations.

    Using a 1-D Array of Float, and specifying the dtype of each element:

    Even though NumPy automatically selects the dtype of the ndarray, NumPy also allows
     you to specify the particular dtype you want to assign to the elements of the
     ndarray. You can specify the dtype when you create the ndarray using the keyword
     dtype in the np.array() function. Let's see an example:

    Example 1.e - Using a 1-D Array of Float, and specifying the datatype of each
     element as int64
 '''

# We create a rank 1 ndarray of floats but set the dtype to int64
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)

# We print the dtype x
print('x = ', x)
print('The elements in x are of type:', x.dtype)

'''
    We can see that even though we created the ndarray with floats, by specifying the
     dtype to be int64, NumPy converted the floating point numbers into integers
     by removing their decimals. Specifying the data type of the ndarray can be useful
     in cases when you don't want NumPy to accidentally choose the wrong data type,
     or when you only need certain amount of precision in your calculations and you
     want to save memory.

    numpy.ndarray.size and Creating a 2-D array
    Another useful attribute is NumPy.size, which returns the number of elements in
     the array. Let us now look at how we can create a rank 2 ndarray from a nested
     Python list.

    Example 2 - Using a 2-D Array (Rank #2 Array)
 '''

# We create a rank 2 ndarray that only contains integers
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])

print('Y = \n', Y)

# We print information about Y
# We can see that now the shape attribute returns the tuple (4,3) telling us that
#  Y is of rank 2 and it has 4 rows and 3 columns.
print('Y has dimensions:', Y.shape)
# The .size attribute tells us that Y has a total of 12 elements.
print('Y has a total of', Y.size, 'elements')
print('Y is an object of type:', type(Y))
# Notice that when NumPy creates an ndarray it automatically assigns its dtype based
# on the type of the elements you used to create the ndarray.
print('The elements in Y are of type:', Y.dtype)

'''
    Save the NumPy array to a File
    Once you create an ndarray, you may want to save it to a file to be read later or
     to be used by another program. NumPy provides a way to save the arrays into files
     for later use - let's see how this is done.

    Example 3 - Save the NumPy array to a File
 '''

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We save x into the current directory as
np.save('my_array', x)

# The above saves the x ndarray into a file named my_array.npy. You can load the
# saved ndarray into a variable by using the load() function.

# We load the saved array from our current directory into variable y
y = np.load('my_array.npy')

# We print y
print()
print('y = ', y)
print()

# We print information about the ndarray we loaded
print('y is an object of type:', type(y))
print('The elements in y are of type:', y.dtype)

# When loading an array from a file, make sure you include the name of the file
# together with the extension .npy, otherwise you will get an error.

'''
    Using Built-in Functions to Create ndarrays:

    One great time-saving feature of NumPy is its ability to create ndarrays using
     built-in functions. These functions allow us to create certain kinds of ndarrays
     with just one line of code. Below we will see a few of the most useful built-in
     functions for creating ndarrays that you will come across when doing AI programming.

    Let's start by creating an ndarray with a specified shape that is full of zeros.
     We can do this by using the np.zeros() function. The function np.zeros(shape)
     creates an ndarray full of zeros with the given shape. So, for example, if you
     wanted to create a rank 2 array with 3 rows and 4 columns, you will pass the
     shape to the function in the form of (rows, columns), as in the example below:

    Example 1. Create a Numpy array of zeros with a desired shape
 '''

# We create a 3 x 4 ndarray full of zeros.
X = np.zeros((3,4))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
# As we can see, the np.zeros() function creates by default an array with dtype float64.
# If desired, the data type can be changed by using the keyword dtype.
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

'''
    Similarly, we can create an ndarray with a specified shape that is full of ones.
     We can do this by using the np.ones() function. Just like the np.zeros() function,
     the np.ones() function takes as an argument the shape of the ndarray you want to
     make. Let's see an example:

    Example 2. Create a Numpy array of ones:
 '''
# We create a 3 x 2 ndarray full of ones.
X = np.ones((3,2))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

# We create a 2 x 3 ndarray full of fives.
X = np.full((2,3), 5)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

# We create a 5 x 5 Identity matrix.
X = np.eye(5)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

# Create a 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50
# on its main diagonal
X = np.diag([10,20,30,50])

# We print X
print()
print('X = \n', X)
print()

# We create a rank 1 ndarray that has sequential integers from 0 to 9
x = np.arange(10)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 1 ndarray that has sequential integers from 4 to 9.
x = np.arange(4,10)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 1 ndarray that has evenly spaced integers from 1 to 13 in steps of 3.
x = np.arange(1,14,3)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.
x = np.linspace(0,25,10)

# We print the ndarray
print()
print('x = \n', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25,
# with 25 excluded.
x = np.linspace(0,25,10, endpoint = False)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a rank 1 ndarray with sequential integers from 0 to 19
x = np.arange(20)

# We print x
print()
print('Original x = ', x)
print()

# We reshape x into a 4 x 5 ndarray
x = np.reshape(x, (4,5))

# We print the reshaped x
print()
print('Reshaped x = \n', x)
print()

# We print information about the reshaped x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# We create a a rank 1 ndarray with sequential integers from 0 to 19 and
# reshape it to a 4 x 5 array
Y = np.arange(20).reshape(4, 5)

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)

# We create a rank 1 ndarray with 10 integers evenly spaced between 0 and 50,
# with 50 excluded. We then reshape it to a 5 x 2 ndarray
X = np.linspace(0,50,10, endpoint=False).reshape(5,2)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

# We create a 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
X = np.random.random((3,3))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in x are of type:', X.dtype)

# We create a 1000 x 1000 ndarray of random floats drawn from normal (Gaussian) distribution
# with a mean of zero and a standard deviation of 0.1.
X = np.random.normal(0, 0.1, size=(1000,1000))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
print('The elements in X have a mean of:', X.mean())
print('The maximum value in X is:', X.max())
print('The minimum value in X is:', X.min())
print('X has', (X < 0).sum(), 'negative numbers')
print('X has', (X > 0).sum(), 'positive numbers')

# Using the Built-in functions you learned about on the
# previous page, create a 4 x 4 ndarray that only
# contains consecutive even numbers from 2 to 32 (inclusive)

X = np.linspace(2,32,16).reshape(4,4)

# We print X
print()
print('X = \n', X)
print()

# We create a rank 1 ndarray that contains integers from 1 to 5
x = np.array([1, 2, 3, 4, 5])

# We print x
print()
print('x = ', x)
print()

# Let's access some elements with positive indices
print('This is First Element in x:', x[0])
print('This is Second Element in x:', x[1])
print('This is Fifth (Last) Element in x:', x[4])
print()

# Let's access the same elements with negative indices
print('This is First Element in x:', x[-5])
print('This is Second Element in x:', x[-4])
print('This is Fifth (Last) Element in x:', x[-1])

# We create a rank 1 ndarray that contains integers from 1 to 5
x = np.array([1, 2, 3, 4, 5])

# We print the original x
print()
print('Original:\n x = ', x)
print()

# We change the fourth element in x from 4 to 20
x[3] = 20

# We print x after it was modified
print('Modified:\n x = ', x)

# We create a 3 x 3 rank 2 ndarray that contains integers from 1 to 9
X = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print X
print()
print('X = \n', X)
print()

# Let's access some elements in X
print('This is (0,0) Element in X:', X[0,0])
print('This is (0,1) Element in X:', X[0,1])
print('This is (2,2) Element in X:', X[2,2])

# We create a 3 x 3 rank 2 ndarray that contains integers from 1 to 9
X = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print the original x
print()
print('Original:\n X = \n', X)
print()

# We change the (0,0) element in X from 1 to 20
X[0,0] = 20

# We print X after it was modified
print('Modified:\n X = \n', X)

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print x
print()
print('Original x = ', x)

# We delete the first and last element of x
x = np.delete(x, [0,4])

# We print x with the first and last element deleted
print()
print('Modified x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We delete the first row of y
w = np.delete(Y, 0, axis=0)

# We delete the first and last column of y
v = np.delete(Y, [0,2], axis=1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)

# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We create a rank 2 ndarray
Y = np.array([[1,2,3],[4,5,6]])

# We print x
print()
print('Original x = ', x)

# We append the integer 6 to x
x = np.append(x, 6)

# We print x
print()
print('x = ', x)

# We append the integer 7 and 8 to x
x = np.append(x, [7,8])

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We append a new row containing 7,8,9 to y
v = np.append(Y, [[7,8,9]], axis=0)

# We append a new column containing 9 and 10 to y
q = np.append(Y,[[9],[10]], axis=1)

# We print v
print()
print('v = \n', v)

# We print q
print()
print('q = \n', q)

# We create a rank 1 ndarray
x = np.array([1, 2, 5, 6, 7])

# We create a rank 2 ndarray
Y = np.array([[1,2,3],[7,8,9]])

# We print x
print()
print('Original x = ', x)

# We insert the integer 3 and 4 between 2 and 5 in x.
x = np.insert(x,2,[3,4])

# We print x with the inserted elements
print()
print('x = ', x)

# We print Y
print()
print('Original Y = \n', Y)

# We insert a row between the first and last row of y
w = np.insert(Y,1,[4,5,6],axis=0)

# We insert a column full of 5s between the first and second column of y
v = np.insert(Y,1,5, axis=1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)

# We create a rank 1 ndarray
x = np.array([1,2])

# We create a rank 2 ndarray
Y = np.array([[3,4],[5,6]])

# We print x
print()
print('x = ', x)

# We print Y
print()
print('Y = \n', Y)

# We stack x on top of Y
z = np.vstack((x,Y))

# We stack x on the right of Y. We need to reshape x in order to stack it on the right of Y.
w = np.hstack((Y,x.reshape(2,1)))

# We print z
print()
print('z = \n', z)

# We print w
print()
print('w = \n', w)

'''
    In addition to being able to access individual elements one at a time, NumPy
     provides a way to access subsets of ndarrays. This is known as slicing.
     Slicing is performed by combining indices with the colon : symbol inside
     the square brackets. In general you will come across three types of slicing:

    1. ndarray[start:end]
    2. ndarray[start:]
    3. ndarray[:end]

    The first method is used to select elements between the start and end indices.
     The second method is used to select all elements from the start index till the
     last index. The third method is used to select all elements from the first index
     till the end index. We should note that in methods one and three, the end index
     is excluded. We should also note that since ndarrays can be multidimensional,
     when doing slicing you usually have to specify a slice for each dimension of the
     array.

     # Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
     # Afterwards use Boolean indexing to pick out only the odd numbers in the array
'''

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
X = np.arange(1,26).reshape(5,5)

# Use Boolean indexing to pick out only the odd numbers in the array
Y = X[X % 2 != 0]
