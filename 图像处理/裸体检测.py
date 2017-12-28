import nude

# pip install --upgrade nudepy

print(nude.is_nude('data/women.jpg'))

n = nude.Nude('data/women.jpg')
n.parse()
print("damita :", n.result, n.inspect())
