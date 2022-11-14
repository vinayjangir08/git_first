
# coding: utf-8

# ## Data Types: 
# 
# * Integer (int) -- contains values like 0, 1, 3 ... 9999 and does not contains the values with decimal points.
# * Float (float) -- contains values which have decimal point within it.
# * Boolean  -- contains only two values True and False where True = 1 and False = 0
# * String -- contains values which are in the form of words and characters. e.g. 'a', 'P', 'java', 'Python'. Every character has seperate ascii value whether its capital letter or small letter, the ascii value for both is different. 
# * None -- when no value is mentioned its data type is none. Empty variable have none data type. 
# * Complex -- its the combination of real+imaginery number.

# In[1]:


a = 10
b = 2999


# In[2]:


z = -1
type(z)


# In[3]:


type(b)


# In[4]:


c = 195.28679
type(c)


# In[5]:


d = -15.26
type(d)


# In[6]:


pi = 22/7
pi


# In[7]:


round(pi,4)   ## round as inbuilt function 


# In[8]:


True # def 1


# In[9]:


False # def 0


# In[10]:


True + True # 1+1


# In[11]:


True + False # 1+0


# In[12]:


False + False # 0+0


# In[13]:


n = 'Python'
type(n)


# In[14]:


m = 'c'
type(m)


# In[15]:


type(True)


# In[16]:


w = 10 + 9j  # def j/J is alloted for mentioning the imaginery numbers in python
type(w)


# In[17]:


temp = None
temp


# In[18]:


temp = 7896543
temp


# ## Error Types:
# 
# * Key Error -- when the element/values are not available in DS, then it will show key error.
# * Attribute Error -- when the attribute/method/operations is not available on that particular DS then it shows attribute error.
# * Type Error -- this error will occur when perform wrong operation(methods) on DS which are not availabel for that particular typr of DS.
# * Syntax Error -- This error will occur when wrong syntax is written in code.
# 

# ## Rules to Define Variables:
# 
# * Variable name should never start with numbers, rather it can start with alphabets, underscore
# * It can be combination of numbers and alphabets i.e. alphanumeric with only special char i.e. underscore( _ )
# * It is recommended to use meaningful variable.
# * There is no limit to declare variable length.
# * We cannot use keywords as variable name.
# * Python is case sensitive lang, hence accordingly we should define variable name.

# ## Types of Cases for Writing Variable Name:
# 
# * Pascal Case - where first letter of every word is always capital -- eg. ProdId, PhonePay, GeoArea
# 
# 
# * Snake case - where two words are connected to make variable with underscore -- eg. prod_id, market_sale, stud_data
# 
# 
# * Camal case - where first letter of first word is small and other word's first letters are capital -- eg. prodId, marketData, marketDATA
# 
# 
# * Kebab case - where two words are connected with hyphen (-) instead underscore ( _ ). THis case is not supported in jupyter, pycharm and google colab ide -- eg. pune-tcs-emp-id or pune_tcs_emp_id

# ## Data Structures (DS) :
# 
# * List -- Defined in [] bracket. It is the collection of all data types and DS(eg. list, tuple, set, dict). It is mutable type of DS. It is an ordered type DS, hence indexing can be performed.
# Homogeneous and Heterogeneous are the types
# Lists are one of 4 built-in data types in Python used to store collections of data in which all the other DS can be stored as elements (eg. tuple (1, 1, 2), set {1, 2}, dictionary {key:value}) 
# for example list_1= [0, 22, 15.62, 'Java', (1, 1, 2),{name:'Python'}, {1, 2}, [1, 2, 3] ]
# 
# * Tuple -- Defined in () bracket. It is the collection of all the data types and DS(eg. list, tuple, dict, set). It is immutable and ordered type DS, in which indexing can be performed.
# p1 = ({'1':2},'java',[78], (1, 2, 2),{1, 2, 3})
# 
# 
# * Dictionary -- It is defined in {} brackets. The items in dictionary are in the form of Key:Value pairs. In dictionary Keys are immutable (keys are generally strings or int) and Values are mutable. Dictionaries are unordered type DS.
# dict = {'name':python, 'ide':jupyter, 33:'integer'}
# 
# 
# * Set -- Defined in {} barckets. These are the mutable and unordered type of DS. Set contains only unique values. Duplication of elements in the lists can be removed using set type DS (by using typecasting). In set Minimun 1 element is required.
# list_2 = [1, 1, 2, 3, 4, 5]
# set(list_2) = {1,2,3,4,5}
# 
# 
# * String -- Strings are the collection characters where there is no indexing.
# 
# 
# * Frozenset -- 
# 
# 
# ### DS are of two Types/ Property :
# * Mutable -- are the data structures in which elements can be added or sutracted and various operations can be performed.
# * Immutable -- are the data structures in which elements can not be added or removed. 

