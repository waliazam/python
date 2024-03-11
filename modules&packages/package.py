'''
A package is a way of collecting related modules together within a single tree-like hierarchy. Very complex packages like NumPy or SciPy have hundreds of individual modules so they are grouped into subpackages.

Creating a Package
To create a package, you simply need to create a directory and then put your modules into it. The directory must contain a file named __init__.py. This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.

For example, if you create a package named mypackage with one module named mymodule, your structure will look like this:

mypackage/
    __init__.py
    mymodule.py
    
    And you can import it using:
    
    from mypackage import mymodule

'''

'''
Example: Using the datetime Module
Here's a quick example of using the datetime module from the Python Standard Library:
'''

import datetime

now = datetime.datetime.now()

print(f"The current date and time is : {now}")



