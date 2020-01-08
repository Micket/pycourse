x = parse_login_event('[2018-05-06T13:35:45] - LOGIN_FAILED: mikael@123.45.67.89')
print(x)

y = parse_login_event('[2018-05-06T14:03:10] - LOGIN_SUCCESS: thomas@10.20.30.40')
print(y)

z = parse_login_event('[2018-05-06T15:35:45] - FILE_UPLOAD: "exam_results.txt" mikael@123.45.67.89')
print(z)