# In[19]:


t1 = (1, 2, 3, 4, 2, 3, {'name':'python', 33:'integer'})
t1


# In[20]:


t1[-1]


# In[21]:


p1 = {12, 45, 8, 'python', 'Python', 'java', 'v', 't', 100.23}  #-- its not a list 


# In[22]:


p1  ## set obeject


# In[23]:


p1[2]


# In[ ]:


p = ['AI', 'ML', 'Java', 'Python', 'R', 'C', 'C++']
p


# In[ ]:


p[3]


# In[24]:


p.index('R')


# ## 1. List --> []
# 
# * It is a mutable DS.
# * Elements can be added/remove/updated.
# * Following generalized methods can be performed on list: 
#    * append
#    * extend
#    * insert
#    * remove
#    * pop
#    * clear
#    * copy
#    * count 
#    * index
#    * reverse
#    * sort 
#    * mro 
#    * len - inbuilt (function)
#  

# In[25]:


list_f = [11, 12, 36, 49, 59, 48, 8995, 49, 69]
list_s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[26]:


list_f.append(list_s)
print(list_f)


# In[27]:


list_f[-1] # index


# In[28]:


list_f.pop()


# In[29]:


print(list_f)


# In[30]:


list_f.extend(list_s)
list_f


# In[31]:


list_f[-1]


# In[32]:


list_f.clear()
list_f


# In[33]:


list_f.insert(0, 25)
list_f


# In[34]:


list_s.sort()


# In[35]:


list_s


# In[36]:


list_s.reverse()


# In[37]:


list_s


# In[38]:


list_new = list_s.copy()
list_new


# In[39]:


list_fn = [11, 12, 36, 49, 59, 48, 8995, 49, 69]
list_fn.count(49)


# In[40]:


list_fn.remove(8995)
list_fn


# In[41]:


list_fn.pop()


# In[42]:


list_fn


# In[43]:


list_fn.pop(2)
list_fn


# ## Tuples:  --> ()
# 
# * It is collection of elements.
# * Immutable DS --> we can't add/remove/update the existing file.
# * Its an ordered data type.
# * Tuples are faster than lists.
# * It can contain duplicate elements.
# * It is used to store infrequent data sets to avoid accidental changes in dataset.
# * Following are the generalized methods:
#     * count
#     * index
#     * mro

# In[44]:


t = (100, 2, 3, 4, 2, 2, 3, 5, 1, 2, 3)


# In[45]:


t.count(1)


# In[46]:


type(t)


# In[47]:


t[5]


# In[48]:


t[-1]


# In[49]:


t[0]


# In[50]:


t1 = ('Java_')
t2= ('Python')

tf = t1 + t2
print(tf)


# In[51]:


t3 = (500)
t4 = (200)

tff = t3 - t4
print(tff)


# In[52]:


t5 = (500, 566)
t6 = (200, 35)

tfft = t5 - t6
print(tff)


# ## Order of elements: (ASCII Value)
# 
# * A to Z --> 65 to 90
# * a to z --> 97 to 122
# * 0 to 9 --> 48 to 57
# 

# In[53]:


c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


# In[54]:


ord('A')


# In[55]:


ord('Z')


# In[56]:


ord('a')


# In[57]:


ord('z')


# In[58]:


ord('0')


# In[59]:


ord('9')


# In[60]:


p = {55, 102, 'a', 'g', 'L', 'D', 'Aakash', 'John', 'roshan'}
p


# In[61]:


ord('!')


# In[62]:


ord('@')


