

1. 300分 给出M个货物的大小，求一个容量ans，你可以提供两个ans大小的仓库，来放下M个货物，求ans的最小值。 例如 M=3  17 8 11. 答案为19 两个19的仓库可以放下11+8， 17 的货物，且 19为最小值。
2. 100分 给出N个时间，秒，为在第i个页面停留的时间， 要求60s内浏览的页面不能超过4个。 例如10 10 10 10 10 10  为false， 10 120 10 40. 第一个60s浏览了1个页面， 第二个60秒 0个页面， 第三个60秒 3个页面 为true；
3. 较为复杂的字符串是否符合规则的题目， 大概为规则1：正常文本，带空格不带其它符号的英文文本。 第二第三（文本|文本） [文本|文本]  同为|两边不能为空，|可有可无。  第四{数字，数字} 必须包含两个数字。这道题不给错误案例，规则太繁琐了。


int main() {
    int t, n;
    cin >> t;
    while (t--) {
        scanf("%d", &n);
        vector<int> num(n);
        for (int i = 0; i < n; i++)
            scanf("%d", &num[i]);
        vector<int> finish(n);
        int ans = 1;
        unordered_map<int, int> hash;
        for (int i = 0; i < n; i++) {
            finish[i] = i > 0 ? finish[i - 1] + num[i] : num[i];
            int minu = (finish[i] - 1) / 60;
            hash[minu]++;
            if (hash[minu] > 4) {
                ans = 0;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}
第一题01背包，满分





import sys

if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    minute = 60
    for i in range(n):
        cnt = 1  # 第几分钟
        result = []
        sum_time = 0
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        # go through each line
        for j in range(values[0]):
            sum_time += values[j + 1]  # 累计时间
            while sum_time >= cnt * minute:  # 只要超过60s，120s等
                result.append(j - sum(result))  # 记录每分钟读了几页
                cnt += 1
            if j == values[0] - 1 and sum_time < cnt * minute:  # 手动处理最后一页
                result.append(j + 1 - sum(result))
        if (all(ele < 4 for ele in result)):
            print(1)
        else:
            print(0)