
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

f = open('task_1.txt', 'wb')
pickle.dump(dict_list, f)
f.close()

f = open('task_1.txt', 'rb')
data = pickle.load(f)
print(data)
f.close()
