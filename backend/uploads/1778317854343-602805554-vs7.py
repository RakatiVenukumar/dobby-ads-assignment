letter = '''Dear <|NAME|>
you are selected!

date: <|DATE|>'''
name = input("enter your name")
date = input("enter date")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)