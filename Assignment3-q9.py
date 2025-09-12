import email
import re
email_pattern = r'[a-za-ZO-9._%+-]+@[a-za-ZO-9.-]+\.[a-z]{2,4}'
emails = re.findall(email_pattern, text)
print("email addresses found:")
for email in emails:
    print(email)






import re
def validate_date(date_string):
    pattern = r'^(?:[0-9]{4})-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12][0-9]|3[01])/?$'
    if re.match(pattern, date_string):
        return True
    else:
        return False




    import re
    text = ("Prayer is helpful. I love Prayer because Prayer is powerful.")
    word_to_replace = "Prayer"
    replacement_word = "intercession"
    new_text = re.sub(rf'\b{word_to_replace}\b', replacement_word, text')
    print("Original text:", text)
    print(text)
    print("\nModified text:")
    print(new_text))




    import re
    text = "Hello, world! Welcome to Prayer! @ OpenChurch."
    words = re.split(r'\W+', text)
    words = [word for word in words if word]
    print("Original text:")
    print(text)
    print("\nSplit words:")
    print(words)



