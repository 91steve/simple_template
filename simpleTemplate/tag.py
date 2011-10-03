#
# Author : Steve
# Email  : stephen91.murphy@gmail.com
# Date   : 30th September 2011

class Tag(object):
    '''This class takes a name and a value as strings on
    initialization. The tag object can then be used to search
    for tags ( <+name+> ) in strings. If a tag object matches 
    a tag ( <+name+> ) in a string, then that tag can be replaced
    with the value supplied on initialization.
    
    eg. t = Tag('greet', 'Hello world') 
    t.is_in(any_string) will match <+greet+>
    t.replace() will replace <+greet+> with 'Hello world' '''

    def __init__(self, name, value):
        '''Take the name of a tag and the value it is
        to be replaced with.'''

        #validate parameters
        self.__type_string(name)
        self.__type_string(value)
        
        #tags are case insensitive
        self.name = name.lower()
        #the value to replace the tag with
        self.value = value
        #the current string to search for the tag
        self.line = ''
        #define a tags left bracket
        self.left = '<+'
        #define a tags right bracket
        self.right = '+>'
        #the actual tag string
        self.tag =   self.left  + self.name +  self.right

    def is_in(self, search):
        '''checks to see if a string contains a tag'''
        
        #validate parameter
        self.__type_string(search)

        self.line = search

        #check for the tag in the search string
        if self.line.lower().find(self.tag) >= 0 :

            return True

        else :

            return False
        
    def replace(self):
        '''if a tag is found, replace it with a specified value.
        return the new string'''
        
        return  self.line.replace(self.tag, self. value)

    def get_name(self):
        '''Return a tags name'''
        return self.name

    def __type_string(self, var):
        '''Throws a TypeError if var is not a string'''
        string_type = type('')
        var_type = type(var)

        if string_type != var_type:
            #build an error message
            msg = "Expected type = %s, received type = %s" % (string_type , var_type)
            raise TypeError, msg
