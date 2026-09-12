d = "DEBUG"
i = "INFO"
e = "ERROR"
w = "WARNING"
t = "TRACE"

log_levels = ["DEBUG", "INFO", "ERROR", "WARNING", "TRACE"]
print(type(log_levels)) # <class 'list'>
print(len(log_levels)) # 5


log_levels.append("TEST") # dodanie elementu do listy
print(log_levels)
log_levels.sort() # sortowanie listy
print(log_levels)

create_list = list("codebrainers") # 
print(create_list) # ['c', 'o', 'd', 'e', 'b', 'r', 'a', 'i', 'n', 'e', 'r', 's']

l1 = ["a", "b", "c"]
l2 = ["d", "e", "f"]
l3 = l1 + l2
print(l3) # ['a', 'b', 'c', 'd', 'e', 'f']

