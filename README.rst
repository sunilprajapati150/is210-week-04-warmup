####################
IS 210 Assignment 04
####################
************
Warmup Tasks
************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210

Overview
========

In this assignment, we'll focus on the construction of basic functions. The
functions we create will be intentionally simple to make it easier to isolate
the task at hand.

Instructions
============

The following tasks will either have you interacting with existing files in
the assignment repository or creating new ones on the fly. Don't forget to add
your interpreter directive, utf-8 encoding, and a short docstring with any new
files that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Warmup Tasks
============

Task 01
-------

Functions have their own documentation standards which are covered in the
Google Python Style Guide. Document the function found here appropriately.

.. warning::

    Neither Lint nor Unit tests will test the quality of your documentation or
    whether or not it's formatted correctly. You must document each function
    correctly in order to receive credit.

.. hint::

    Indentation and spacing both matter so pay attention to how you indent the
    headers and the sections.
    
.. hint::

    Remember that optional parameters should be indicated as-such in their
    declaration!

Specifications
^^^^^^^^^^^^^^

1.  Document the function in ``task_01.py`` according to the Google Python
    Style Guide.

.. hint::

    You can use the ``help()`` function to test your docstring as below.

Examples
^^^^^^^^

.. code:: pycon

    >>> import task_01
    >>> help(task_01.know_what_i_mean)

Task 02
-------

Calling a function is already something we've done a few times but let's
practice it again just to make sure we've connected the dots.

Specifications
^^^^^^^^^^^^^^

1.  Open ``hamlet.py`` to get a sense of what this function does.

2.  Open ``task_02.py`` and call the ``hamlet.crazy_math()`` math function
    assigning it the following parameters in order:

    1.  4

    2.  100000

    3.  8

    4.  98

3.  Assign the returned result to a new global variable named ``POSITIONAL``

Examples
^^^^^^^^

.. code:: pycon

    >>> import task_02
    >>> print task_02.POSITIONAL
    0.00374391674995

Task 03
-------

Positional parameters may suffice in many cases but most programmers prefer to
use keyword arguments. Here you'll call a function with keyword arguments
instead of positional parameters.

Specifications
^^^^^^^^^^^^^^

1.  Open ``hamlet.py`` to get a sense of what this function does.

2.  Open ``task_03.py`` and call the ``hamlet.crazy_math()`` math function
    assigning it the following parameters by keyword reference:

    1.  bananas: 48

    2.  monkeys: 84

    3.  hours: 200000

3.  Assign the returned result to a new global variable named ``KEYWORD``

Examples
^^^^^^^^

.. code:: pycon

    >>> import task_03
    >>> print task_03.KEYWORD
    0.00879168510437

Task 04
-------

In this task, you'll be defining a function with three parameters.

Specifications
^^^^^^^^^^^^^^

1.  Create a new file names ``task_04.py``

2.  Define a new function named ``too_many_kittens`` that takes three
    arguments, in order:

    1.  kittens, the number of kittens

    2.  litterboxes, the (integer) number of available litterboxes

    3.  catfood, a boolean representing whether or not any catfood exists

3.  In the function return the value of the following comparison statement:

    .. code:: python

        not (litterboxes >= kittens and catfood)

    This statement ensures we have at least one litterbox for each kitten and
    that we have some catfood. It then uses inversion via ``not`` to answer
    whether or not we have too many kittens.

.. note::

    Note the spacing of the ``not`` operator. There should always be spacing
    around all logical operators like ``and``, ``not`` or ``or``. Without it,
    ``not`` would look like a function, eg ``not()``.

..  note::

    A fun fact of the polymorphic properties of python is the fact that
    truthiness would allow ``catfood`` to either be a boolean (eg, ``True``) or
    some number like ``0`` or even ``None`` and this would continue to operate
    in a reasonably sane manner.

Examples
^^^^^^^^

.. code:: pycon

    >>> too_many_kittens(12, 12, False)
    True
    
    >>> too_many_kittens(13, 12, True)
    True

    >>> too_many_kittens(12, 13, True)
    False

Task 05
-------

Here we'll set a default value in our function definition.

Specifications
^^^^^^^^^^^^^^

1.  Create a file named ``task_05.py``

2.  Create a new function named ``defaults`` with two parameters:
    
    1.  ``my_optional`` which has a default value of True

    2.  ``my_required`` which is a required param and has no default value

3.  Return the following logical comparison:

    .. code:: python

        my_optional is my_required

Examples
^^^^^^^^

.. code:: pycon

    >>> defaults(True)
    True

    >>> defaults(True, False)
    False

    >>> defaults(False, False)
    True

Executing Tests
===============

Code must be functional and pass tests before it will be eligible for credit.

Linting
-------

Lint tests check your code for syntactic or stylistic errors To execute lint
tests against a specific file, simply open a terminal in the same directory as
your code repository and type:

.. code:: console

    $ pylint filename.py

Where ``filename.py`` is the name of the file you wish to lint test.

Unit Tests
----------

Unit tests check that your code performs the tested objectives. Unit tests
may be executed individually by opening a terminal in the same directory as
your code repository and typing:

.. code:: console

    $ nosetests tests/name_of_test.py

Where ``name_of_test.py`` is the name of the testfile found in the ``tests``
directory of your source code.

Running All Tests
-----------------

All tests may be run simultaneously by executing the ``runtests.sh`` script
from the root of your assignment repository. To execute all tests, open a
terminal in the same directory as your code repository and type:

.. code:: console

    $ ./runtests.sh

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Week Two.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
