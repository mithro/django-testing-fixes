#!/usr/bin/python
#
# -*- coding: utf-8 -*-
# vim: set ts=4 sw=4 et sts=4 ai:

import os

from django.core.servers import basehttp
from django.conf import settings
from django.db.models import get_app
from django.utils import unittest
from django.test import simple
from django.test import testcases


class TestSuiteRunner(simple.DjangoTestSuiteRunner):
    """A test suite runner which can use a display."""

    def setup_test_environment(self, **kwargs):
        simple.setup_test_environment()
        settings.DEBUG=False
        settings.TEMPLATE_CONTEXT_PROCESSORS = list(settings.TEMPLATE_CONTEXT_PROCESSORS) + [
            'django_testing_fixes.testing_context.extra'
        ]
        unittest.installHandler()

    def filter_suite(self, suite, pred):
        """Recursively filter test cases in a suite based on a predicate."""
        newtests = []
        for test in suite._tests:
            if test.__class__.__name__.endswith('TestSuite'):
                self.filter_suite(test, pred)
                newtests.append(test)
            else:
                if pred(test):
                    newtests.append(test)
        suite._tests = newtests

    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        suite = unittest.TestSuite()

        if test_labels:
            for label in test_labels:
                if '.' in label:
                    appname, test = label.split('.', 1)
                else:
                    appname, test = label, ''

                def filter_test(testcase, testprefix=label):
                    testname = "%s.%s.%s" % (testcase.__class__.__module__, testcase.__class__.__name__, testcase)
                    return testname.startswith(testprefix)

                app = get_app(appname)
                suite.addTest(simple.build_suite(app))
                self.filter_suite(suite, filter_test)
        else:
            for appname in settings.OUR_APPS:
                app = get_app(appname, emptyOK=True)
                if app is None:
                    continue
                suite.addTest(simple.build_suite(app))

        if extra_tests:
            for test in extra_tests:
                suite.addTest(test)

        return simple.reorder_suite(suite, (testcases.TestCase,))


def create_suite(location, modulename):
    suite = unittest.TestSuite()
    for dirpath, dirnames, filenames in os.walk(location):
        for filename in filenames:
            remaining = dirpath[len(os.path.commonprefix([location, dirpath])):].replace('/', '.')
            test = "%s%s.%s" % (modulename, remaining, filename[:-3])

            # Unittest test
            if filename.endswith('_test.py'):
                suite.addTest(unittest.TestLoader().loadTestsFromName(test))

    return suite
