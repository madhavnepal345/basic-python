#dictinoary is mutable it means it  can be changed after its creation.#
dict_1={
    "name":"Ram",
    "age":25,
    "address":"Biratnagr",
    "Mobile_No":9876543210
}
dict_1["age"]=19
print(dict_1["name"])


#%%
#we can also change the value of dictinoary into list
student_data={
    "name":"ram",
    "age":23
}
student_data_1={
    "name":"sita",
    "age":20
}
list_1=[student_data,student_data_1]
print(type(list_1))
print(list_1)
# %%
