def count_hobby_words(hobbies,word):
    count = 0
    for hobby in hobbies:
        if word in hobby.split():
            count+=1
    return count

print(count_hobby_words(["Tennis","Table Tennis"],"Tennis"))
print(count_hobby_words(["Tennis","Table Tennis"],"Tab"))
print(count_hobby_words(["Tennis","Table Tennis"],"Table"))
print(count_hobby_words(["Tennis","Table Tennis"],"tennis"))
