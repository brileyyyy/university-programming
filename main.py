import re

text = "abbbaaa bac cab cccbaabacc"
# pattern = re.compile(r'\b\w*b\w*a\w*\b')
pattern = re.compile(r'\b\w*b[a-c]a\w*\b')
# pattern = re.compile(r'b\w{1}a')

words_with_subword = pattern.findall(text)

print(words_with_subword)

text = "abbbaaa bac cab baabacc"
words = text.split(' ')

result = []
for i in range(len(words)):
	if re.findall(r'b\w?a', words[i]) != []:
		result.append(words[i])

for res in result:
    print(res)