# ## 3.  Sets: --> {}
# 
# * Collections of different types.
# * It is unordered type DS.
# * We can't perform indexing on sets. 
# * It is mutable type dataset.
# * It is collection of unique elements, hence removes duplication.
# * At least one element is required in set type DS.
# * It is used for perform general operations:
#     * add -- adds single element ()
#     * update -- adds multiple elements ({ ---})
#     * remove -- deletes element if present, otherwise shows key error
#     * discard -- deletes element if present, otherwise do nothing
#     * pop -- randomely deletes elements, by default first element
#     * clear -- 
#     * copy
#     * difference
#     * difference_update
#     * intersection --
#     * intesection_update
#     * union
#     * count
#     * symmetric_difference
#     * symmetric_difference_update
#     * isdisjoint
#     * issubset
#     * issuperset
#     * mro
#  
#     

# #### Set Operations:
# 
# * union -- all the elements in both sets
# * intersection -- similar elements in both sets
# * symmetric_difference -- negation of intersection is symmetric difference
# * difference -- gives the difference of both the lists
# * superset -- if all members of b are present in a -- a is superset of b
# * subset -- if all members of b are present in b -- b is subset of a
# * disjoint -- a.isdisjoint(c) -- no element of c is present in a
# 

# to save the variables in other variable we can use updates
# 
# loan_k.intersection_update(credit_k) -- will get updated in loan_k
# -- only intesection, difference and symmetric_difference can be updated using update operations.
# 
# 
# 

# In[63]:


loan = {'john', 'Aakash', 'tanush', 'Shubham', 12, 11, 201, 56}
credit = {'Aakash', 'Shubham', 'Trisha', 56, 89, 902}


# #### As the combination of numbers and characters are there, set is getting printed as output as per order of elements i.e. ASCII Value.

# In[64]:


loan


# In[65]:


credit


# In[66]:


loan.intersection(credit)


# #### As only numbers are there in set, set is getting printed in increasing order of given numbers.

# In[67]:


t = {1, 265, 184, 85, 6, 5, 2, 26, 24, 59, 96, 3}
t2 = {100, 1100, 105, 908, 9000,200, 780, 300}


# In[68]:


t


# In[69]:


t2


# In[70]:


t2.discard(200)
t2


# In[71]:


t.add(9)
t


# In[72]:


t.update({59, 87, 63, 1009})   # it will not take 59 twice as the element is already there
t


# In[73]:


t.remove(1005)


# In[74]:


t.remove(1009)
t


# In[75]:


t.discard(1009)
t


# In[76]:


t.discard(59)
t


# In[77]:


t.pop()
t


# In[78]:


t.pop()
t


# In[79]:


t.pop(63)


# In[80]:


wer = {'Ml', 'Python', 'Java'}
wer.clear()


# In[81]:


wer


# In[82]:


ws = {56, 60.4, 1516, 184, 468, 0.5993}
ws


# In[83]:


ws.clear()


# In[84]:


print(ws)


# In[85]:


a = 20
a


# In[86]:


a = {1, 2, 3}
b = {4, 5, 6}


# In[87]:


b = a.copy()
b


# In[88]:


s = {34,756,354,64, 'ML'}
s1= s.copy()
s1


# In[89]:


loan = {'john', 'Aakash', 'tanush', 'Shubham', 12, 11, 201, 56}
credit = {'Aakash', 'Shubham', 'Trisha', 56, 89, 902}


# In[90]:


loan.difference(credit)


# In[91]:


credit.difference(loan)


# In[92]:


loan.difference_update(credit)


# In[93]:


loan


# In[94]:


credit.difference_update(loan)
credit


# In[95]:


loan = {'john', 'Aakash', 'tanush', 'Shubham', 12, 11, 201, 56}
credit = {'Aakash', 'Shubham', 'Trisha', 56, 89, 902}


# In[96]:


credit.difference_update(loan)
credit


# In[97]:


loan = {'john', 'Aakash', 'tanush', 'Shubham', 12, 11, 201, 56}
credit = {'Aakash', 'Shubham', 'Trisha', 56, 89, 902}


# In[98]:


loan.intersection_update(credit)


# In[99]:


