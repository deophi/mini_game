a = [23, 76, 45, 20, 70, 65, 15, 54]
indexMin = 0
indexMax = 0
index = 1
while index < len(a):
    if a[index] < a[indexMin]:
        indexMin = index
    if a[index] > a[indexMax]:
        indexMax = index

    index += 1

print("Lowest value ", indexMin,":", a[indexMin])
print("Highest value:", indexMax,":", a[indexMax])