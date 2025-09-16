import jwt
from configs.settings import SECRET_KEY
import time


class Myjwt():
    def __init__(self) -> None:
        # 初始化secret key变量 来自settings模块的SECRET_KEY
        self.secret_key = SECRET_KEY

    def jwt_encode(self, data, secret_key=None):

        if secret_key is None:
            secret_key = self.secret_key
        # jwt库的encode方法 将data数据和secret_key秘钥作为参数 使用HS256算法进行编码
        return jwt.encode(data, secret_key, algorithm='HS256')

    def jwt_decode(self, token):
        try:
            # jwt库的decode方法 将token和secret_key秘钥作为参数 使用HS256算法进行解码 结果保存在data变量中
            data = jwt.decode(token, self.secret_key, algorithms='HS256')
        except:
            #解码过程中出现异常 将data设置为空字典
            data = {}
        return data


myjwt = Myjwt()
