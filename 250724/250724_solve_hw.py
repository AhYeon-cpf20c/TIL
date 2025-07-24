pro_num = {'key' : 1000}
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

def create_data(subject, day , title =None, key=None):
    global pro_num
    pro_num['key'] += 1
    data = {'과목': subject,'일차' : day, '제목': title, '문제번호' : pro_num }
    return data

result_1 = create_data(global_data['subject'],global_data['day'])
print(result_1)

result_2 = create_data('web', 1, 'web 연습하기')
print(result_2)
 
result_3 = create_data(global_data['subject'],global_data['day'], global_data['title'],**pro_num)
print(result_3)


