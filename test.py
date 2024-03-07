print("Hello world!")

# dont have to "let variable =21";
name = "Ricardo"
last_name = "Hurtado"
total = 14.33
age = 36
found = True

# if/else statement js vs python
# if (var==var2){
# logic
# }
# this is a test
if age < 100:
    print("Don't worry you're not that old")
    print("This is only a example")
elif age == 100:
    print("Congratz you're a Century")
else:
    print("Sorry, seem that you're knock knock on Heaven Door")

#funtion
# function say_hello(){}

def say_hello():
    print("Hey Dude")

def say_goodbye(name):
    print("Goobye "+ name)

# to call funtion
say_hello()
say_goodbye("Ricardo")

#concatinate
print("Hello my name is " + name +" and am " + str(age) +" years old")

#arrary
#list      0      1       2      3      
colorList = ["red","white","blue","black"]
numberList = [1,2,3]

#add 
colorList.append("pink")

#travle the list
for temp in numberList:
    print(temp)
#ex:for (i=0;color.len;i++)
    #let temp = color [i]
        #console.log(temp) js