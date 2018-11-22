from socket import * 
import pymysql
import os
# if import multiprocessing and the chirld procss can't input

#定义全局变量
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)
DICT_TEXT = './dict.txt'

