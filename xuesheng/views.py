import re
from django.db.models import Q, Value, F
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework.parsers import JSONParser
import json
import base64
import os
import uuid
import cv2

def get_image_url(filename):
    """生成图片的完整访问URL"""
    if not filename:
        return None
    return f"http://localhost:8080/py56788/upload/{filename}"



import time
import random
import datetime
from datetime import timedelta
from utils.myjwt import myjwt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from address.models import *
from address.serializers import *
from orders.models import *
from orders.serializers import *
from cart.models import *
from cart.serializers import *
from news.models import *
from news.serializers import *
from messagess.models import *
from messagess.serializers import *
from exampaper.models import *
from exampaper.serializers import *
from examquestion.models import *
from examquestion.serializers import *
from examrecord.models import *
from examrecord.serializers import *
from kechengxinxi.models import *
from kechengxinxi.serializers import *
from discusskechengxinxi.models import *
from discusskechengxinxi.serializers import *
from kechengziyuanxinxi.models import *
from kechengziyuanxinxi.serializers import *
from discusskechengziyuanxinxi.models import *
from discusskechengziyuanxinxi.serializers import *
from kechengleixing.models import *
from kechengleixing.serializers import *
from xuexijihua.models import *
from xuexijihua.serializers import *
from jiaoshi.models import *
from jiaoshi.serializers import *
from xuesheng.models import *
from xuesheng.serializers import *
from tokens.models import *
from utils import *
from collections import defaultdict


