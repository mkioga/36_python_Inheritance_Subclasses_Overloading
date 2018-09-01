

# ======================================================================
# html_doc3.py - Challenge - Composition
# ======================================================================

# At the moment, our Head() class does not create a document header with anything in it.
# Modify the program so that Head() class can include a Title tag
# HTML head section should look like ==> <head> Document Title </head>
# The text for the title will be passed to the "HtmlDoc" class "init" method when the document is created.

# We will modify the Head() class __init__ method to take title
# Then we will modify HtlmDoc() class
# Then we will provide a title when calling it in the "if __name__ == __main__ code
# NOTE our result will create test3.html on the left side


class Tag(object):

    # create constructor with option to add name and contents

    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)  # takes name and adds it in {} so result is <name> and puts in self.start_tag
        self.end_tag = '</{}>'.format(name)   # takes name and adds it in {} so result is </name> and puts in self.end_tag
        self.contents = contents              # takes contents and puts in self.contents

    # Then we add string method
    # This returns the above self in format (start_tag, content, end_tag)

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    # Now we add a function to print or display the string returned by __str__
    # MOTE: We add file=None and file=file to display method to save to file.

    def display(self, file=None):
        print(self, file=file)

# Now we will create a class for Doctype.
# NOTE that Doctype only has start_tag, No Contents and No end_tag

# <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">

class DocType(Tag):  # class DocType is a subclass of Tag i.e. it extends class Tag, hence it inherits characteristics of Tag

    def __init__(self):  # We make its constructor.
        # Use super to make it inherit Tag's constructor above "def __init__(self, name, contents)".
        # Give it name, and but contents will be blank ''
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # since name is given to both start_tag and end_tag, overide the end_tag with blank because DocType has no end_tag

    # NOTE: we used inheritance here for "DocType" to inherit "Tag" class characteristics
    # although we are dealing with composition, you should know that inheritance and composition are not mutually exclusive.
    # we can create a class hierarchy using inheritance and then use those classes in a composition relationship to build up another class
    # When using composition, you have to have some classes to compose a class out of.

    # Our HTML document class will be composed of a DTD, Header and Body
    # So at the moment we are creating those classes

    # We will start using "Composition" when we create our HTML Doc Class


# Now we will create the "Head" Class

class Head(Tag):  # Head class will inherit from Tag class

    # We create constructor for Head class
    # it inherits init from Tag class (using super) and we pass it name of 'head'
    # Although header has content above, right now we will leave content blank using ''
    # we will add content later.

    # NOTE: we modify init to take title

    def __init__(self, title=None):           # Add title here and give it default value None
        super().__init__('head', '')
        if title:                                   # Test if title exist (not None) then run below code.
            self._title_tag = Tag('title', title)   # Add this _title_tag and give it parameters shown
            self.contents = str(self._title_tag)    # contents are then converted to string.


# Now we will add the Body class

class Body(Tag):

    def __init__(self):
        super().__init__('body', '')   # NOTE: body contents will be built up separately
        self._body_contents = []  # Currently we give body_contents an empty list

    # Now we make a method to add the tag to Body
    # "self._body_contents" is currenty empty. So add_tag takes parameters name and contents is passed to it.
    # then it creates new_tag using class Tag, passing it name and contents.
    # new_tag will use Class Tag to create tags like ==> <name> contents </name>
    # Then new_tag will be appended to self._body_contents (which is initially empty)

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)


    # Now we will make the display method
    # NOTE: We add file=None on this display to

    def display(self, file=None):  # NOTE: This display under Body class overides display method under Tag superclass

        # It builds up the contents attribute by iterating through the self._body_contents list
        # And adding each tag to the contents.

        for tag in self._body_contents:  # if there is a tag in self._body_contents
            self.contents += str(tag)

        # Once that is done, it uses the superclass display method to display the body tag with the full contents.
        # NOTE: Here we put arguments file=file to save output in file

        super().display(file=file)

# if we are going to fully implement the header, we could give our Head class the same ability to add Tags and build up its contents.
# We may create a special kind of Tag class that can contain other Tags and then have both Head and Body inherit from them
# But we are keeping things simple here.
# At this point we have all the classes that make up our html document and we can create the document class.


class HtmlDoc(object):

    # This constructor/init method defines three data attributes to hold the
    # DocType, Head and Body of a html document.
    # So our HtmlDoc Class is made up of Instances of the other three classes (DocType, Head and Body)
    # So HtmlDoc is composed of the three other classes, hence that is "Composition"
    # we can also say that HtmlDoc has DocType, Has Head and Has Body, hence "Composition"
    # Since HtmlDoc contains these three classes, it can make use of attributes that these classes have

    # NOTE: we add title here, initialize it as None and then pass it to Head(title)

    def __init__(self, title=None):
        self._doc_type = DocType()  # We initialize _doc_type with DocType class
        self._head = Head(title)    # We initalize _head with Head Class. And now assign it title
        self._body = Body()         # We initialize _body with Body Class

    # We will continue with code to see how this works to produce a HTML Doc

    # We add the add_tag method which gets parameters name and contents and adds tag to HtmlDoc
    # It does this by calling "self._body.add_tag(name, contents)"
    # NOTE that "self._body = Body()" from above.
    # so "self._body.add_tag" is same as "Body.add_tag" above which appends the tags to "self._body_contents"

    # This method just delegates the job of adding a tag to its instance of the body class.
    # The body class takes care of implementing the process of adding a new tag to its contents
    # The HtmlDoc class just passes on the name and contents

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)



    # Now we will add a display method to display the HtmlDoc tags
    # Again, this display method delegates the display method to the classes that it contains.
    # NOTE: We add file=None here to all the lines below save to file.

    def display(self, file=None):
        self._doc_type.display(file=file)   # Displays DTD by calling DocType.display instance
        print('<html>', file=file)            # After DTD, we enclose everything in opening tag '<html>"
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)            # This is the closing tag '</html>"


# We will add code to run the program.
# We are creating a new HtmlDoc Object and assigning it to variable called my_page
# Then we use the add_tag method to add the headings and paragraph
# Then we call the display() to display the html structure
# We see it gives results with HTML code with Main Heading, Sub-heading and Paragraph

# NOTE: Here we will use the technique we learned in section 10 to write to file
# We will give HtmlDoc a title here. Named "HTML Doc Title"

if __name__ == '__main__':
    my_page = HtmlDoc('HTML DOC Title')   # we pass title here
    my_page.add_tag('h1', 'Main Heading')
    my_page.add_tag('h2', 'Sub-Heading')
    my_page.add_tag('P', 'Paragraph in page')
    with open('test3.html', 'w') as test_doc:
        my_page.display(file=test_doc)


# When you run this file, it will create test3.html
# Right click test3.html > Open in Browser
# It will open in browser and you will see title "HTML DOC Title" at the top
# You can also "View Source" and you will see it like this: <head><title>HTML DOC Title</title></head>

