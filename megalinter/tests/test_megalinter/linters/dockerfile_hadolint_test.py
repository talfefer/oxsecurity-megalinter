# !/usr/bin/env python3
"""
Unit tests for DOCKERFILE linter hadolint
This class has been automatically generated by .automation/build.py, please do not update it manually
"""

from unittest import TestCase

from megalinter.tests.test_megalinter.LinterTestRoot import LinterTestRoot


class dockerfile_hadolint_test(TestCase, LinterTestRoot):
    descriptor_id = "DOCKERFILE"
    linter_name = "hadolint"
