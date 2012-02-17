# -*- coding: iso-8859-1 -*-
# -*- mode: python -*-
"""
load comparison methods from the entry points.

Copyright (C) 2011 Daniel Meliza <dan // meliza.org>
Created 2011-08-30
"""
from pkg_resources import iter_entry_points

entry_point_name = "chirp.compare.method"

def names():
    """ Return list of available comparison methods """
    return [ep.name.lower() for ep in iter_entry_points(entry_point_name)]

def load(name):
    """ Load the entry point associated with a method, or ImportError if it doesn't exist """
    for ep in iter_entry_points(entry_point_name):
        if ep.name.lower() == name.lower():
            return ep.load()
    raise ImportError, "No entry point for %s in group %s" % (name.lower(), entry_point_name)

def make_scriptdoc():
    out = "Available methods:"
    for ep in iter_entry_points(entry_point_name):
        obj = ep.load()
        out += "\n%15s    %s" % (obj.__name__, obj._descr)
    return out

# Variables:
# End:
