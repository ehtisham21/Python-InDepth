#Testing a Function
def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + last
    return full_name.title()

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
        last = input("Please give me a last name: ")
    if last == 'q':
        break
        formatted_name = get_formatted_name(first, last)
        print("\tNeatly formatted name: " + formatted_name + '.')

#Unit Tests and Test Cases
#A Passing Test
import unittest
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin') #assertEqual methods verify that a result you received matches the result you expected to receive.
unittest.main()

#A Failing Test
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name."""
    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
unittest.main()

# ======================================================================
# ERROR: test_first_last_name (__main__.NamesTestCase)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
# File "test_name_function.py", line 8, in test_first_last_name
# formatted_name = get_formatted_name('janis', 'joplin')
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s
# FAILED (errors=1)
