# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list1 = [1, 2, 3, 2, 1]
copy1 = list1.copy()
copy1.reverse()

if (list1 == copy1):
    print("List is a palindrome.")

else: 
    print("List is not a palindrome.")

list2 = [1, "abc", "abc", 1]
copy2 = list2.copy()
copy2.reverse()

if (list2 == copy2):
    print("List is a palindrome.")

else: 
    print("List is not a palindrome.")