loan


# In[100]:


credit


# In[103]:


credit.intersection_update(loan)
credit


# In[114]:


## methods exactly starting with 'is' will always reaturn outputs as Boolean values
## If two sets have at least one common element then output of "isdisjoint" is False


# In[119]:


a = {1, 2, 3, 4, 5, 6}
b = {2, 4, 6}
c = {'python', 'ml'}
d = {2, 11, 12, 'ml'}
e = {'python'}

# Here a, c are supersets of b, e respectively
# And b,e are subsets of a,c respectively


# In[106]:


a.isdisjoint(b)


# In[107]:


a.isdisjoint(c)


# In[111]:


d.isdisjoint(b)


# In[113]:


c.isdisjoint(e)


# In[115]:


b.issubset(a)


# In[116]:


a.issubset(b)


# In[117]:


a.issuperset(b)


# In[118]:


d.issubset(c)


# In[137]:


loan = {'john', 'Aakash', 'tanush', 'Shubham', 12, 11, 201, 56}
credit = {'Aakash', 'Shubham', 'Trisha', 56, 89, 902}


# In[138]:


loan.intersection(credit)


# In[136]:


loan.symmetric_difference(credit)


# In[140]:


credit.symmetric_difference(loan)


# In[141]:


loan.symmetric_difference_update(credit)


# In[142]:


loan


# In[143]:


credit


# In[144]:


loan.union(credit)


# ## 4. Dictionary -- { }
# 
# * Its is collection of items.
# * Items are defined as key value pairs.
# * It is mutable and unordered type DS.
# * Key can never be duplicate.
# * Keys are always unmutable but values are mutable.
# * There can be multiple values for single key.
# * Following are the generalized functions:
#     * clear
#     * copy
#     * fromkeys
#     * get -- used to access value by using key, if key is not present in the dict then by default is shows None/mentioned statement.
#     * items
#     * keys
#     * pop -- we will have to mention key for deleting that key value pair
#     * popitem -- ite delets last item by defalut
#     * setdefault
#     * update 
#     * values 
#     * mro

# In[145]:


d = {1:2, 3:4, 5:6}
d


# In[146]:


k = d.keys()
k


# In[147]:


v = d.values()
v


# In[148]:


d.items()


# In[149]:


d1 = d.copy()
d1


# In[150]:


d1.pop(1)
d1


# In[151]:


d1.popitem()
d1


# In[152]:


d1['lang'] = 'python'
d1


# In[153]:


d1.clear()
d1


# In[154]:


d = {'python': 'easy', 'java': 'very easy', 'java script': 'not useful'}

d.get('C++', 'Not Present')


# In[155]:


d.get('python', 'None')


# In[156]:


bride_details = {'name':['sneha','madhu'],
                'height':[5.3,5.5],
                 'color':['fair','very fair']
                }


# In[157]:


bride_details


# In[158]:


bride_details.update({'key':'value', 'city':'pune'})
bride_details


# In[159]:


dt = {'name':'xyz', 'age':20, 'sal':45000, 'city':'pune'}


# In[160]:


dt.setdefault('name', 'abc')


# In[161]:


dt.setdefault('counry','india')
dt


# In[162]:


dt['name'] = 'abc'
dt


# In[170]:


dt


# In[171]:


dt.setdefault('planet', '')
dt


# In[167]:


dt.setdefault('planet', 'Earth')
dt


# In[168]:


dt['planet'] = 'Earth'
dt


# #### Problem 1

# In[184]:


a = {1, 2, 3}


# In[185]:


temp = dict.fromkeys(a)
temp


# In[186]:


temp['1'] = 'Python'
temp['2'] = 'ML'
temp['3'] = 'Java'


# In[187]:


temp


# In[188]:


temp[1] = 'C'
temp[2] = 'C++'
temp[3] = 'Big Data'


# In[189]:


temp


# #### Problem 2

# In[173]:


m = {1, 2, 3, 4}
n = {'A', 'B', 'C', 'D'}


# In[174]:


temp_2 = dict.fromkeys(m)
temp_2


# In[175]:


for item in temp_2:
    for i in n:
        temp_2[item] = 


# In[176]:


