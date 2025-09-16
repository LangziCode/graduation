import operator

class UserBasedCF:
    def __init__(self):
        self.N = {}  # 用户交互的商品数，N[u]=用户u交互的商品数量
        self.W = {}  # 用户u和用户v的相似性

        self.train = {}  # train = { user : [[item1, rating1], [item2, rating2], …], …… }
        self.item_users = {}  # item_users = { item : [user1, user2, …]， …… }

        # 从k个最相似的用户中推荐n个商品
        self.k = 30
        self.n = 10

    def get_data(self, file_path):
        """
        @description: 从数据集中加载数据
        @file_path: 数据集路径
        """
        with open(file_path, 'r') as f:
            for i, line in enumerate(f, 0):
                if i != 0:  # 删除第一行的标题
                    line = line.strip('\n')
                    user, item, rating, timestamp = line.split(',')
                    self.train.setdefault(user, [])
                    self.train[user].append([item, rating])

                    self.item_users.setdefault(item, [])
                    self.item_users[item].append(user)

    def similarity(self):
        """
        @description: 计算用户u和用户v之间的相似度
        """
        for item, users in self.item_users.items():
            for u in users:
                self.N.setdefault(u, 0)
                self.N[u] += 1
                for v in users:
                    if u != v:
                        self.W.setdefault(u, {})
                        self.W[u].setdefault(v, 0)
                        self.W[u][v] += 1  # 用户u和用户v都交互过的商品数
        for u, user_cnts in self.W.items():
            for v, cnt in user_cnts.items():
                self.W[u][v] = self.W[u][v] / (self.N[u] * self.N[v]) ** 0.5  # 用户u和用户v之间的相似性

    def recommendation(self, user):
        """
        @description:为用户推荐商品
        @param-user：推荐的用户，我们称此用户为u
        @return：推荐给用户u的商品
        """
        watched = [i[0] for i in self.train[user]]  # 用户已交互的商品
        rank = {}
        for v, similar in sorted(self.W[user].items(), key=operator.itemgetter(1), reverse=True)[
                          0:self.k]:  # 根据用户v和用户u之间的相似性对用户v进行排序
            for item_rating in self.train[v]:  # 用户u和用户v都交互过的item数
                if item_rating[0] not in watched:  # 商品用户未交互
                    rank.setdefault(item_rating[0], 0.)
                    rank[item_rating[0]] += similar * float(item_rating[1])
        return sorted(rank.items(), key=operator.itemgetter(1), reverse=True)[0:self.n]