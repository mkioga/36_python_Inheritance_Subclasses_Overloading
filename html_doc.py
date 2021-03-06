
# =======================================================
# html_doc.py - Using Composition to generate HTML code:
# =======================================================

# HTML document is a structured document that uses tags to enclose text.
# The browser uses those tags to work out how to display the text

# Search "Global Structure of html document" to see this link showing structure of html
# https://www.w3.org/TR/html401/struct/global.html

# ===============================================================

# 7.1 Introduction to the structure of an HTML document
# An HTML 4 document is composed of three parts:

# (1) a line containing HTML version information,
# (2) a declarative header section (delimited by the HEAD element),
# (3) a body, which contains the document's actual content. The body may be implemented by the BODY element or the FRAMESET element.

# White space (spaces, newlines, tabs, and comments) may appear before or after each section. Sections 2 and 3 should be delimited by the HTML element.

# Here's an example of a simple HTML document:

# <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
#   "http://www.w3.org/TR/html4/strict.dtd">
# <HTML>
#   <HEAD>
#       <TITLE>My first HTML document</TITLE>
#   </HEAD>
#   <BODY>
#       <P>Hello world!
#   </BODY>
# </HTML>

# ==============================================================

# From above structure, we can see a html document "has a" DTD (Doctype),
# "has a" header (HEAD), and "has a" BODY

# So this "has a" relationship is an indication that we should use "Composition" when making our class.

# ==============================================================

# Basic building block of html is the Tag, so we will create a "Tag" class
# For example <HTML> content </HTML> comprises the main html tag.

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

    def display(self):
        print(self)

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

    def __init__(self):
        super().__init__('head', '')


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

    def display(self):  # NOTE: This display under Body class overides display method under Tag superclass

        # It builds up the contents attribute by iterating through the self._body_contents list
        # And adding each tag to the contents.

        for tag in self._body_contents:  # if there is a tag in self._body_contents
            self.contents += str(tag)

        # Once that is done, it uses the superclass display method to display the body tag with the full contents.

        super().display()

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

    def __init__(self):
        self._doc_type = DocType()  # We initialize _doc_type with DocType class
        self._head = Head()         # We initalize _head with Head Class
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

    def display(self):
        self._doc_type.display()   # Displays DTD by calling DocType.display instance
        print('<html>')            # After DTD, we enclose everything in opening tag '<html>"
        self._head.display()
        self._body.display()
        print('</html>')            # This is the closing tag '</html>"


# We will add code to run the program.
# We are creating a new HtmlDoc Object and assigning it to variable called my_page
# Then we use the add_tag method to add the headings and paragraph
# Then we call the display() to display the html structure
# We see it gives results with HTML code with Main Heading, Sub-heading and Paragraph

if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_tag('h1', 'Main Heading')
    my_page.add_tag('h2', 'Sub-Heading')
    my_page.add_tag('P', 'Paragraph in page')
    my_page.display()


# ======================================================================
# Instead of printing the html code here, we will save it to a file
# We will do this in html_doc2.py
# ======================================================================
