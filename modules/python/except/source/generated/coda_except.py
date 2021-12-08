# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _coda_except
else:
    import _coda_except

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class Context(object):
    r"""Proxy of C++ except::Context class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, file: "std::string const &", line: "int", func: "std::string const &", time: "std::string const &", message: "std::string const &"):
        r"""__init__(Context self, std::string const & file, int line, std::string const & func, std::string const & time, std::string const & message) -> Context"""
        _coda_except.Context_swiginit(self, _coda_except.new_Context(file, line, func, time, message))

    def getMessage(self) -> "std::string const &":
        r"""getMessage(Context self) -> std::string const &"""
        return _coda_except.Context_getMessage(self)

    def getTime(self) -> "std::string const &":
        r"""getTime(Context self) -> std::string const &"""
        return _coda_except.Context_getTime(self)

    def getFunction(self) -> "std::string const &":
        r"""getFunction(Context self) -> std::string const &"""
        return _coda_except.Context_getFunction(self)

    def getFile(self) -> "std::string const &":
        r"""getFile(Context self) -> std::string const &"""
        return _coda_except.Context_getFile(self)

    def getLine(self) -> "int":
        r"""getLine(Context self) -> int"""
        return _coda_except.Context_getLine(self)
    mMessage = property(_coda_except.Context_mMessage_get, _coda_except.Context_mMessage_set, doc=r"""mMessage : std::string""")
    mTime = property(_coda_except.Context_mTime_get, _coda_except.Context_mTime_set, doc=r"""mTime : std::string""")
    mFunc = property(_coda_except.Context_mFunc_get, _coda_except.Context_mFunc_set, doc=r"""mFunc : std::string""")
    mFile = property(_coda_except.Context_mFile_get, _coda_except.Context_mFile_set, doc=r"""mFile : std::string""")
    mLine = property(_coda_except.Context_mLine_get, _coda_except.Context_mLine_set, doc=r"""mLine : int""")
    __swig_destroy__ = _coda_except.delete_Context

# Register Context in _coda_except:
_coda_except.Context_swigregister(Context)


def __lshift__(os: "std::ostream &", c: "Context") -> "std::ostream &":
    r"""__lshift__(std::ostream & os, Context c) -> std::ostream &"""
    return _coda_except.__lshift__(os, c)
CODA_OSS_Throwable_isa_std_exception = _coda_except.CODA_OSS_Throwable_isa_std_exception

class Throwable(object):
    r"""Proxy of C++ except::Throwable class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        r"""
        __init__(Throwable self) -> Throwable
        __init__(Throwable self, std::string const & message) -> Throwable
        __init__(Throwable self, Context arg2) -> Throwable
        __init__(Throwable self, Throwable arg2, Context arg3) -> Throwable
        """
        _coda_except.Throwable_swiginit(self, _coda_except.new_Throwable(*args))
    __swig_destroy__ = _coda_except.delete_Throwable

    def getMessage(self) -> "std::string":
        r"""getMessage(Throwable self) -> std::string"""
        return _coda_except.Throwable_getMessage(self)

    def getTrace(self, *args) -> "Trace &":
        r"""
        getTrace(Throwable self) -> Trace const
        getTrace(Throwable self) -> Trace &
        """
        return _coda_except.Throwable_getTrace(self, *args)

    def getType(self) -> "std::string":
        r"""getType(Throwable self) -> std::string"""
        return _coda_except.Throwable_getType(self)

    def getBacktrace(self) -> "std::vector< std::string > const &":
        r"""getBacktrace(Throwable self) -> std::vector< std::string > const &"""
        return _coda_except.Throwable_getBacktrace(self)

    def backtrace(self) -> "except::Throwable &":
        r"""backtrace(Throwable self) -> Throwable"""
        return _coda_except.Throwable_backtrace(self)

    def toString(self, *args) -> "std::string":
        r"""
        toString(Throwable self) -> std::string
        toString(Throwable self, bool includeBacktrace) -> std::string
        """
        return _coda_except.Throwable_toString(self, *args)

    def what(self) -> "char const *":
        r"""what(Throwable self) -> char const *"""
        return _coda_except.Throwable_what(self)

