string = 'b22%2mZUk$hv3^b^3s85Q#'
newstring = ''
for i in string:
    if i.isalpha():
        newstring += '1'
    elif i.isdigit():
        newstring += '2'
    else:
        newstring += '3'
print(newstring)
