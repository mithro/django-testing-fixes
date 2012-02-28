====================
Django Testing Fixes
====================

A set of fixes for various broken things about django testing.

fix_exceptions.py      - Uncaught exceptions when testing cause the django
                         debug page.

fix_finish_response.py - Fixes problems where testing client closes it's socket
                         early.

fix_fixtures.py        - Causes an error to occur when a fixture is not found
                         during a unit test.

testing_context.py     - Provides a TESTING=True value in templates.


suite.py
  TestSuiteRunner()
    A better test suite runner which provides better ability to filter tests.
    You can specify the exact test/module/etc.

  create_suite(location, modulename)
    Find all tests under a given directory (location) which contains
    modulename.

    Tests should end with _test.py

