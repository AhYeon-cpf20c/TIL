password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# 아래에 코드를 작성하시오.


first_char = password[28:35]           # password 문자열 28번째~35번째
second_word = password[113:118]        # password 문자열 113번째부터 5글자
third_word = password[66:69][::-1]     # password 문자열 66번째~68번째까지 뒤집어서 출력
fourth_word = password[322:326][::-1]  # password 문자열 322번째부터 4글자 뒤집어서 출력
fifth_word = password[365:371]         # password 문자열 365번째부터 'python' 출력

result = f'{first_char} {second_word} {third_word} {fourth_word} "{fifth_word}".'

print(result)

