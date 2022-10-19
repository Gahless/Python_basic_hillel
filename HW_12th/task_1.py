
import pickle

dict_list = [
    {
        'name': 'name1',
        'age': 'age1',
        'id': 'id1'
     },
    {
        'name': 'name2',
        'age': 'age2',
        'id': 'id2'
    },
    {
        'name': 'name3',
        'age': 'age3',
        'id': 'id3'
    },
    {
        'name': 'name4',
        'age': 'age4',
        'id': 'id4'
    }
]

with open('task_1.txt', 'wb') as f:
    pickle.dump(dict_list, f)


with open('task_1.txt', 'rb') as f:
    data = pickle.load(f)
    print(data)

