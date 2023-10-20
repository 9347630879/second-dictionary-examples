#dictionary create methods
#from_keys
keys = ('id','name','email','mobilenumber')
value = ("")
user =dict.fromkeys({'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'})
print(user)

#setdefault
user:dict = dict({})
user.setdefault('id',1)
user.setdefault('name','sundhar')
user.setdefault('email','sai@gmail.com')
user.setdefault('ph.no','9347630879')
print(user)

#update

user:dict = ({'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'})
user.update({'firstname':'sundhar'})
print(user)


#delete methods of dictionary
#pop
user:dict = {'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'}
user.pop("email")
print(user)


#pop item
user:dict = {'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'}
user.popitem()
user.popitem()
user.popitem()
print(user)

#clear
user:dict = {'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'}
user.clear()
print(user)


#access dictionary items
#access by using key

user:dict = {'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'}
print(user["mobilenumber"])

#get


user:dict = {'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'}
print(user.get('email'))

#keys

user:dict = {'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'}
print(user.keys())

#values
user:dict = {'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'}
print(user.values())

#items


user:dict = {'firstname':'sai','lastname':'gokavaram','email':'sai@gmail.com','mobilenumber':'9347630879'}
print(user.items())


