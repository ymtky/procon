num_city, num_train, num_question = [int(i) for i in input().split()]

#電車の数
trains = [[0] * (num_city + 1) for _ in range(0, num_city + 1)]
for i in range(0, num_train):
    start, arrive = [int(j) for j in input().split()]
    trains[start][arrive] += 1

#累積和表を作る
#解説には1次元累積和を加算しても間に合うとい書いてあったが、2次元累積和でないとタイムアウトする（pythonだから遅い？）
cumlative_sum = [[0] * (num_city + 1) for _ in range(0, num_city  + 1)]
for start in range(0, num_city + 1):
    for arrive in range(0, num_city + 1):
        cumlative_sum[start][arrive] = cumlative_sum[start][arrive - 1] + trains[start][arrive]
for start in range(0, num_city + 1):
    for arrive in range(0, num_city + 1):
        cumlative_sum[start][arrive] += cumlative_sum[start - 1][arrive]

for i in range(0, num_question):
    start, arrive = [int(j) for j in input().split()]
    result = cumlative_sum[arrive][arrive] - cumlative_sum[start - 1][arrive] - cumlative_sum[arrive][start - 1] + cumlative_sum[start - 1][start - 1]
    print(result)
