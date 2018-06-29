

# dump out an objects attributes
# ignore builtins and methods
def dump(obj):
    def ignore(attrib):
        if attrib[0:2] == '__':
            return False
        else:
            return attrib
    print('\n')
    for attr in filter(ignore, dir(obj)):
        if hasattr( obj, attr ) and  not (attr[0:2] == '__' or callable(getattr(obj, attr))):
            print( "obj.%s = %s %s" % (attr, getattr(obj, attr), callable(getattr(obj, attr))))

