from argparse import Action
from action_heroes.utils import CheckAction, MapAction, MapAndReplaceAction

from action_heroes.path_utils import (
    create_directory,
    create_file,
    is_empty_file,
    is_executable_directory,
    is_executable_file,
    is_executable_path,
    is_existing_directory,
    is_existing_file,
    is_existing_path,
    is_readable_directory,
    is_readable_file,
    is_readable_path,
    is_valid_directory,
    is_valid_file,
    is_valid_path,
    is_writable_directory,
    is_writable_file,
    is_writable_path,
    resolve_path,
)


__all__ = [
    "DirectoryDoesNotExistAction",
    "DirectoryExistsAction",
    "DirectoryIsExecutableAction",
    "DirectoryIsNotExecutableAction",
    "DirectoryIsNotReadableAction",
    "DirectoryIsNotWritableAction",
    "DirectoryIsReadableAction",
    "DirectoryIsValidAction",
    "DirectoryIsWritableAction",
    "EnsureDirectoryAction",
    "EnsureFileAction",
    "FileDoesNotExistAction",
    "FileExistsAction",
    "FileHasExtension",
    "FileIsEmptyAction",
    "FileIsExecutableAction",
    "FileIsNotEmptyAction",
    "FileIsNotExecutableAction",
    "FileIsNotReadableAction",
    "FileIsNotWritableAction",
    "FileIsReadableAction",
    "FileIsValidAction",
    "FileIsWritableAction",
    "PathDoesNotExistsAction",
    "PathExistsAction",
    "PathIsExecutableAction",
    "PathIsNotExecutableAction",
    "PathIsNotReadableAction",
    "PathIsNotWritableAction",
    "PathIsReadableAction",
    "PathIsValidAction",
    "PathIsWritableAction",
    "ResolvePathAction",
]


class ResolvePathAction(MapAndReplaceAction):
    """Resolves path to canonical path removing symbolic links if present"""

    func = resolve_path


class EnsureDirectoryAction(MapAction):
    """Ensure directory exists and create it if it doesnt"""

    @staticmethod
    def _ensure_directory(directory):
        if not is_existing_directory(directory):
            create_directory(directory)

    func = _ensure_directory


class EnsureFileAction(MapAction):
    """Ensure file exists and create it if it doesnt"""

    @staticmethod
    def _ensure_file(filename):
        if not is_existing_directory(filename):
            create_file(filename)

    func = _ensure_file


class PathIsValidAction(CheckAction):
    """Check if path is valid"""

    func = is_valid_path
    err_msg_singular = "Atleast one path is invalid"
    err_msg_plural = "Path is invalid"


class PathExistsAction(CheckAction):
    """Check if Path exists"""

    func = is_existing_path
    err_msg_singular = "Atleast one path does not exist"
    err_msg_plural = "Path does not exist"


class PathDoesNotExistsAction(CheckAction):
    """Check if Path does not exist"""

    def func(value):
        return not is_existing_path(value)

    err_msg_singular = "Atleast one path exists"
    err_msg_plural = "Path exists"


class PathIsWritableAction(CheckAction):
    """Check if path is writable"""

    func = is_writable_path
    err_msg_singular = "Atleast one path is not writable"
    err_msg_plural = "Path is not writable"


class PathIsNotWritableAction(CheckAction):
    """Check if path is not writable"""

    def func(value):
        return not is_writable_path(value)

    err_msg_singular = "Atleast one path is writable"
    err_msg_plural = "Path is writable"


class PathIsReadableAction(CheckAction):
    """Check if path is readable"""

    func = is_readable_path
    err_msg_singular = "Atleast on path is not readable"
    err_msg_plural = "Path is not readable"


class PathIsNotReadableAction(CheckAction):
    """Check if path is not writable"""

    def func(value):
        return not is_readable_path(value)

    err_msg_singular = "Atleast on path is readable"
    err_msg_plural = "Path is readable"


class PathIsExecutableAction(CheckAction):
    """Check if path is executable"""

    func = is_executable_path
    err_msg_singular = "Atleast one path is not executable"
    err_msg_plural = "Path is not executable"


class PathIsNotExecutableAction(CheckAction):
    """Check if path is not executable"""

    def func(value):
        return not is_executable_path(value)

    err_msg_singular = "Atleast one path is executable"
    err_msg_plural = "Path is executable"


