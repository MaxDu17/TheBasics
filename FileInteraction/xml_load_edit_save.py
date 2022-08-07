# taken from https://docs.python.org/3/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
import os

tree = ET.parse('samples/sample.xml')

# you can also get XML from a string. Same as ET.XML()
# tree = ET.fromstring('''
#  <country name="Liechtenstein">
#         <rank>1</rank>
#         <year>2008</year>
#         <gdppc>141100</gdppc>
#         <neighbor name="Austria" direction="E"/>
#         <neighbor name="Switzerland" direction="W"/>
#     </country>''')

root = tree.getroot()

######### READING #######
print(root.tag)
print(root.attrib) #attrib is found in the <> of the header
# print(root.text) #doesn't work, because it is not a leaf node
ET.dump(root) #print raw XML as a string. FOR DEBUGGING ONLY

for child in root:
    print(child.tag, child.attrib)

print(root[0][1].text) #you can also index things

# .iter() iterates every single child and children of children, etc
for neighbor in root.iter("neighbor"):
    print(neighbor.attrib)

# .findall() only looks at direct children
for country in root.findall("country"):
    rank = country.find("rank").text #firs child with this tag
    name = country.get("name") # get particular attribute
    print(name, rank)

########## EDITING #########
# set attributes and values
for neighbor in root.iter("year"):
    neighbor.set("seen", "yes") # adds another attribute
    neighbor.text = str(-1000) #set the text (exists, because it's innermost)
    a = ET.Element('a')
    neighbor.append(a) # adds the child right in the year
# remove elements
for country in root.findall("country"):
    rank = country.find("rank").text #firs child with this tag
    if int(rank) > 50:
        root.remove(country)  # remove all countries whose rank is greater than 50

tree.write("output.xml")


a = ET.Element('a')
b = ET.SubElement(a, "b", attrib = {"bob" : str(2)})
c = ET.SubElement(a, "c")
c.text = "Red Fred"
d = ET.SubElement(c, "d")

ET.indent(a) # applies pretty formatting
ET.dump(a) # prints a pretty version, DEBUGGING ONLY
print(ET.tostring(a)) #this is the flattened version in string form
# remember: to save the file, use the write() feature, not the tostring()

input("press enter to remove the added xml file")

os.remove("output.xml")
