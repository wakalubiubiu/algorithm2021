if __name__ == '__main__':
    list_a = [[0]*2 for i in range(10001)]
    def find(x):
        if x == fa[x]:
            return x
        fa[x] = find(fa[x])
        return fa[x]

    while True:
        money = 0
        str_input = input("")
        if str_input == '\n' or str_input == '':
            continue
        list_input = str_input.replace("   ", " ").replace("  ", " ").split(" ")
        n = list_input[0]
        # list_input = list_input[1:]
        fa = [i for i in range(10001)]
        local = 1
        for i in range(1, len(list_input), 2):
            list_a[local][0] = int(list_input[i])
            list_a[local][1] = int(list_input[i+1])
            local += 1

        list_a_sorted = sorted(list_a, key=lambda x: x[0], reverse=True)
        for i in list_a_sorted:
            last_available_day = find(i[1])
            if last_available_day > 0:
                money += i[0]
                fa[last_available_day] = last_available_day -1
        print(money)