s_1 = {'Vlad Tepes', 'Alucard', 'Trevor', 'Isaac'}
s_2 = {1, 2, 3, 4}


dictionary = dict(zip(s_1,s_2))


# In[177]:


s1 = {'Vlad Tepes', 'Alucard', 'Trevor', 'Isaac'}
s2 = {1, 2, 3, 4}


# In[179]:


a = dict(zip(s2,s1))
a


# In[180]:


##It's working 

a = {1, 2, 3}
b = {4, 5, 6}


# In[181]:


d = dict(zip(a,b))
d


# #### Problem 3

# In[7]:


z = [15, 25, 62, 58, 89, 67]
z = [0, 1, 2, 3, 4, 5]   #-- index values (index 5==(-1) i.e 67)

temp = {}
for i in z:
    if i in [z[-1]]:
        break
        
    temp[i] = z[(z.index(i))+1]   
    
# for i= 15 temp[i=0 --15] =z[0+1=1 -- index] -- z[i=1 --25]
# for i= 25 temp[i=1 --25] =z[1+1=2 -- index] -- z[i=2 --62]


# In[8]:


print(temp)


# #### Some more practice examples

# In[6]:


py_dict = {'name':'Ranbir', 'Sal':'75000','City':'Pune'}
py_dict


# In[2]:


py_dict['name']


# In[3]:


py_dict.get('name')


# In[4]:


py_dict['holidays']


# In[9]:


h = py_dict.get('holidays', 'no key present')


# In[10]:


type(h)


# In[11]:


py_dict['company'] = 'MIT-WPU'


# In[12]:


py_dict


# In[13]:


py_dict.update({'course':'Ph.D', 'duration':'3 years'})


# In[14]:


py_dict


# In[15]:


cars = {'name':['BMW', 'AUDI'], 'mil':[15, 18], 'color':['red', 'black']}
cars


# In[17]:


cars['mil'][0]


# In[18]:


cars['name'][1]


# In[24]:


cars_ver = {'ver1' :{cars = {'name':['BMW', 'AUDI'], 'mil':[15, 18], 'color':['red', 'grey']}}, 
            'ver2': {cars = {'name':['BMW', 'AUDI'], 'mil':[15, 18], 'color':['red','black']}}, 
            'ver3':{cars = {'name':['BMW', 'AUDI'], 'mil':[15, 18], 'color':['red', 'white']}}
           }


# In[25]:


cars.keys()


# In[26]:


cars.values()


# #### To delete the values from dictionary
# 
# --> pop -- to delete item using key and entire pair will get deleted
# --> popitem -- it deletes the last item from dictionary
# 

# In[27]:


k = ('name', 'id', 'sal')


# In[32]:


temp = dict.fromkeys(k)
temp


# In[34]:


temp['name'] = ['Tanush', 'Priyanka']


# In[35]:


temp['id'] = [101, 102]


# In[36]:


temp['sal'] = [1000, 90000]


# In[37]:


temp


# In[39]:


import pandas as pd
pd.DataFrame({'name': ['Tanush', 'Priyanka'], 'id': [101, 102], 'sal': [1000, 90000]})


# In[41]:


temp.setdefault('name', 'Akshay')


# In[42]:


temp.setdefault('city', 'Pune')


# In[43]:


temp


# #### in case of setdefault id already existing index is there then value wont change  -- but if the key value pair is not there then it will get added

# regex -->
# 
# python --> regex
# 
# numpy --> c language

# ## String
# 
# It is collection of characters arranged in meaningful oreder. 
# It is of immutable types. By default any input is considered as string. 
# 
# This is higher priority that given input is string. If you mention the type of input then it can get converted into particular type, otherwise treated as string.
# 
# '_'   "_"  --> this are notations for single line string
# 
# '''_'''  -->
# 
# """__"""  --> it is used for multiple line commenting and at the same time, it prints the text as it is without "_" or '_' format.. you will get plain text as usual. 
# 
# 
# if you find some part/elements of list using find function it shows its proper index and if you don't find anything then by default it shows the -1 index for that element.  

# In[1]:


a_str = input("Enter the number: ")
print(a_str)
type(a_str)


# In[2]:


