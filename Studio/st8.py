# # in a list of numbers, print every ith number
# def print_every(i, nums):
#     counter = 0
#     for x in nums:
#
#            print(nums.index(i))
#            counter += 3
#
# print_every(3, [4, 7, 2, 10, 1, 0, 9, 6])
# # should print 4, then print 10, then print 9
def check_group(ages):
    for age in ages:
        if age < 70:
            return False
    else:
        return True

# this group should not be allowed inside the bar
group = [78, 71, 25, 84]
print(check_group(group))

# this group should also not be allowed inside the bar
group2 = [ 2, 99 ]
print(check_group(group2))

# this loner is allowed
group3 = [ 99 ]
print(check_group(group3))

# ////////////////////////////////////////////////////
def password_checker(password):

   contains_non_alpha = False

   for char in password:
        if char == " ":
            return False
        if not char.isalpha():
            contains_non_alpha = True

   return contains_non_alpha

pw1 = "i <3 makonnen"
print(password_checker(pw1))
# should print False

pw2 = "puzzlesareforfun"
print(password_checker(pw2))
# should print False

pw2 = "puzzlesr4fun"
print(password_checker(pw2))
# should print True
