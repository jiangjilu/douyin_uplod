# -*- coding: utf-8 -*-
"""
@Time    : 2024/1/9 23:03
@Author  : superhero
@Email   : 838210720@qq.com
@File    : config.py
@IDE: PyCharm
"""

from pydantic import BaseModel
import os
from datetime import datetime


class Config(BaseModel):
    day: int = datetime.now().day
    video_at: list = ["@家居百科 "]  # 你要@的人的昵称，默认是必须@作者的
    video_at2: list = ["jiajubaike"]  # 你要@的人的抖音号
    # 单双日不同的话题
    today: bool = True

    video_title_list1: list = ["#家居 ", "#设计 ", "#家居生活 ", "#家居设计 "]  # 单号取这个自定义视频标题

    video_title_list2: list = ["这里会介绍家居生活中的时尚趋势#家居时尚 ，让普通的生活更时尚", "#装修 ", "#装修设计 ", "#装修效果图 ", "#家居装修 "]  # 双号取这个自定义视频标题

    title_random: bool = True  # 标题是否随机取一个，不随机的话就是全部加上去

    _path: str = os.path.abspath("")

    video_path: str = os.path.join(_path, "video")  # 视频存放路径
    cookie_path: str = os.path.join(_path, "cookie.json")  # cookie路径
    remove_enterprise: bool = True  # 是否排除企业号，建议排除否则取到政治号就不好了
    remove_custom_verify: bool = True  # 排除普通认证号
    remove_video: bool = True  # 是否自动删除video文件夹中的视频
    duration: int = 10  # 筛选>=xx秒的视频
    remove_images: bool = True  # 是否排除图集作品，必须排除，否则失败
    city: bool = False  # 是否添加位置
    city_list: list = ["深圳市"]  # 添加位置信息，从中随机，固定的话输入一个就行

    declaration: bool = True  # 是否添加声明
    declaration_int: int = 1  # 添加什么声明序号，1-6
    declaration_list: list = ["内容取材网络", "内容由AI生成", "可能引人不适", "虚构演绎，仅供娱乐", "危险行为，请勿模仿"]
    declaration_value: list = ["中国-广东-深圳", None]  # 如果设置内容自行拍摄，则必须设置此项，list[0]=拍摄地，list[1]=拍摄日期，默认当天

conigs = Config()