# Register Throwable in _coda_except:
_coda_except.Throwable_swigregister(Throwable)

class Exception(Throwable):
    r"""Proxy of C++ except::Exception class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_Exception

    def __init__(self, *args):
        r"""
        __init__(Exception self) -> Exception
        __init__(Exception self, Context c) -> Exception
        __init__(Exception self, Throwable t, Context c) -> Exception
        __init__(Exception self, std::string const & message) -> Exception
        """
        _coda_except.Exception_swiginit(self, _coda_except.new_Exception(*args))

    def getType(self) -> "std::string":
        r"""getType(Exception self) -> std::string"""
        return _coda_except.Exception_getType(self)

# Register Exception in _coda_except:
_coda_except.Exception_swigregister(Exception)

class IOException(Exception):
    r"""Proxy of C++ except::IOException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_IOException

    def __init__(self, *args):
        r"""
        __init__(IOException self) -> IOException
        __init__(IOException self, IOException arg2) -> IOException
        __init__(IOException self, IOException arg2) -> IOException
        __init__(IOException self, Context c) -> IOException
        __init__(IOException self, std::string const & msg) -> IOException
        __init__(IOException self, Throwable t, Context c) -> IOException
        """
        _coda_except.IOException_swiginit(self, _coda_except.new_IOException(*args))

    def getType(self) -> "std::string":
        r"""getType(IOException self) -> std::string"""
        return _coda_except.IOException_getType(self)

# Register IOException in _coda_except:
_coda_except.IOException_swigregister(IOException)

class FileNotFoundException(IOException):
    r"""Proxy of C++ except::FileNotFoundException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_FileNotFoundException

    def __init__(self, *args):
        r"""
        __init__(FileNotFoundException self) -> FileNotFoundException
        __init__(FileNotFoundException self, FileNotFoundException arg2) -> FileNotFoundException
        __init__(FileNotFoundException self, FileNotFoundException arg2) -> FileNotFoundException
        __init__(FileNotFoundException self, Context c) -> FileNotFoundException
        __init__(FileNotFoundException self, std::string const & msg) -> FileNotFoundException
        __init__(FileNotFoundException self, Throwable t, Context c) -> FileNotFoundException
        """
        _coda_except.FileNotFoundException_swiginit(self, _coda_except.new_FileNotFoundException(*args))

    def getType(self) -> "std::string":
        r"""getType(FileNotFoundException self) -> std::string"""
        return _coda_except.FileNotFoundException_getType(self)

# Register FileNotFoundException in _coda_except:
_coda_except.FileNotFoundException_swigregister(FileNotFoundException)

class BadCastException(Exception):
    r"""Proxy of C++ except::BadCastException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_BadCastException

    def __init__(self, *args):
        r"""
        __init__(BadCastException self) -> BadCastException
        __init__(BadCastException self, BadCastException arg2) -> BadCastException
        __init__(BadCastException self, BadCastException arg2) -> BadCastException
        __init__(BadCastException self, Context c) -> BadCastException
        __init__(BadCastException self, std::string const & msg) -> BadCastException
        __init__(BadCastException self, Throwable t, Context c) -> BadCastException
        """
        _coda_except.BadCastException_swiginit(self, _coda_except.new_BadCastException(*args))

    def getType(self) -> "std::string":
        r"""getType(BadCastException self) -> std::string"""
        return _coda_except.BadCastException_getType(self)

# Register BadCastException in _coda_except:
_coda_except.BadCastException_swigregister(BadCastException)

