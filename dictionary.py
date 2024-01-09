person = {
    "firstName" : "Burhan",
    "lasName" : "Faizee",
    "email" : "burhanfaizullah@gmail.com",
    "age" : 11,
    "isMale" :True,
}
print(person)
print(person["firstName"])
message = "Hi, my name is " + (person["firstName"]) + ". " + (person["lasName"]) + ". I am " + str(person["age"]) + " years old."
print(message)