w = int(input("Enter the number: "))
type(w)


# In[3]:


p = 'Python'


# In[5]:


p[0] = 'J'


# In[6]:


p.upper()


# In[7]:


q = 'HADOOP'
q.lower()


# In[8]:


a = 'admin'
username = input("Enter the username: ")


# In[10]:


a == username.lower()


# In[11]:


a == username.upper()


# In[12]:


k = 'phd entrance test'


# In[13]:


k.capitalize()


# In[14]:


k.title()


# In[15]:


k.swapcase()


# In[18]:


w = 'DJango fLasK'


# In[19]:


w.swapcase()


# In[20]:


e_id = 'priyanka.garsole.rw@gmail.com'


# In[21]:


e_id


# In[24]:


sp = e_id.split('@')
sp


# In[28]:


sp.split('.')


# In[26]:


sp[0].split('.')


# In[27]:


sp[1].split('.')


# In[29]:


p_ = 'pyspark'


# In[30]:


p_.startswith('py')


# In[31]:


p_ = 'pyspark.pdf'


# In[32]:


p_.startswith('py')


# In[35]:


p_.endswith('.pdf')


# In[36]:


p_.endswith('..pdf')


# In[37]:


email = ['priyanka@gmail.com', 'pri@yahoo.co.in', 'priki_style', 'priyanka_garsole', 'p.a.garsole@gmail.com', 'priya.gar.rw@gmail.com']


# In[38]:


email


# In[40]:


for e in email:
    if e.endswith('com'):
        print(e)


# In[41]:


for e in email:
    if e.endswith('in'):
        print(e)


# In[42]:


lang = 'python..c..cpp..java..csharp..chash..hadoop..apache.scoop..sql..web.develop'
lang


# In[43]:


lang.split('..')


# In[44]:


lang.index('apache.scoop')


# In[47]:


lang[45:57].split('.')


# In[48]:


lang.find('c')


# In[49]:


lang.find('logo')


# In[51]:


us_in = input("Enter the req string: ")

if lang.find(us_in) == -1:
    print("Not Found")
else:
    print("Found")


# In[52]:


e = 10 ; f = 56 ; g = e+f


# In[53]:


g


# In[54]:


"Addition of {} and {} is {} ".format(101, 102, 101+102)


# In[55]:


filename = 'test_date'


# In[56]:


import datetime


# In[60]:


datetime.date(2022,9, 6)


# In[61]:


filename = 'test_{}.pdf'.format(datetime.datetime.date(datetime.datetime.now()))


# In[62]:


filename


# In[69]:


'{} and {} is tremendously useful in near future'.format('Python' , 'AI-ML')


# In[72]:


x = 70
y = 75
z = 5

f"Subtraction of {y} and {x} is {z}"


# In[74]:


j = 'vrgarhrscsdwtedrrrsdsrr'


# In[76]:


j.count('r')


# In[78]:


j.count('s')


# #### Cutting the string --> whitespace

# In[79]:


username = 'admin'


# In[84]:


ui = input("Enter the username: ")


# In[85]:


username == ui.strip()


# In[86]:


ui = input("Enter the username: ")


# In[87]:


username == ui.strip()


# In[88]:


ui = input("Enter the username: ")


# In[89]:


username == ui.strip()


# In[90]:


ui = input("Enter the username: ")
username == ui.strip()


# In[91]:


ui.strip()


# In[92]:


st = '   Tanush          '


# In[93]:


st.strip()


# In[94]:


st


# In[95]:


at = 'test entry level'


# In[97]:


at.zfill(36)


# In[99]:


at.center(22)


# String contains -->
#  -- alpha
# -- num
# -- alpha +num
# 

# In[103]:


n = '1634684'
n.isnumeric()


# In[107]:


n = 'vres164egdfgh'
n.isalpha()


# In[108]:


n.isnumeric()


# In[109]:


n.isalnum()


# In[111]:


n = 'vs#bdg1259'
n.isalnum()


# In[114]:


n.isnumeric()


# In[115]:


n = '$ 25000'


# In[116]:


n.isnumeric()


# In[118]:


n[1:].isnumeric()


# In[119]:


n[2:].isnumeric()