class InvalidFormatException(Exception):
    r"""Proxy of C++ except::InvalidFormatException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_InvalidFormatException

    def __init__(self, *args):
        r"""
        __init__(InvalidFormatException self) -> InvalidFormatException
        __init__(InvalidFormatException self, InvalidFormatException arg2) -> InvalidFormatException
        __init__(InvalidFormatException self, InvalidFormatException arg2) -> InvalidFormatException
        __init__(InvalidFormatException self, Context c) -> InvalidFormatException
        __init__(InvalidFormatException self, std::string const & msg) -> InvalidFormatException
        __init__(InvalidFormatException self, Throwable t, Context c) -> InvalidFormatException
        """
        _coda_except.InvalidFormatException_swiginit(self, _coda_except.new_InvalidFormatException(*args))

    def getType(self) -> "std::string":
        r"""getType(InvalidFormatException self) -> std::string"""
        return _coda_except.InvalidFormatException_getType(self)

# Register InvalidFormatException in _coda_except:
_coda_except.InvalidFormatException_swigregister(InvalidFormatException)

class IndexOutOfRangeException(Exception):
    r"""Proxy of C++ except::IndexOutOfRangeException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_IndexOutOfRangeException

    def __init__(self, *args):
        r"""
        __init__(IndexOutOfRangeException self) -> IndexOutOfRangeException
        __init__(IndexOutOfRangeException self, IndexOutOfRangeException arg2) -> IndexOutOfRangeException
        __init__(IndexOutOfRangeException self, IndexOutOfRangeException arg2) -> IndexOutOfRangeException
        __init__(IndexOutOfRangeException self, Context c) -> IndexOutOfRangeException
        __init__(IndexOutOfRangeException self, std::string const & msg) -> IndexOutOfRangeException
        __init__(IndexOutOfRangeException self, Throwable t, Context c) -> IndexOutOfRangeException
        """
        _coda_except.IndexOutOfRangeException_swiginit(self, _coda_except.new_IndexOutOfRangeException(*args))

    def getType(self) -> "std::string":
        r"""getType(IndexOutOfRangeException self) -> std::string"""
        return _coda_except.IndexOutOfRangeException_getType(self)

# Register IndexOutOfRangeException in _coda_except:
_coda_except.IndexOutOfRangeException_swigregister(IndexOutOfRangeException)

class OutOfMemoryException(Exception):
    r"""Proxy of C++ except::OutOfMemoryException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_OutOfMemoryException

    def __init__(self, *args):
        r"""
        __init__(OutOfMemoryException self) -> OutOfMemoryException
        __init__(OutOfMemoryException self, OutOfMemoryException arg2) -> OutOfMemoryException
        __init__(OutOfMemoryException self, OutOfMemoryException arg2) -> OutOfMemoryException
        __init__(OutOfMemoryException self, Context c) -> OutOfMemoryException
        __init__(OutOfMemoryException self, std::string const & msg) -> OutOfMemoryException
        __init__(OutOfMemoryException self, Throwable t, Context c) -> OutOfMemoryException
        """
        _coda_except.OutOfMemoryException_swiginit(self, _coda_except.new_OutOfMemoryException(*args))

    def getType(self) -> "std::string":
        r"""getType(OutOfMemoryException self) -> std::string"""
        return _coda_except.OutOfMemoryException_getType(self)

# Register OutOfMemoryException in _coda_except:
_coda_except.OutOfMemoryException_swigregister(OutOfMemoryException)

class NullPointerReferenceException(Exception):
    r"""Proxy of C++ except::NullPointerReferenceException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_NullPointerReferenceException

    def __init__(self, *args):
        r"""
        __init__(NullPointerReferenceException self) -> NullPointerReferenceException
        __init__(NullPointerReferenceException self, NullPointerReferenceException arg2) -> NullPointerReferenceException
        __init__(NullPointerReferenceException self, NullPointerReferenceException arg2) -> NullPointerReferenceException
        __init__(NullPointerReferenceException self, Context c) -> NullPointerReferenceException
        __init__(NullPointerReferenceException self, std::string const & msg) -> NullPointerReferenceException
        __init__(NullPointerReferenceException self, Throwable t, Context c) -> NullPointerReferenceException
        """
        _coda_except.NullPointerReferenceException_swiginit(self, _coda_except.new_NullPointerReferenceException(*args))

    def getType(self) -> "std::string":
        r"""getType(NullPointerReferenceException self) -> std::string"""
        return _coda_except.NullPointerReferenceException_getType(self)

