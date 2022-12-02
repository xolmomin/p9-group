key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

d = {' ': ' '}
i = 97
for char in key:
    if not d.get(char) and char != ' ':
        d[char] = chr(i)
        i += 1
print(''.join(d[i] for i in message))

