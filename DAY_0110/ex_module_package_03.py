# ------------------------------------------------------------------------------
# 패키지 사용법
# => 모듈 내의 모든 변수, 함수, 클래스 포함
# ------------------------------------------------------------------------------
# 사용할 모듈 로딩 -------------------------------------------------------------
# import 패키지명.모듈명
import urllib.request as req


# from 패키지명 import 모듈명
from urllib import error, parse

from http.client import HTTPResponse

dataObj = req.urlopen("https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png")
# 객체타입
print(dataObj)