# Register NullPointerReferenceException in _coda_except:
_coda_except.NullPointerReferenceException_swigregister(NullPointerReferenceException)

class NoSuchKeyException(Exception):
    r"""Proxy of C++ except::NoSuchKeyException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_NoSuchKeyException

    def __init__(self, *args):
        r"""
        __init__(NoSuchKeyException self) -> NoSuchKeyException
        __init__(NoSuchKeyException self, NoSuchKeyException arg2) -> NoSuchKeyException
        __init__(NoSuchKeyException self, NoSuchKeyException arg2) -> NoSuchKeyException
        __init__(NoSuchKeyException self, Context c) -> NoSuchKeyException
        __init__(NoSuchKeyException self, std::string const & msg) -> NoSuchKeyException
        __init__(NoSuchKeyException self, Throwable t, Context c) -> NoSuchKeyException
        """
        _coda_except.NoSuchKeyException_swiginit(self, _coda_except.new_NoSuchKeyException(*args))

    def getType(self) -> "std::string":
        r"""getType(NoSuchKeyException self) -> std::string"""
        return _coda_except.NoSuchKeyException_getType(self)

# Register NoSuchKeyException in _coda_except:
_coda_except.NoSuchKeyException_swigregister(NoSuchKeyException)

class NoSuchReferenceException(Exception):
    r"""Proxy of C++ except::NoSuchReferenceException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_NoSuchReferenceException

    def __init__(self, *args):
        r"""
        __init__(NoSuchReferenceException self) -> NoSuchReferenceException
        __init__(NoSuchReferenceException self, NoSuchReferenceException arg2) -> NoSuchReferenceException
        __init__(NoSuchReferenceException self, NoSuchReferenceException arg2) -> NoSuchReferenceException
        __init__(NoSuchReferenceException self, Context c) -> NoSuchReferenceException
        __init__(NoSuchReferenceException self, std::string const & msg) -> NoSuchReferenceException
        __init__(NoSuchReferenceException self, Throwable t, Context c) -> NoSuchReferenceException
        """
        _coda_except.NoSuchReferenceException_swiginit(self, _coda_except.new_NoSuchReferenceException(*args))

    def getType(self) -> "std::string":
        r"""getType(NoSuchReferenceException self) -> std::string"""
        return _coda_except.NoSuchReferenceException_getType(self)

# Register NoSuchReferenceException in _coda_except:
_coda_except.NoSuchReferenceException_swigregister(NoSuchReferenceException)

class KeyAlreadyExistsException(Exception):
    r"""Proxy of C++ except::KeyAlreadyExistsException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_KeyAlreadyExistsException

    def __init__(self, *args):
        r"""
        __init__(KeyAlreadyExistsException self) -> KeyAlreadyExistsException
        __init__(KeyAlreadyExistsException self, KeyAlreadyExistsException arg2) -> KeyAlreadyExistsException
        __init__(KeyAlreadyExistsException self, KeyAlreadyExistsException arg2) -> KeyAlreadyExistsException
        __init__(KeyAlreadyExistsException self, Context c) -> KeyAlreadyExistsException
        __init__(KeyAlreadyExistsException self, std::string const & msg) -> KeyAlreadyExistsException
        __init__(KeyAlreadyExistsException self, Throwable t, Context c) -> KeyAlreadyExistsException
        """
        _coda_except.KeyAlreadyExistsException_swiginit(self, _coda_except.new_KeyAlreadyExistsException(*args))

    def getType(self) -> "std::string":
        r"""getType(KeyAlreadyExistsException self) -> std::string"""
        return _coda_except.KeyAlreadyExistsException_getType(self)

# Register KeyAlreadyExistsException in _coda_except:
_coda_except.KeyAlreadyExistsException_swigregister(KeyAlreadyExistsException)

class NotImplementedException(Exception):
    r"""Proxy of C++ except::NotImplementedException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_NotImplementedException

    def __init__(self, *args):
        r"""
        __init__(NotImplementedException self) -> NotImplementedException
        __init__(NotImplementedException self, NotImplementedException arg2) -> NotImplementedException
        __init__(NotImplementedException self, NotImplementedException arg2) -> NotImplementedException
        __init__(NotImplementedException self, Context c) -> NotImplementedException
        __init__(NotImplementedException self, std::string const & msg) -> NotImplementedException
        __init__(NotImplementedException self, Throwable t, Context c) -> NotImplementedException
        """
        _coda_except.NotImplementedException_swiginit(self, _coda_except.new_NotImplementedException(*args))

    def getType(self) -> "std::string":
        r"""getType(NotImplementedException self) -> std::string"""
        return _coda_except.NotImplementedException_getType(self)

