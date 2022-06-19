import psycopg2
mydb =  psycopg2.connect(
    database = "manyy",
    user ="postgres",
    password="123456789",
    host="localhost",
    port=5432,
)
cursor = mydb.cursor()
query = 'Select * from "manish"'
cursor.execute(query)
array=list(cursor.fetchall())
print(array)
print("given data is:")
for x in array:
    print(x)
    
def merge_sort(list):
    list_length = len(list)
    if list_length == 1:
        return list
    mid_point = list_length // 2
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])
    return merge(left_partition, right_partition)


def merge(left, right):
    output = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][2] < right[j][2]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    output.extend(left[i:])
    output.extend(right[j:])
    return output


def run_merge_sort():
    print(x)
   

run_merge_sort()    

