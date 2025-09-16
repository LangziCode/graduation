from collections import defaultdict, Counter
from itertools import chain
from typing import Dict, Set, List, Tuple

class UserBasedCollaborativeFiltering:
    def __init__(self, user_item_collections: Dict[str, Set[str]]):
        self.user_item_collections = user_item_collections

    def calculate_similarity(self, user1: str, user2: str) -> float:
        user1_collections = self.user_item_collections[user1]
        user2_collections = self.user_item_collections[user2]

        intersection = user1_collections.intersection(user2_collections)
        union = user1_collections.union(user2_collections)

        similarity = len(intersection) / len(union)
        return similarity

    def recommend_items(self, target_user: str, n: int) -> Dict[str, float]:
        recommendations = defaultdict(float)

        # 计算目标用户与其他用户的相似度
        user_similarities = {}
        for user in self.user_item_collections.keys():
            if user != target_user:
                if target_user in self.user_item_collections:
                    similarity = self.calculate_similarity(target_user, user)
                    user_similarities[user] = similarity

        # 选择相似度最高的用户，并基于他们的收藏为目标用户推荐物品
        for user, similarity in user_similarities.items():
            user_collections = self.user_item_collections[user]
            for item in user_collections:
                if item not in self.user_item_collections[target_user]:  # 目标用户尚未收藏过的物品
                    recommendations[item] += similarity

        # 排序推荐物品，按照分数降序排列
        sorted_recommendations = dict(sorted(recommendations.items(), key=lambda item: item[1], reverse=True))

        top_n_recommendations = {}
        if len(sorted_recommendations) > 0:
            # 只返回前n个推荐物品
            top_n_recommendations = dict(list(sorted_recommendations.items())[:len(sorted_recommendations)])
        return top_n_recommendations
