print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # what'd that do?
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

formatter = "%r %r %r %r"
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# Here's some new strange stuff, remember type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: ", days
print "Here are the months: ", months
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

"I am 6'2\" tall."  # escape double-quote inside string
'I am 6\'2" tall.'  # escape single-quote inside string

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Escape What it does.
# \\ Backslash ()
# \' Single quote (')
# \" Double quote (")
# \a ASCII Bell (BEL)
# \b ASCII Backspace (BS)
# \f ASCII Formfeed (FF)
# \n ASCII Linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only)
# \r ASCII Carriage Return (CR)
# \t ASCII Horizontal Tab (TAB)
# \uxxxx Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v ASCII Vertical Tab (VT)
# \ooo Character with octal value ooo
# \xhh Character with hex value hh