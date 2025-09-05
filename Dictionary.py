users_informations = {
    "arsalan": {
        "language": "English",
        "age": "16",
        "profession": "Student"
    },
    "mueed":{
        "language": "Spanish",
        "age": "21",
        "profession": "Musician"
    },
    "hussain":{
        "language": "Arabic",
        "age": "15",
        "profession": "Trainer"
    },
}

for key, values in users_informations.items():
    print(f"\n{key.title()}'s info:")
    for keys,val in values.items():
        print(f"\t{key.title()}'s {keys} is {val}")