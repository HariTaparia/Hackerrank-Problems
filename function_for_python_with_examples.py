Variable uses by type and meaning
type <string> = a,b,s           a = "Well, Shankar always have a story to tell!"
type <int> = i,j,k,l,m,n,num
type <list> = alpha, beta, gamma

Input commands
>>>  a = input()        #it always  takes a string as an input but rest depends on you how to manupulate it
>>>  i = int(input())   #takes string as an input and converts to type <int>

String manupulation
----String Function----
>>>   alpha = a.split("*give the seperation indicator like*")
>>>   alpha = a.split(" ")
>>>   print(alpha)
>>>>>> ['Well,', 'Shankar', 'always', 'have', 'a', 'story', 'to', 'tell!'] 

----Join Function----
>>>b = "*join list elements by*".join(*list name*)
>>>b = "-".join(alpha)
>>>print(b,"---------",type(b))
>>>>>> Well,-Shankar-always-have-a-story-to-tell! --------- <class 'str'>

----any function----
>>>print (any(i.isupper() for i in s))          #Boolean output type function with considering union

----bool_type_identifiers----
>>>a.isalnum()          #alpha(alphabet)-numeric boolean type identifier
>>>a.isalpha()          #alpha boolean based identifier
>>>a.isdigit()          #numeric boolean type identifier
>>>a.islower()          #lower case idenifier boolean function
>>>a.isupper()          #upper case identiifer boolean function

----rjust,ljust,center function-----
>>>a.rjust(width,'*space element*') same with ljust and center rjust for right alignment and similarly
>>>a = 'H'
>>>print((a*5).center(24,'a'))
>>>>>>aaaaaaaaaHHHHHaaaaaaaaaa

----textwrap-----
>>> import textwrap
>>> wrapped_text = textwrap.wrap(*string_name*,*wrap_width*)
>>>>>>wrapped text
