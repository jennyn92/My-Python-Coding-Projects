#First I will save the string requested
fox_statement = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

#I will use replace function to remove ! and replace with space

print(fox_statement.replace("!"," ")) #prints out The quick brown fox jumps over the lazy dog .

"""I will find then length of this string
    and then slice it and rename to a new string,
    then I will use this new string to reprint with upper function"""


print(len(fox_statement.replace("!"," ")))

fox_statement_2 = (fox_statement.replace("!"," "))

print(fox_statement_2)

print(fox_statement_2.upper())

#I will make a new string name for upper casted string.

fox_statement_3 = (fox_statement_2.upper())

#I will print this statement in reverse

print(fox_statement_3[::-1])
