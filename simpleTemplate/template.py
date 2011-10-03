#
# Author : Steve
# Email  : stephen91.murphy@gmail.com
# Date   : 2nd October 2011

from tag import *

class Template(object):
    '''A class used for simple templating. Takes a string
    that should contain tags, eg <+name+> <+age+>. The
    value in these tags are used as key values for a dictionary.
    the tag is then replaced with the coresponding dictionary
    value'''

    def __init__(self, template):
        '''set up the template object'''

        #validate parameters
        self.__cmp_type(template, '')
        self.template = template

    def populate_with(self, values):
        '''Takes a dictionary of values and returns a populated
        template string'''

        #validate parameters
        comp = dict()
        self.__cmp_type(values, comp)
        
        #create a list of tags
        tags = list()

        for key, value in values.items():
            tags.append(Tag(key, value))

        #the string to be returned
        complete = self.template

        for tag in tags:

            if tag.is_in(complete):
                complete = tag.replace()

        return complete

    def __cmp_type(self, var, expected):
        '''compares type of two variables. if they do 
        not have the same type, raise TypeError'''

        got = type(var)
        want = type(expected)

        if want != got:
            #build an error message
            msg = "Expected type = %s, recieved type = %s" % (want, got)
            raise TypeError, msg
