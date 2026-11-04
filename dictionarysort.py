d = {"banana": 3, "apple": 4, "cherry": 1}
sorted_key=dict(sorted(d.items()))
reverse_key=dict(sorted(d.items(),reverse=True))

print(sorted_key)
print(reverse_key)
