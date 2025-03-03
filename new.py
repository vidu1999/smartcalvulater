def result(test):
    test = test
    te = test
    test_len1 = len(test)
    new_test1 = test.split("+")
    #print(new_test1)
    split_test1 = []
    multi = []
    ans = []
    for i in new_test1:
        split_test1 = split_test1 + i.split("-")
    for i in range(len(split_test1)):
        if '*' in split_test1[i] or '/' in split_test1[i]:
            multi.append(split_test1[i])
    #print(multi)
    #print(split_test1)
    # test=['20*50','40*2']
    for text in multi:
        test = text

        test_len = len(text)
        new_test = test.split("+")
        #print(new_test)
        split_test = []
        last_test = []
        new_last_test = []
        #
        nul_an = []
        div_an = []
        for i in new_test:
            split_test = split_test + i.split("-")
        """for i in range(len(split_test)):
            if '*' in split_test[i] or '/' in split_test[i]:
                multi.append(split_test[i])
        print(multi)"""
        for i in split_test:
            last_test = last_test + i.split("*")

        for i in last_test:
            new_last_test = new_last_test + i.split("/")
        """for i in multi:
            split_test.remove(i)"""
        #print(split_test)
        #print(last_test)
        #print(new_last_test)

        a = 0
        answer = 1
        answer_test = []
        final_test = []
        final_test = final_test + new_last_test
        answer_test = answer_test + new_last_test
        for i in range(len(new_last_test) - 1):
            a = a + len(new_last_test[i]) + 1
            #print(a)

            if test[a - 1] == '*':
                answer = int(answer_test[i]) * int(answer_test[i + 1])
                answer_test[i + 1] = str(answer)

            elif test[a - 1] == '/':
                #print(answer_test[i])
                answer = int(int(answer_test[i]) / int(answer_test[i + 1]))
                answer_test[i + 1] = str(answer)
            else:
                continue

        ans.append(answer)
        #print(ans)
        #print(new_last_test)
    n = 0
    for i in split_test1:
        if '*' in i or '/' in i:
            b = split_test1.index(i)
            split_test1[b] = ans[n]
            n = n + 1
        else:
            c = split_test1.index(i)
            #print(c)
            split_test1[c] = int(split_test1[c])
    #print(split_test1)
    k = 0
    fi = split_test1[k]
    for j in te:
        if j == '+':
            fi = fi + split_test1[k + 1]
            # print(fi)
            k = k + 1
        if j == '-':
            fi = fi - split_test1[k + 1]
            k = k + 1
            # print(fi)"""
        else:
            continue
    print("ANSWER IS:",fi)
