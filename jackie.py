s = "Hello Jackie. How are you? That's good!"

s = s.replace('?', '.')
s = s.replace('!', '.')
print(s)

first_s_index = s.find('.')
first_sentence = s[0:first_s_index]
rest = s[first_s_index+2:len(s)]
print("rest is: " + rest)

second_s_index = rest.find('.')
second_sentence = rest[0:second_s_index]
third_sentence = rest[second_s_index + 2:len(rest)-1]

print(first_sentence)
print(second_sentence)
print(third_sentence)
