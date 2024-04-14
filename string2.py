#String is immutable and list is mutable
#Example-
ls = [10, 20, 30, 40, 50, 60, 'Helloo', 'Vijay', 44.525, (2+5j)]
ls[4] = 5000
print(ls)
#Output => [10, 20, 30, 40, 5000, 60, 'Helloo', 'Vijay', 44.525, (2+5j)]
st1 = "AdyCoool is Using This Code"
st1[8]="$"
print(st1)
#Give error => TypeError: 'str' object does not support item assignment