# 保存
class XueshengSave(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            yonghuming=data['yonghuming']
            if yonghuming == '':
                yonghuming = None
        except KeyError:
            yonghuming = None
        except ValueError:
            yonghuming = None
        try:
            touxiang=data['touxiang']
            if touxiang == '':
                touxiang = None
        except KeyError:
            touxiang = None
        except ValueError:
            touxiang = None
        try:
            mima=data['mima']
            if mima == '':
                mima = None
        except KeyError:
            mima = None
        except ValueError:
            mima = None
        try:
            xingbie=data['xingbie']
            if xingbie == '':
                xingbie = None
        except KeyError:
            xingbie = None
        except ValueError:
            xingbie = None
        try:
            dianhua=data['dianhua']
            if dianhua == '':
                dianhua = None
        except KeyError:
            dianhua = None
        except ValueError:
            dianhua = None
        try:
            nicheng=data['nicheng']
            if nicheng == '':
                nicheng = None
        except KeyError:
            nicheng = None
        except ValueError:
            nicheng = None
        try:
            rlimg=data['rlimg']
            if rlimg == '':
                rlimg = None
        except KeyError:
            rlimg = None
        except ValueError:
            rlimg = None
        try:
            isws=data['isws']
            if isws == '':
                isws = None
        except KeyError:
            isws = None
        except ValueError:
            isws = None
        try:
            money=data['money']
            if money == '':
                money = None
        except KeyError:
            money = None
        except ValueError:
            money = None
        Xuesheng.objects.create(
            yonghuming=yonghuming,
            touxiang=touxiang,
            mima=mima,
            xingbie=xingbie,
            dianhua=dianhua,
            nicheng=nicheng,
            rlimg=rlimg,
            isws=isws,
            money=money,
        )
        return Response({"code": 0, 'msg': '添加成功'})

# 修改
class XueshengUpdate(APIView):
    def post(self, request):
        data = request.data
        id=data['id']
        yonghuming=data['yonghuming']
        touxiang=data['touxiang']
        mima=data['mima']
        xingbie=data['xingbie']
        dianhua=data['dianhua']
        nicheng=data['nicheng']
        rlimg=data['rlimg']
        isws=data['isws']
        money=data['money']
        id = data['id']
        Xuesheng.objects.filter(id=id).update(
        id=id,
        yonghuming=yonghuming,
        touxiang=touxiang,
        mima=mima,
        xingbie=xingbie,
        dianhua=dianhua,
        nicheng=nicheng,
        rlimg=rlimg,
        isws=isws,
        money=money,
        )
        return Response({'code': 0, 'msg': '修改成功'})

# 删除
class XueshengDelete(APIView):
    def post(self, request):
        data = request.data
        for id in data:
            Xuesheng.objects.filter(id=int(id)).delete()
        return Response({'code': 0, 'msg': '删除成功'})

# 查询详情
class XueshengInfo(APIView):
    def get(self, request, id):
        id = id
        entity = Xuesheng.objects.filter(id=int(id)).all()
        entityser = XueshengSer(entity, many=True)
        return Response({'code': 0, 'data': entityser.data[0]})

# 分页
class XueshengList(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量

        if page is None or limit is None:
            return XueshengListNotPage(request)
        else:
            return XueshengListPage(request)

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        if page is None or limit is None:
            return XueshengListNotPage(request)
        else:
            return XueshengListPage(request)

def XueshengListPage(request):
    userid = request.query_params.get('userid')
    page = request.query_params.get('page')  # 第几页
    limit = request.query_params.get('limit')  # 数量
    sort = request.query_params.get('sort') # 排序

    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'yonghuming__icontains': request.query_params.get('yonghuming'),
                                'touxiang__icontains': request.query_params.get('touxiang'),
                                'mima__icontains': request.query_params.get('mima'),
                                'xingbie__icontains': request.query_params.get('xingbie'),
                                'dianhua__icontains': request.query_params.get('dianhua'),
                                'nicheng__icontains': request.query_params.get('nicheng'),
                                'rlimg__icontains': request.query_params.get('rlimg'),
                                'isws__icontains': request.query_params.get('isws'),
                                'money__icontains': request.query_params.get('money'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Xuesheng.objects.filter(q_objects).all()
    count = Xuesheng.objects.filter(q_objects).count()

            # 第二步：创建分页器，每页10条数据
    paginator = Paginator(queryset, limit)
    try:
        # 获取当前页的数据
        items = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码不是整数，返回第一页
        items = paginator.page(1)
    except EmptyPage:
        # 如果页码超出范围，返回最后一页
        items = paginator.page(paginator.num_pages)
    result = XueshengSer(items, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

def XueshengListNotPage(request):
    userid = request.query_params.get('userid')
    query_params = {
                        'id__icontains': request.query_params.get('id'),
                                'addtime__icontains': request.query_params.get('addtime'),
                                'yonghuming__icontains': request.query_params.get('yonghuming'),
                                'touxiang__icontains': request.query_params.get('touxiang'),
                                'mima__icontains': request.query_params.get('mima'),
                                'xingbie__icontains': request.query_params.get('xingbie'),
                                'dianhua__icontains': request.query_params.get('dianhua'),
                                'nicheng__icontains': request.query_params.get('nicheng'),
                                'rlimg__icontains': request.query_params.get('rlimg'),
                                'isws__icontains': request.query_params.get('isws'),
                                'money__icontains': request.query_params.get('money'),
                    }
    q_objects = Q()

    for key, value in query_params.items():
        if value is not None and value.strip():  # 检查值是否非空且非空白字符串
            value = value[1: -1]
            q_objects.add(Q(**{key: value}), Q.AND)

    if userid is not None:
        q_objects.add(Q(**{'userid': userid}), Q.AND)


    queryset = Xuesheng.objects.filter(q_objects).all()
    count = Xuesheng.objects.filter(q_objects).count()
    result = XueshengSer(queryset, many=True)
    return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

# 分页
class XueshengPage(APIView):
    def get(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'yonghuming__icontains': request.query_params.get('yonghuming'),
            'touxiang__icontains': request.query_params.get('touxiang'),
            'mima__icontains': request.query_params.get('mima'),
            'xingbie__icontains': request.query_params.get('xingbie'),
            'dianhua__icontains': request.query_params.get('dianhua'),
            'nicheng__icontains': request.query_params.get('nicheng'),
            'rlimg__icontains': request.query_params.get('rlimg'),
            'isws__icontains': request.query_params.get('isws'),
            'money__icontains': request.query_params.get('money'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)


        queryset = Xuesheng.objects.filter(q_objects).all()
        count = Xuesheng.objects.filter(q_objects).count()

        # 第二步：创建分页器，每页10条数据
        paginator = Paginator(queryset, limit)
        try:
            # 获取当前页的数据
            items = paginator.page(page)
        except PageNotAnInteger:
            # 如果页码不是整数，返回第一页
            items = paginator.page(1)
        except EmptyPage:
            # 如果页码超出范围，返回最后一页
            items = None
        result = XueshengSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})

    def post(self, request):
        page = request.query_params.get('page')  # 第几页
        limit = request.query_params.get('limit')  # 数量
        sort = request.query_params.get('sort') # 排序

        query_params = {
            'id__icontains': request.query_params.get('id'),
            'addtime__icontains': request.query_params.get('addtime'),
            'yonghuming__icontains': request.query_params.get('yonghuming'),
            'touxiang__icontains': request.query_params.get('touxiang'),
            'mima__icontains': request.query_params.get('mima'),
            'xingbie__icontains': request.query_params.get('xingbie'),
            'dianhua__icontains': request.query_params.get('dianhua'),
            'nicheng__icontains': request.query_params.get('nicheng'),
            'rlimg__icontains': request.query_params.get('rlimg'),
            'isws__icontains': request.query_params.get('isws'),
            'money__icontains': request.query_params.get('money'),
        }
        q_objects = Q()

        for key, value in query_params.items():
            if value is not None and value.strip():  # 检查值是否非空且非空白字符串
                if(value.startswith('%') and value.endswith('%')):
                    value = value[1: -1]
                q_objects.add(Q(**{key: value}), Q.AND)

        queryset = Xuesheng.objects.filter(q_objects).all()
        count = Xuesheng.objects.filter(q_objects).count()

                    # 第二步：创建分页器，每页10条数据
        paginator = Paginator(queryset, limit)
        try:
            # 获取当前页的数据
            items = paginator.page(page)
        except PageNotAnInteger:
            # 如果页码不是整数，返回第一页
            items = paginator.page(1)
        except EmptyPage:
            # 如果页码超出范围，返回最后一页
            items = paginator.page(paginator.num_pages)
        result = XueshengSer(items, many=True)
        return Response({'code': 0, 'data': {'list': result.data, 'total': count}})







# 用户登录
class LoginXuesheng(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        if not all([username, password]):
            return Response({"code": 401, 'msg': '参数不全'})
        entity = Xuesheng.objects.filter(yonghuming=username, mima=password).first()
        if entity:
            token = myjwt.jwt_encode({"data": {"userid": entity.id, 'exp': int(time.time()) + 31104000}})
            current_time = datetime.datetime.now()  # 获取当前时间
            futue_time = current_time + timedelta(hours=5)
            print(current_time, futue_time)
            Token.objects.create(
                userid=entity.id,
                username=entity.yonghuming,
                tablename='xuesheng',
                role='学生',
                token=token,
                expiratedtime=futue_time
            )
            request.session['users'] = entity.id
            return Response({"code": 0, "token": token})
        else:
            return Response({"code": 401, 'msg': '账号密码错误'})

    def get(self, request):
        username = request.query_params.get('username')
        password = request.query_params.get('password')
        if not all([username, password]):
            return Response({"code": 401, 'msg': '参数不全'})
        entity = Xuesheng.objects.filter(yonghuming=username, mima=password).first()
        if entity:
            token = myjwt.jwt_encode({"data": {"userid": entity.id, 'exp': int(time.time()) + 31104000}})
            current_time = datetime.datetime.now()  # 获取当前时间
            futue_time = current_time + timedelta(hours=5)
            print(current_time, futue_time)
            Token.objects.create(
                userid=entity.id,
                username=entity.yonghuming,
                tablename='xuesheng',
                role='学生',
                token=token,
                expiratedtime=futue_time
            )
            request.session['users'] = entity.id
            return Response({"code": 0, "token": token})
        else:
            return Response({"code": 401, 'msg': '账号密码错误'})

# 用户获取session
class XueshengSession(APIView):
    def get(self, request):
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        session = myjwt.jwt_decode(token)['data']['userid']
        users = Xuesheng.objects.filter(id=session).all()
        user_ser = XueshengSer(users, many=True)
        user_ser.data[0]['role'] = 'xuesheng'
        return Response({'code': 0, 'data': user_ser.data[0]})

    def post(self, request):
        token = request.META.get('HTTP_TOKEN', 'No token provided')
        session = myjwt.jwt_decode(token)['data']['userid']
        users = Xuesheng.objects.filter(id=session).all()
        user_ser = XueshengSer(users, many=True)
        user_ser.data[0]['role'] = 'xuesheng'
        return Response({'code': 0, 'data': user_ser.data[0]})

# 用户注册
class Register(APIView):
    def post(self, request):
        data = request.data
        yonghuming=data['yonghuming']
        touxiang=data['touxiang']
        mima=data['mima']
        xingbie=data['xingbie']
        dianhua=data['dianhua']
        nicheng=data['nicheng']
        # 检查是否是完善信息（传入了ID）
        user_id = data.get('id', None)
    # 获取人脸图片数据（base64格式）
        face_image_base64 = data.get('faceImage', None)

        if not all([
            yonghuming,
            touxiang,
            mima,
            xingbie,
            dianhua,
            nicheng,
        ]):
            return Response({"code": 401, 'msg': '参数不全'})


        if user_id:
            # 根据ID更新用户信息（完善信息）
            try:
                user = Xuesheng.objects.get(id=user_id)
                user.yonghuming = yonghuming
                user.touxiang = touxiang
                user.mima = mima
                user.xingbie = xingbie
                user.dianhua = dianhua
                user.nicheng = nicheng
                user.isws = 1  # 标记为已完善信息
        # 如果传入了人脸图片数据，处理并保存
                if face_image_base64:
                    try:
                        # 处理base64图片数据
                        if ',' in face_image_base64:
                            face_image_base64 = face_image_base64.split(',')[1]

                        # 解码base64图片
                        image_data = base64.b64decode(face_image_base64)

                        # 生成图片文件名（使用用户ID）
                        face_filename = f"face_{user_id}.jpg"

                        # 保存图片
                        upload_dir = os.path.join(settings.MEDIA_ROOT, 'upload')
                        if not os.path.exists(upload_dir):
                            os.makedirs(upload_dir)

                        face_path = os.path.join(upload_dir, face_filename)

                        with open(face_path, 'wb') as f:
                            f.write(image_data)

                        # 更新用户的人脸图片路径
                        user.rlimg = face_filename

                    except Exception as e:
                        return Response({'code': 500, 'msg': f'人脸图片保存失败: {str(e)}'})

                user.save()
                return Response({'code': 0, 'msg': '信息完善成功'})
            except Xuesheng.DoesNotExist:
                return Response({'code': 401, 'msg': '用户记录不存在'})








def generate_unique_userid():
    # 获取当前时间戳（精确到微秒）
    timestamp = int(time.time() * 1000000)
    # 添加随机数
    random_part = random.randint(1, 1000000)
    # 合成唯一整数
    userid = timestamp + random_part
    return userid

class FaceRecognizeAPI(APIView):
    """人脸识别API - 匹配前端的recognize接口"""
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        """
        人脸识别接口

        前端请求格式:
        {
            "imageBase64": "data:image/jpeg;base64,/9j/4AAQSkZJRgABA...",
            "fileName": "face.png"
        }

        返回格式:
        {
            "state": 1,  // 0-未找到，1-找到
            "users": {
                "zhanghao": "用户账号",
                "mima": "用户密码"
            }
        }
        """
        try:
            data = json.loads(request.body)
            image_base64 = data.get('imageBase64', '')
            file_name = data.get('fileName', 'face.jpg')

            if not image_base64:
                return Response({'code': 400, 'msg': '未提供图片数据'})

            # 处理base64图片数据
            if ',' in image_base64:
                image_base64 = image_base64.split(',')[1]

            try:
                # 解码base64图片
                image_data = base64.b64decode(image_base64)
            except Exception as e:
                return Response({'code': 400, 'msg': '图片数据格式错误'})

            # 保存临时文件
            temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)

            temp_filename = f"face_recognize_{uuid.uuid4()}.jpg"
            temp_path = os.path.join(temp_dir, temp_filename)

            with open(temp_path, 'wb') as f:
                f.write(image_data)

            # 进行人脸检测和识别
            recognition_result = self.recognize_face(temp_path)

            # 删除临时文件
            try:
                os.remove(temp_path)
            except:
                pass

            return Response(recognition_result)

        except Exception as e:
            return Response({'code': 500, 'msg': f'处理失败: {str(e)}'})

    def recognize_face(self, image_path):
        """识别人脸并匹配用户"""
        try:
            # 检测上传图片中的人脸
            image = cv2.imread(image_path)
            if image is None:
                return {'code': 400, 'msg': '无法读取图片'}

            # 转换为灰度图
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # 初始化人脸检测器
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            if face_cascade.empty():
                return {'code': 500, 'msg': '人脸检测器加载失败'}

            # 检测人脸
            faces = face_cascade.detectMultiScale(gray, 1.05, 8, minSize=(50, 50))

            if len(faces) == 0:
                return {'code': 400, 'msg': '未检测到人脸'}

            # 找到最大的人脸（提高识别精度）
            max_face = max(faces, key=lambda face: face[2] * face[3])  # 按面积排序
            x, y, w, h = max_face

            # 提取最大人脸区域，稍微扩大边界以包含更多特征
            margin = 10
            x1 = max(0, x - margin)
            y1 = max(0, y - margin)
            x2 = min(gray.shape[1], x + w + margin)
            y2 = min(gray.shape[0], y + h + margin)

            # 截取最大人脸区域
            face_roi = gray[y1:y2, x1:x2]

            # 只查询已完善信息的用户（isws=1）进行人脸识别对比
            users_with_face = Yonghu.objects.filter(rlimg__isnull=False, isws=1).exclude(rlimg='')

            if not users_with_face.exists():
                # 没有已完善信息的用户人脸数据，只返回未匹配信息
                return {
                    'code': 0,
                    'state': 0,
                    'message': '人脸库没有当前人脸，请完善信息',
                    'needComplete': True
                }

            best_match = None
            best_similarity = 0

            # 与每个用户的人脸图像进行比较
            for user in users_with_face:
                if user.rlimg:
                    # 构建用户人脸图像完整路径
                    face_path = os.path.join(settings.MEDIA_ROOT, 'upload', user.rlimg)

                    if os.path.exists(face_path):
                        try:
                            # 读取用户人脸图像
                            user_image = cv2.imread(face_path, 0)
                            if user_image is not None:
                                # 统一尺寸进行对比（将当前截取的人脸尺寸作为标准）
                                current_face_size = face_roi.shape  # (height, width)
                                user_image_resized = cv2.resize(user_image, (current_face_size[1], current_face_size[0]))

                                # 计算直方图相似度
                                hist1 = cv2.calcHist([face_roi], [0], None, [256], [0, 256])
                                hist2 = cv2.calcHist([user_image_resized], [0], None, [256], [0, 256])
                                similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

                                # 详细的调试信息
                                print(f"\n=== 用户 {user.zhanghao} 人脸对比详情 ===")
                                print(f"用户ID: {user.id}")
                                print(f"人脸图片路径: {user.rlimg}")
                                print(f"图像尺寸: {face_roi.shape} vs {user_image_resized.shape}")
                                print(f"直方图相似度: {similarity:.4f}")
                                print(f"当前最佳相似度: {best_similarity:.4f}")
                                print(f"阈值: 0.8")
                                print(f"是否超过阈值: {'是' if similarity > 0.8 else '否'}")
                                print(f"是否更新最佳匹配: {'是' if similarity > best_similarity else '否'}")
                                print(f"=====================================\n")

                                if similarity > best_similarity and similarity > 0.8:  # 相似度阈值
                                    best_similarity = similarity
                                    best_match = user
                        except Exception as e:
                            print(f"处理用户 {user.zhanghao} 人脸图像时出错: {e}")

            # 最终结果调试信息
            print(f"\n=== 人脸识别最终结果 ===")
            print(f"检测到的人脸数量: {len(faces)}")
            print(f"数据库中人脸用户数量: {len(users_with_face)}")
            print(f"最佳匹配用户: {best_match.zhanghao if best_match else '无'}")
            print(f"最佳相似度: {best_similarity:.4f}")
            print(f"识别结果: {'成功' if best_match else '失败'}")
            print(f"========================\n")

            if best_match:
                return {
                    'code': 0,
                    'state': 1,
                    'users': {
                        'zhanghao': best_match.zhanghao,
                        'mima': best_match.mima
                    },
                    'similarity': round(best_similarity * 100, 2)
                }
            else:
                # 没有匹配的用户，只返回未匹配信息，不插入数据库
                return {
                    'code': 0,
                    'state': 0,
                    'message': '人脸库没有当前人脸，请完善信息',
                    'needComplete': True
                }

        except Exception as e:
            return {'code': 500, 'msg': f'识别失败: {str(e)}'}


class ExtractMaxFaceAPI(APIView):
    """提取最大人脸API - 匹配前端的extractMaxFace接口"""
    parser_classes = [JSONParser]

    def post(self, request, *args, **kwargs):
        """
        提取最大人脸接口

        前端请求格式:
        {
            "imageBase64": "data:image/jpeg;base64,/9j/4AAQSkZJRgABA...",
            "fileName": "face.png"
        }

        返回格式:
        {
            "id": "生成的用户ID",
            "rlimg": "保存的人脸图像路径"
        }
        """
        try:
            data = json.loads(request.body)
            image_base64 = data.get('imageBase64', '')
            file_name = data.get('fileName', 'face.jpg')

            if not image_base64:
                return Response({'code': 400, 'msg': '未提供图片数据'})

            # 处理base64图片数据
            if ',' in image_base64:
                image_base64 = image_base64.split(',')[1]

            try:
                # 解码base64图片
                image_data = base64.b64decode(image_base64)
            except Exception as e:
                return Response({'code': 400, 'msg': '图片数据格式错误'})

            # 保存临时文件
            temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir)

            temp_filename = f"extract_face_{uuid.uuid4()}.jpg"
            temp_path = os.path.join(temp_dir, temp_filename)

            with open(temp_path, 'wb') as f:
                f.write(image_data)

            # 提取最大人脸
            extract_result = self.extract_max_face(temp_path)

            # 删除临时文件
            try:
                os.remove(temp_path)
            except:
                pass

            return Response(extract_result)

        except Exception as e:
            return Response({'code': 500, 'msg': f'处理失败: {str(e)}'})

    def extract_max_face(self, image_path):
        """提取图片中最大的人脸"""
        try:
            # 检测图片中的人脸
            image = cv2.imread(image_path)
            if image is None:
                return {'code': 400, 'msg': '无法读取图片'}

            # 转换为灰度图
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # 初始化人脸检测器
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            if face_cascade.empty():
                return {'code': 500, 'msg': '人脸检测器加载失败'}

            # 检测人脸
            faces = face_cascade.detectMultiScale(gray, 1.05, 8, minSize=(50, 50))

            if len(faces) == 0:
                return {'code': 400, 'msg': '未检测到人脸'}

            # 找到最大的人脸
            max_face = max(faces, key=lambda face: face[2] * face[3])  # 按面积排序
            x, y, w, h = max_face

            # 提取人脸区域，稍微扩大边界
            margin = 20
            x1 = max(0, x - margin)
            y1 = max(0, y - margin)
            x2 = min(image.shape[1], x + w + margin)
            y2 = min(image.shape[0], y + h + margin)

            face_image = image[y1:y2, x1:x2]

            # 生成用户ID
            user_id = generate_unique_userid()

            # 根据ID生成图片文件名
            face_filename = f"face_{user_id}.jpg"

            # 保存提取的人脸
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'upload')
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            face_path = os.path.join(upload_dir, face_filename)
            cv2.imwrite(face_path, face_image)

            # 插入数据库 - 创建用户记录（isws=0表示未完善信息）
            Yonghu.objects.create(
                id=user_id,
                rlimg=face_filename,  # 数据库中只保存文件名
                isws=0,  # 未完善信息
                zhanghao=None,
                mima=None,
                shoujihao=None,
                nianling=None
            )

            # 调试信息
            print(f"\n=== 人脸提取和数据库插入详情 ===")
            print(f"生成的用户ID: {user_id}")
            print(f"人脸图片文件名: {face_filename}")
            print(f"人脸图片完整路径: {face_path}")
            print(f"人脸图片URL: {get_image_url(face_filename)}")
            print(f"人脸尺寸: {face_image.shape}")
            print(f"数据库插入状态: 成功")
            print(f"用户状态: isws=0 (未完善信息)")
            print(f"================================\n")

            return {
                'code': 0,
                'id': user_id,
                'rlimg': get_image_url(face_filename),
                'face_info': {
                    'position': {'x': int(x), 'y': int(y), 'width': int(w), 'height': int(h)},
                    'extracted_size': {'width': int(x2-x1), 'height': int(y2-y1)}
                }
            }

        except Exception as e:
            return {'code': 500, 'msg': f'提取失败: {str(e)}'}