# Register NotImplementedException in _coda_except:
_coda_except.NotImplementedException_swigregister(NotImplementedException)

class InvalidArgumentException(Exception):
    r"""Proxy of C++ except::InvalidArgumentException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_InvalidArgumentException

    def __init__(self, *args):
        r"""
        __init__(InvalidArgumentException self) -> InvalidArgumentException
        __init__(InvalidArgumentException self, InvalidArgumentException arg2) -> InvalidArgumentException
        __init__(InvalidArgumentException self, InvalidArgumentException arg2) -> InvalidArgumentException
        __init__(InvalidArgumentException self, Context c) -> InvalidArgumentException
        __init__(InvalidArgumentException self, std::string const & msg) -> InvalidArgumentException
        __init__(InvalidArgumentException self, Throwable t, Context c) -> InvalidArgumentException
        """
        _coda_except.InvalidArgumentException_swiginit(self, _coda_except.new_InvalidArgumentException(*args))

    def getType(self) -> "std::string":
        r"""getType(InvalidArgumentException self) -> std::string"""
        return _coda_except.InvalidArgumentException_getType(self)

# Register InvalidArgumentException in _coda_except:
_coda_except.InvalidArgumentException_swigregister(InvalidArgumentException)

class SerializationException(IOException):
    r"""Proxy of C++ except::SerializationException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_SerializationException

    def __init__(self, *args):
        r"""
        __init__(SerializationException self) -> SerializationException
        __init__(SerializationException self, SerializationException arg2) -> SerializationException
        __init__(SerializationException self, SerializationException arg2) -> SerializationException
        __init__(SerializationException self, Context c) -> SerializationException
        __init__(SerializationException self, std::string const & msg) -> SerializationException
        __init__(SerializationException self, Throwable t, Context c) -> SerializationException
        """
        _coda_except.SerializationException_swiginit(self, _coda_except.new_SerializationException(*args))

    def getType(self) -> "std::string":
        r"""getType(SerializationException self) -> std::string"""
        return _coda_except.SerializationException_getType(self)

# Register SerializationException in _coda_except:
_coda_except.SerializationException_swigregister(SerializationException)

class ParseException(IOException):
    r"""Proxy of C++ except::ParseException class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_except.delete_ParseException

    def __init__(self, *args):
        r"""
        __init__(ParseException self) -> ParseException
        __init__(ParseException self, ParseException arg2) -> ParseException
        __init__(ParseException self, ParseException arg2) -> ParseException
        __init__(ParseException self, Context c) -> ParseException
        __init__(ParseException self, std::string const & msg) -> ParseException
        __init__(ParseException self, Throwable t, Context c) -> ParseException
        """
        _coda_except.ParseException_swiginit(self, _coda_except.new_ParseException(*args))

    def getType(self) -> "std::string":
        r"""getType(ParseException self) -> std::string"""
        return _coda_except.ParseException_getType(self)

# Register ParseException in _coda_except:
_coda_except.ParseException_swigregister(ParseException)



