a = '''this is a test of the
    testing system''' #this is how you make extended strings


a.upper()
a.lower()
a.strip() # removes leading white space
idx = a.find("is")
print(idx)


# string to list
a = "the quick brown fox"
words = a.split(sep = " ")
print(words)

# list to string
comma_sep = ", ".join(words)
print(comma_sep)

#f-strings
x = "bobbie"
print(f"Hello my name is {x}. {x.upper()} likes tea") # any valid python expression works
