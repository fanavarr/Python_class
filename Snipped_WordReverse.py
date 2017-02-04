
#simple snipped to reverse a string

def reverse(text):
    rev = ""
    for i in text:
        rev = i + rev
        print(rev)
    return rev
  
reverse("my word")
