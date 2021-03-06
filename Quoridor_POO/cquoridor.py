# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_cquoridor')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_cquoridor')
    _cquoridor = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cquoridor', [dirname(__file__)])
        except ImportError:
            import _cquoridor
            return _cquoridor
        try:
            _mod = imp.load_module('_cquoridor', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _cquoridor = swig_import_helper()
    del swig_import_helper
else:
    import _cquoridor
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _cquoridor.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _cquoridor.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _cquoridor.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _cquoridor.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _cquoridor.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _cquoridor.SwigPyIterator_equal(self, x)

    def copy(self):
        return _cquoridor.SwigPyIterator_copy(self)

    def next(self):
        return _cquoridor.SwigPyIterator_next(self)

    def __next__(self):
        return _cquoridor.SwigPyIterator___next__(self)

    def previous(self):
        return _cquoridor.SwigPyIterator_previous(self)

    def advance(self, n):
        return _cquoridor.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _cquoridor.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _cquoridor.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _cquoridor.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _cquoridor.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _cquoridor.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _cquoridor.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _cquoridor.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class Line(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Line, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Line, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cquoridor.Line_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cquoridor.Line___nonzero__(self)

    def __bool__(self):
        return _cquoridor.Line___bool__(self)

    def __len__(self):
        return _cquoridor.Line___len__(self)

    def __getslice__(self, i, j):
        return _cquoridor.Line___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cquoridor.Line___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cquoridor.Line___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cquoridor.Line___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cquoridor.Line___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cquoridor.Line___setitem__(self, *args)

    def pop(self):
        return _cquoridor.Line_pop(self)

    def append(self, x):
        return _cquoridor.Line_append(self, x)

    def empty(self):
        return _cquoridor.Line_empty(self)

    def size(self):
        return _cquoridor.Line_size(self)

    def swap(self, v):
        return _cquoridor.Line_swap(self, v)

    def begin(self):
        return _cquoridor.Line_begin(self)

    def end(self):
        return _cquoridor.Line_end(self)

    def rbegin(self):
        return _cquoridor.Line_rbegin(self)

    def rend(self):
        return _cquoridor.Line_rend(self)

    def clear(self):
        return _cquoridor.Line_clear(self)

    def get_allocator(self):
        return _cquoridor.Line_get_allocator(self)

    def pop_back(self):
        return _cquoridor.Line_pop_back(self)

    def erase(self, *args):
        return _cquoridor.Line_erase(self, *args)

    def __init__(self, *args):
        this = _cquoridor.new_Line(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _cquoridor.Line_push_back(self, x)

    def front(self):
        return _cquoridor.Line_front(self)

    def back(self):
        return _cquoridor.Line_back(self)

    def assign(self, n, x):
        return _cquoridor.Line_assign(self, n, x)

    def resize(self, *args):
        return _cquoridor.Line_resize(self, *args)

    def insert(self, *args):
        return _cquoridor.Line_insert(self, *args)

    def reserve(self, n):
        return _cquoridor.Line_reserve(self, n)

    def capacity(self):
        return _cquoridor.Line_capacity(self)
    __swig_destroy__ = _cquoridor.delete_Line
    __del__ = lambda self: None
Line_swigregister = _cquoridor.Line_swigregister
Line_swigregister(Line)

class Array(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Array, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Array, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cquoridor.Array_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cquoridor.Array___nonzero__(self)

    def __bool__(self):
        return _cquoridor.Array___bool__(self)

    def __len__(self):
        return _cquoridor.Array___len__(self)

    def __getslice__(self, i, j):
        return _cquoridor.Array___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cquoridor.Array___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cquoridor.Array___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cquoridor.Array___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cquoridor.Array___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cquoridor.Array___setitem__(self, *args)

    def pop(self):
        return _cquoridor.Array_pop(self)

    def append(self, x):
        return _cquoridor.Array_append(self, x)

    def empty(self):
        return _cquoridor.Array_empty(self)

    def size(self):
        return _cquoridor.Array_size(self)

    def swap(self, v):
        return _cquoridor.Array_swap(self, v)

    def begin(self):
        return _cquoridor.Array_begin(self)

    def end(self):
        return _cquoridor.Array_end(self)

    def rbegin(self):
        return _cquoridor.Array_rbegin(self)

    def rend(self):
        return _cquoridor.Array_rend(self)

    def clear(self):
        return _cquoridor.Array_clear(self)

    def get_allocator(self):
        return _cquoridor.Array_get_allocator(self)

    def pop_back(self):
        return _cquoridor.Array_pop_back(self)

    def erase(self, *args):
        return _cquoridor.Array_erase(self, *args)

    def __init__(self, *args):
        this = _cquoridor.new_Array(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _cquoridor.Array_push_back(self, x)

    def front(self):
        return _cquoridor.Array_front(self)

    def back(self):
        return _cquoridor.Array_back(self)

    def assign(self, n, x):
        return _cquoridor.Array_assign(self, n, x)

    def resize(self, *args):
        return _cquoridor.Array_resize(self, *args)

    def insert(self, *args):
        return _cquoridor.Array_insert(self, *args)

    def reserve(self, n):
        return _cquoridor.Array_reserve(self, n)

    def capacity(self):
        return _cquoridor.Array_capacity(self)
    __swig_destroy__ = _cquoridor.delete_Array
    __del__ = lambda self: None
Array_swigregister = _cquoridor.Array_swigregister
Array_swigregister(Array)


def BreadthFirstSearch(positionDeDepart, ligneAAtteindre, barrieresHorizontales, barrieresVerticales):
    return _cquoridor.BreadthFirstSearch(positionDeDepart, ligneAAtteindre, barrieresHorizontales, barrieresVerticales)
BreadthFirstSearch = _cquoridor.BreadthFirstSearch

def print_array(myarray):
    return _cquoridor.print_array(myarray)
print_array = _cquoridor.print_array
# This file is compatible with both classic and new-style classes.