class DirectoryExistsAction(CheckAction):
    """Check if Directory exists"""

    func = is_existing_directory
    err_msg_singular = "Atleast one directory does not exist"
    err_msg_plural = "Directory does not exist"


class DirectoryDoesNotExistAction(CheckAction):
    """Check if Directory does not exist"""

    def func(value):
        return not is_existing_directory(value)

    err_msg_singular = "Atleast one directory exists"
    err_msg_plural = "Directory exists"


class DirectoryIsWritableAction(CheckAction):
    """Check if directory is writable"""

    func = is_writable_directory
    err_msg_singular = "Atleast one directory is not writable"
    err_msg_plural = "Directory is not writable"


class DirectoryIsNotWritableAction(CheckAction):
    """Check if directory is not writable"""

    def func(value):
        return not is_writable_directory(value)

    err_msg_singular = "Atleast one directory is not writable"
    err_msg_plural = "Directory is not writable"


class DirectoryIsReadableAction(CheckAction):
    """Check if directory is readable"""

    func = is_readable_directory
    err_msg_singular = "Atleast one directory is not readable"
    err_msg_plural = "Directory is not readable"


class DirectoryIsNotReadableAction(CheckAction):
    """Check if directory is not readable"""

    def func(value):
        return not is_readable_directory(value)

    err_msg_singular = "Atleast one directory is readable"
    err_msg_plural = "Directory is readable"


class DirectoryIsExecutableAction(CheckAction):
    """Check if directory is executable"""

    func = is_executable_directory
    err_msg_singular = "Atleast one directory is not executable"
    err_msg_plural = "Directory is not executable"


class DirectoryIsNotExecutableAction(CheckAction):
    """Check if directory is not executable"""

    def func(value):
        return not is_executable_directory(value)

    err_msg_singular = "Atleast one directory is executable"
    err_msg_plural = "Directory is executable"


class DirectoryIsValidAction(CheckAction):
    """Check directory is valid"""

    func = is_valid_directory
    err_msg_singular = "Atleast one directory is not valid"
    err_msg_plural = "Directory is not valid"


class FileIsWritableAction(CheckAction):
    """Check if file is writable"""

    func = is_writable_file
    err_msg_singular = "Atleast one file is not writable"
    err_msg_plural = "File is not writable"


class FileIsNotWritableAction(CheckAction):
    """Check if file is not writable"""

    def func(value):
        return not is_writable_file(value)

    err_msg_singular = "Atleast one file is writable"
    err_msg_plural = "File is writable"


class FileIsReadableAction(CheckAction):
    """Check if file is readable"""

    func = is_readable_file
    err_msg_singular = "Atleast one file is not readable"
    err_msg_plural = "File is not readable"


class FileIsNotReadableAction(CheckAction):
    """Check if file is not readable"""

    def func(value):
        return not is_readable_file(value)

    err_msg_singular = "Atleast one file is readable"
    err_msg_plural = "File is readable"


class FileIsExecutableAction(CheckAction):
    """Check if file is executable"""

    func = is_executable_file
    err_msg_singular = "Atleast one file is not executable"
    err_msg_plural = "File is not executable"


class FileIsNotExecutableAction(CheckAction):
    """Check if file is not executable"""

    def func(value):
        return not is_executable_file(value)

    err_msg_singular = "Atleast one file is executable"
    err_msg_plural = "File is executable"


class FileIsValidAction(CheckAction):
    """Check file is valid"""

    func = is_valid_file
    err_msg_singular = "Atleast one file is not valid"
    err_msg_plural = "File is not valid"


class FileExistsAction(CheckAction):
    """Check if file exists"""

    func = is_existing_file
    err_msg_singular = "Atleast one file does not exist"
    err_msg_plural = "File does not exist"


class FileDoesNotExistAction(CheckAction):
    """Check if file exists"""

    def func(value):
        return not is_existing_file(value)

    err_msg_singular = "Atleast one file exists"
    err_msg_plural = "File exists"


class FileIsEmptyAction(CheckAction):
    """Check if file is empty"""

    func = is_empty_file
    err_msg_singular = "Atleast one file is not empty"
    err_msg_plural = "File is not empty"


class FileIsNotEmptyAction(CheckAction):
    """Check if file is not empty"""

    def func(value):
        return not is_empty_file(value)

    err_msg_singular = "Atleast one file is empty"
    err_msg_plural = "File is empty"


class FileHasExtension(Action):
    """Check if file has specified extension

    TODO: Accept extension as an argument

    """

    def __init__(self):
        raise NotImplementedError
