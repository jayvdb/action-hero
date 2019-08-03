import unittest
import functools
import argparse

import requests


__all__ = [
    "CheckAction",
    "CheckPresentInUserValuesAction",
    "MapAction",
    "MapAndReplaceAction",
    "run_only_when_when_internet_is_up",
]


def run_only_when_when_internet_is_up(urls=["http://www.google.com"]):
    """Decorator that runs wrapped function when the internet is up.

    Note:
        - Connection is checked by checking connection to values in urls

    """

    def run_only_when_when_internet_is_up_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Do network check
            try:
                [requests.get(url).raise_for_status() for url in urls]

                func(*args, **kwargs)

            # Do nothing on response error
            except requests.exceptions.RequestException:
                pass

        return wrapper

    return run_only_when_when_internet_is_up_wrapper


class BaseAction(argparse.Action):
    """ArgumentParser Action subclass that runs user's func over values"""

    func = None
    err_msg_singular = None
    err_msg_plural = None

    @classmethod
    def run_user_func(cls, value):
        """Runs cls.func. Used nside __call__

        Note:
            Needs to be @classmethod to avoid
            1. including self when being called in other methods
            2. not including self when calling other funcs within
        """
        return cls.func(value)


class CheckAction(BaseAction):
    """Checks all values return True with func"""

    def __init__(
        self, option_strings, dest, nargs=None, help=None, metavar=None
    ):
        for attr in ["func", "err_msg_singular", "err_msg_plural"]:
            # Use getattr. hasattr returns True as they're initialized to None.
            if not getattr(self, attr):
                raise ValueError(
                    "Please supply required attribute: {}".format(attr)
                )

        super(CheckAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            help=help,
            metavar=metavar,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        # When values are a list of strings
        if isinstance(values, list):
            if not all([self.run_user_func(value) for value in values]):
                raise argparse.ArgumentError(self, self.err_msg_plural)

        # When values is one string
        else:
            value = values
            if not self.run_user_func(value):
                raise argparse.ArgumentError(self, self.err_msg_singular)

        setattr(namespace, self.dest, values)


class CheckPresentInUserValuesAction(BaseAction):
    """Checks result func over each value in values is in user_values"""

    user_values = None

    def __init__(
        self,
        option_strings,
        dest,
        user_values=None,
        nargs=None,
        help=None,
        metavar=None,
    ):
        for attr in ["func", "err_msg_singular", "err_msg_plural"]:
            # Use getattr. hasattr returns True as they're initialized to None.
            if not getattr(self, attr):
                raise ValueError(
                    "Please supply required attribute: {}".format(attr)
                )

        if not user_values:
            # Raise ValueError if user_values not specified
            raise ValueError("Please supply required attribute: user_values")
        else:
            # Raise ValueError if user_values is not of type list
            if not isinstance(user_values, list):
                raise ValueError(
                    "Required attribute user_values has to be of type list"
                )
            # Raise ValueError if user_values list is empty
            elif len(user_values) == 0:
                raise ValueError(
                    "Required attribute user_values cannot be empty list"
                )
            else:
                # Accept init's user_values
                self.user_values = user_values

        super(CheckPresentInUserValuesAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            help=help,
            metavar=metavar,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        # When values are a list of strings
        if isinstance(values, list):
            if not all(
                [
                    self.run_user_func(value) in self.user_values
                    for value in values
                ]
            ):
                raise argparse.ArgumentError(self, self.err_msg_plural)

        # When values is one string
        else:
            value = values
            if not self.run_user_func(value) in self.user_values:
                raise argparse.ArgumentError(self, self.err_msg_singular)

        setattr(namespace, self.dest, values)


class MapAction(BaseAction):
    """Maps func on values"""

    def __init__(
        self, option_strings, dest, nargs=None, help=None, metavar=None
    ):
        for attr in ["func"]:
            # Use getattr. hasattr returns True as they're initialized to None.
            if not getattr(self, attr):
                raise ValueError(
                    "Please supply required attribute: {}".format(attr)
                )

        super(MapAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            help=help,
            metavar=metavar,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        # When values are a list of strings
        if isinstance(values, list):
            [self.run_user_func(value) for value in values]

        # When values is one string
        else:
            value = values
            self.run_user_func(value)

        setattr(namespace, self.dest, values)


class MapAndReplaceAction(BaseAction):
    """Maps func on values and replaces values with the result"""

    def __init__(
        self, option_strings, dest, nargs=None, help=None, metavar=None
    ):
        for attr in ["func"]:
            # Use getattr. hasattr returns True as they're initialized to None.
            if not getattr(self, attr):
                raise ValueError(
                    "Please supply required attribute: {}".format(attr)
                )

        super(MapAndReplaceAction, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            help=help,
            metavar=metavar,
        )

    def __call__(self, parser, namespace, values, option_string=None):
        # When values are a list of strings
        if isinstance(values, list):
            updated = [self.run_user_func(value) for value in values]
            values = updated

        # When values is one string
        else:
            value = values
            updated = self.run_user_func(value)
            values = updated

        setattr(namespace, self.dest, values)


class ExitCapturedArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        """error(message: string)

        Important note from this superclass's error(s, m) docstring:
            If you override this in a subclass, it should not return -- it
            should either exit or raise an exception.

        Reason for overriding superclass error:
            This function is overridden in order to stop the default behavior
            of ArgumentParser to exit when receiving an ArgumentError as that
            convolutes testing.
            So instead of exiting, just constructing the message and passing it
            on as a ValueError that can be captured in testing.
        """
        error_message = "{}s: error: {}s\n".format(self.prog, message)
        raise ValueError(error_message)


class ActionHeroesTestCase(unittest.TestCase):
    """unitests.TestCase subclass that encloses a ExitCapturedArgumentParser

        Reason for a special TestCase:
            1. Enclose parser within setup
            2. The enclosed parser should capture exits and raise ValueError

    """

    def setUp(self):
        """Enclose ExitCapturedArgumentParser as parser"""
        self.parser = ExitCapturedArgumentParser()
