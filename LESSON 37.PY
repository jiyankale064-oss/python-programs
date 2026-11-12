my_set = {'dheeraj', 'suraj', 'neeraj'}
s = list(my_set)
print(s)

['suraj', 'neeraj', 'dheeraj']


###############################################################################################


# create set
s = {'a', 'b', 'c', 'd', 'e'}

# print set
print(type(s),"",s)

# call tuple() method
# this method convert set to tuple
t = tuple(s)

# print tuple
print(type(t),"", t)

{'c', 'b', 'a','d'}
('c', 'b', 'a','d')



##########################################################################3



my_set  = {1, 3}
print(my_set)

# my_set[0]
# if you uncomment the above line
# you will get an error
# TypeError: 'set' object does not

# add an element
# Output: {1, 2, 3}
my_set. add(2)
print(my_set)




#############################################################################################3

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use union function
A.union(B)


{1, 2, 3, 4, 5, 6, 7, 8}


###################################################################################

A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}

print (A.difference(B))

{10, 20}

print (B.difference(A))

{100,60}


#############################################################################



A = {1, 5, 9, 0}
B = {2, 4, -5}

A = {1, 2, 3, 4}
B = {5, 6, 7}
C = {4, 5, 6}

print('Are A and B disjoint?', A.isdisjoint(B))
print('Are A and C disjoint?', A.isdisjoint(C))