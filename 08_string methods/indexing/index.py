# indexing = accessing elements of a sequence using [](Indexing operator)
#            [start : end : step]
# starting index : inclusive ending index : exclusive
credit_number = "1234-5667-7897-4456"

print(credit_number[4]) 
print(credit_number[0:4]) # first 4 digit
print(credit_number[5:9])
print(credit_number[5:])
print(credit_number[-1])

print(credit_number[::2])