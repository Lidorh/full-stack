

# read the file json_read_write_file_game
import json
with open(r'python/files/json_read_write_file_game.json','r') as f:
    json_var = json.load(f);
# say hello to the player by his name
print(f"Hello {json_var['name']}")

while True:
    # ask the user to enter information
    ans= input("Do you want to enter new information? y/n \t") 
    if ans == 'n':
        break
    key = input("Enter the key\t")
    type_of_data = input("What type do you want str / arr?\t")
    if (type_of_data == 'str'):
        value = input("Enter the value\t")
        json_var['data'][key] = value
    else: # type_of_data == 'arr'
        # if the key is not in the dictionary
        if key not in json_var['data']:
            json_var['data'][key] = []
        # if there is a values but the value is text
        elif isinstance(json_var['data'][key], str):
            json_var['data'][key] = [   json_var['data'][key]  ]
        
        while True:
            # ask the user if he want to insert value
            value = input("Enter the value\t")
            json_var['data'][key].append(value)

            answerArr = input('Do you wish to add more elements to the array? y/n\t')
            if (answerArr == 'n'):
                break
# when done save the file

print(json.dumps(json_var, indent=2))

with open(r'python/files/json_read_write_file_game.json','w') as f:
    json.dump(json_var,f, indent=2)


'''
1) use this game as a basis for building a new game that you can add custom
key and value to the data including array and map (dict , object)

and if you have a nested one you should ask the user how much inside he want to go
data : {
    x: {
        a: ['y'],
        b: 's',
        c: {
            d: 's',
            e: ['w']
        }
    }
}

'''