# In[120]:


n[2:]


# In[124]:


n = '1#2#3#'


# In[129]:


nm = n.split('#')
nm


# In[130]:


nm[0]+nm[1]+nm[2]


# In[132]:


n= '123'
n.isdigit()


# In[133]:


n.isdecimal()


# In[134]:


n.isnumeric()


# In[135]:


nm = '0'


# In[136]:


n.isdigit()


# In[137]:


n.isdecimal()


# In[138]:


n.isnumeric()


# In[140]:


nm = '550.556'
nm.isdigit()


# In[141]:


n.isdecimal()


# In[142]:


n.isnumeric()


# In[146]:


nmm = '-2'
nmm.isdigit()


# In[148]:


nmm = '-2'
nmm.isdecimal()


# In[157]:


nmm = '2m'
nmm.isdigit()


# In[155]:


nmt = '2m'
nmt.isnumeric()


# ###  isDigits ---> 
# check whether string contains only digits --> supports decimal, subscripts, superscripts all
# 
# ###  isDecimal ---> 
# supports only decimal nums  
# 
# ### isNumeric ---> 
# checks whether all the characters are numeric --> supports digits, vulgar fractions, subscripts,                                   superscripts, roman nums, currency numerators 

# In[167]:


nmt = '$200'
nmt.isnumeric()


# In[168]:


nmt = 'XII'
nmt.isnumeric()


# ## Type Casting
# 
# -- data will be mostly available in the form of string.
# -- you may have to change the type of data according to your use.
# -- tuple are immutable but it can be converted into list to modify. 
# 
# 

# In[1]:


p = [1, 2, 3]


# In[2]:


p1 = ['a', 'b', 'c']


# In[3]:


dict(zip(p,p1))


# In[19]:


list_1 = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 0, 2, 1, 0, 3, 5]


# In[20]:


tuple(list_1)


# In[21]:


set(list_1)


# In[22]:


a = '12'


# In[23]:


b = '89'


# In[24]:


int(a)+int(b)


# In[25]:


t = list


# In[26]:


tt = set(t)
tt


# In[28]:


tuple(tt)


# In[29]:


75/6


# In[30]:


75//6


# In[32]:


import math
math.ceil(75/6)


# ## Operators
# 
# #### ** - used to find power
# #### // - used to find the floor and ceiling of number -- like for 12.5, 12 is floor and 13 is ceiling
# #### % - to calculate reminder
# #### = - to assign values
# #### == - it is used to compare the numbers or strings
# 
# #### conditional operators - <, >, <=, >=, !=
# 
# #### Membership operator - in , not in -- mostly will find in list, tuple, string, dictionary, sets 

# In[34]:


a = 10
b = 20


# In[37]:


a>b


# In[38]:


a<b


# In[39]:


a<=b


# In[40]:


a>=b


# In[41]:


a!=b


# In[42]:


d = {'1':'a', '2':'b', '3':'c'}


# In[43]:


1 in d.keys()


# In[44]:


'1' in d.keys()


# In[45]:


('1','a') in d.items()


# In[46]:


10 in list_1


# In[47]:


5 in list_1


# In[48]:


10 not in list_1


# ## Bitwise Operator

# In[4]:


ab = 35
cd = 35


# In[5]:


ab == cd


# In[7]:


id(ab)


# In[8]:


id(cd)


# In[9]:


bin(15)


# In[10]:


bin(2)


# In[11]:


hex(2)


# In[12]:


bin(42)


# In[14]:


int(0b101010)  # 32+0+8+0+2+0 = 42


# In[15]:


20 | 2


# In[16]:


30 & 7


# In[17]:


15>>2


# In[18]:


15<<2


# In[3]:


print('Hi')
print('Welcome')
print('to Python')

## by defalut it will have endline command


# In[4]:


print('Hi', end=' ')
print('Welcome', end=' ')
print('to Python')


# In[6]:


py_list = ['Python', 'Java', '12345', '936', 'crv64vr', 'loop', 'ML', "SCADA", 'AI', 'anaconda']

for item in py_list:
    if item.isalpha():
        print(item)


# In[7]:


for i in range(101,501,50):
    print(i)

