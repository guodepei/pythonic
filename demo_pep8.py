#!/bin/python3
# demo_pep3.py - a demo of python3 program with PEP8

'''A one file demo of python3 program with PEP8

For usage, try this:
$ python demo.py
'''


class DemoPep8():
    '''This is a class showing all the elements of PEP8'''
    # https://www.python.org/dev/peps/pep-0008/
    def __init__(self,name):
        self.name = name


class Pep8CodeLayout(DemoPep8):
    # Add 4 spaces (an extra level of indentation) 
    # to distinguish arguments from the rest.
    def long_function_name(
            var_one, var_two, var_three,
            var_four):
        print(var_one)

    def calling_long_function():
        # Aligned with opening delimiter.
        foo = long_function_name(var_one, var_two,
                                 var_three, var_four)

    def if_block():
        # Add some extra indentation on the conditional continuation line.
        if (this_is_one_thing
                and that_is_another_thing):
            do_something()

    def multiline_construct():
        my_list = [
            1, 2, 3,
            4, 5, 6,
        ]
        result = some_function_that_takes_arguments(
            'a', 'b', 'c',
            'd', 'e', 'f',
        )

    def maximum_line_length():
        # Limit all lines to a maximum of 79 characters.
        with open('/path/to/some/file/you/want/to/read') as file_1, \
             open('/path/to/some/file/being/written', 'w') as file_2:
            file_2.write(file_1.read())

    def line_break():
        # Yes: easy to match operators with operands
        income = (gross_wages
                  + taxable_interest
                  + (dividends - qualified_dividends)
                  - ira_deduction
                  - student_loan_interest)

    def imports():
        # Imports are always put at the top of the file, 
        # just after any module comments and docstrings, 
        # and before module globals and constants.
        #
        # Imports should be grouped in the following order:
        #
        #     Standard library imports.
        #     Related third party imports.
        #     Local application/library specific imports.
        #
        # You should put a blank line between each group of imports.
        import os
        import sys
        from subprocess import Popen, PIPE

    def dunder_names():
        """This is the example module.

        This module does stuff.
        """

        # from __future__ import barry_as_FLUFL

        __all__ = ['a', 'b', 'c']
        __version__ = '0.1'
        __author__ = 'Cardinal Biggles'

        import os
        import sys

    def __init__(self, name, subname):
        self.subname = subname
        DemoPep8.__init__(self, name)



class Pep8Whitespace(DemoPep8):
    from typing import AnyStr
    def whitespace():
        spam(ham[1], {eggs: 2})
        foo = (0,)
        if x == 4: print(x, y); x, y = y, x

        # slice
        ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
        ham[lower:upper], ham[lower:upper:], ham[lower::step]
        ham[lower+offset : upper+offset]
        ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
        ham[lower + offset : upper + offset]

        spam(1)
        dct['key'] = lst[index]
        
        x = 1
        y = 2
        long_variable = 3

        i = i + 1
        submitted += 1
        x = x*2 - 1
        hypot2 = x*x + y*y
        c = (a+b) * (a-b)

    def function_munge1(input: AnyStr):
        pass

    def function_munge2() -> AnyStr:
        pass

    def function_complex(real, imag=0.0):
        return magic(r=real, i=imag)

    def function_munge3(input: AnyStr, sep: AnyStr = None, limit=1000):
        pass

    def __init__(self, name, subname):
        self.subname = subname
        DemoPep8.__init__(self, name)


class Pep8Comments(DemoPep8):
    """This is a subclass showing comments

    This is a docstring.
    Write docstrings for all public modules, functions, classes, and methods.
    """
    def block_comments():
        # Block comments generally apply to some (or all) code
        # that follows them, and are indented to the same level as that code.
        # Each line of a block comment starts with a #
        # and a single space (unless it is indented text
        # inside the comment).

        # Paragraphs inside a block comment are separated by a line
        # containing a single #.
        pass

    def inline_comments():
        pass  # at least two spaces from the statement

    def __init__(self, name, subname):
        self.subname = subname
        DemoPep8.__init__(self, name)


class Pep8NamingConventions(DemoPep8):
    def descriptive():
        lower_case_with_underscores  # functions and variables
        UPPERCASE
        CapitalizedWords  # or CapWords, or CamelCase. Classes
        mixedCase

    def prescriptive():
        # Modules should have short, all-lowercase names. 
        # Underscores can be used in the module name if it improves readability.
        #
        # Python packages should also have short, all-lowercase names,
        # although the use of underscores is discouraged.
        #
        # Class names should normally use the CapWords convention.
        #
        # Modules that are designed for use via 
        #     from M import * 
        # should use the __all__ mechanism to prevent exporting globals,
        # or use the older convention of prefixing such globals with an 
        # underscore
        #
        # *Function* names should be *lowercase*, with words separated by 
        # *underscores* as necessary to improve readability.
        #
        # *Variable* names follow the same convention as function names.
        #
        # mixedCase is allowed only in contexts where that's already the 
        # prevailing style (e.g. threading.py), to retain backwards 
        # compatibility.
        pass

    def function_lowercase_with_underscores():
        CONSTANTS_ALL_CAPITAL_WITH_UNDERSCORES = 999
        variable_name = 'the same'
 
    def __init__(self, name, subname):
        self.subname = subname
        DemoPep8.__init__(self, name)


class Pep8ProgrammingRecommendations(DemoPep8):
    def __init__(self, name, subname):
        self.subname = subname
        DemoPep8.__init__(self, name)


class Pep8iReferences(DemoPep8):
    def __init__(self, name, subname):
        self.subname = subname
        DemoPep8.__init__(self, name)


if __name__ == '__main__':
    # Surround top-level function and class definitions with two blank lines.
    print('Hello world. This is a demo of PEP8.')
