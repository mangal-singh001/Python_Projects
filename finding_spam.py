def is_spam(comment):
    spam_keywords = ["make a lot of money","buy now","subscribe this","click this"]
    for keyword in spam_keywords:
        if keyword.lower() in comment.lower():
            return True
    return False

comments = [
    "I make a lot of money from this",
    "you buy now car",
    "You are beautiful",
    "Please! subscribe this",
    "click this man",
    "You are awesome"
]

for idx,comment in enumerate(comments):
    if is_spam(comment):
        print(f"Comment {idx+1} : Spam detected")
    else:
        print(f"Comment {idx+1} : Spam not detected")