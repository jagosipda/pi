url = "http://naver.com"
my_str = url.replace("http://", "")  #규칙1 
#print(my_str)
my_str = my_str[:my_str.index(".")] #규칙2
passward = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"  #규칙3
print("{} 의 비밀번호는 {} 입니다.".format(url, passward))

print("고양이는\n귀엽다")