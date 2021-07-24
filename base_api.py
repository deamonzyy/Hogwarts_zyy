#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests


class BaseApi:
    CORPID="wwc0f98a061cc6f114"
    CORPSECRET= "-kQK8vvROn6svZoCihASbCTu3LM7d-5Xjy3hV88ZYrQ"
    BASEURL="https://qyapi.weixin.qq.com/cgi-bin"
    def __init__(self):
        self.token=self.get_token()

    def get_token(self):
        url = self.BASEURL+f"/gettoken?corpid={self.CORPID}&corpsecret={self.CORPSECRET}"
        r = requests.get(url)
        return r.json().get("access_token")

    def send(self,method,url,**kwargs):
        """
        封装发送请求
        :param method:请求方式
        :param url: 路由地址
        :param kwargs: 其他参数
        :return:
        """
        #post 和get 底层实现，requests.get==requests.request("GET",)
        url=self.BASEURL+url
        return requests.request(method,url,**kwargs)
