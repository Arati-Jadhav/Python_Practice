# Solving Expressions in Python
# we will take value of a is 5 and value of b is 3 value of c is 4
a = 5
b = 3
c = 4

# 1. a2 – b2 = (a – b)(a + b)
lhs = (a**2 - b**2)
rhs = (a - b) * (a + b)
print(lhs == rhs)
# Output -> True

# 2. (a + b)2 = a2 + 2ab + b2
lhs = (a + b)**2
rhs = a**2 + 2*a*b + b**2
print(lhs == rhs)
# Output -> True

# 3. a2 + b2 = (a + b)2 – 2ab
lhs = a**2 + b**2
rhs = (a + b)**2 - 2*a*b
print(lhs == rhs)
# Output -> True

# 4. (a – b)2 = a2 – 2ab + b2
lhs = (a - b)**2
rhs = a**2 - 2*a*b + b**2
print(lhs == rhs)
# Output -> True

# 5. (a + b + c)2 = a2 + b2 + c2 + 2ab + 2bc + 2ca
lhs = (a + b + c)**2
rhs = a**2 + b**2 + c**2 + 2*a*b + 2*b*c + 2*a*c
print(lhs == rhs)
# Output -> True

# 6. (a - b - c)2 = a2 + b2 + c2 – 2ab + 2bc – 2ca
lhs = (a - b - c)**2
rhs = a**2 + b**2 + c**2 - 2*a*b + 2*b*c - 2*a*c
print(lhs == rhs)
# Output -> True


# 7. (a + b)3 = a3 + 3a2b + 3ab2 + b3
lhs = (a + b)**3
rhs = a**3 + 3*b*a**2 + 3*a*b**2 + b**3
print(lhs == rhs)
# Output -> True

# 8. (a + b)3 = a3 + b3 + 3ab(a + b)
lhs = (a + b)**3
rhs = a**3 + b**3 + 3*a*b*(a + b)
print(lhs == rhs)
# Output -> True

# 9. (a – b)3 = a3 – 3a2b + 3ab2 – b3 = a3 – b3 – 3ab(a – b)
lhs = (a - b)**3
rhs = a**3 - b**3 - 3*a*b*(a - b)
mhs = a**3 - 3*b*a**2 + 3*a*b**2 - b**3
print(lhs == rhs)
# Output -> True

# 10. a3 – b3 = (a – b)(a2 + ab + b2)
lhs = a**3 - b**3
rhs = (a - b) * (a**2 + a*b + b**2)
print(lhs == rhs)
# Output -> True

# 11.  a3 + b3 = (a + b)(a2 – ab + b2)
lhs = a**3 + b**3
rhs = (a + b) * (a**2 - a*b + b**2)
print(lhs == rhs)
# Output -> True

# 12. (a + b)4 = a4 + 4a3b + 6a2b2 + 4ab3 + b4
lhs = (a + b)**4
rhs = a**4 + 4*b*a**3 + 6*a**2*b**2 + 4*a*b**3 + b**4
print(lhs == rhs)
# Output -> True

# 13. (a – b)4 = a4 – 4a3b + 6a2b2 – 4ab3 + b4
lhs = (a - b)**4
rhs = a**4 - 4*b*a**3 + 6*a**2*b**2 - 4*a*b**3 + b**4
print(lhs == rhs)
# Output -> True

# 14. a4 – b4 = (a – b)(a + b)(a2 + b2)
lhs = a**4 - b**4
rhs = (a - b) * (a + b) * (a**2 + b**2)
print(lhs == rhs)
# Output -> True

# 15. a5 – b5 = (a – b)(a4 + a3b + a2b2 + ab3 + b4)
lhs = a**5 - b**5
rhs = (a - b) * (a**4 + b*a**3 + a**2*b**2 + a*b**3 + b**4)
print(lhs == rhs)
# Output -> True