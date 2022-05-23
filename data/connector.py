import mysql.connector

from data.config import password, user, IP


def connection():
    conn = mysql.connector.connect(
        user=user,
        password=password,
        host=IP,
        port=3306,
        database='q_bot',
        auth_plugin='mysql_native_password')
    return conn


def connection_special():
    conn = mysql.connector.connect(
        user=user,
        password=password,
        host=IP,
        port=3306,
        database='money_bot',
        auth_plugin='mysql_native_password')
    return conn


def connection_special_1():
    conn = mysql.connector.connect(
        user=user,
        password=password,
        host=IP,
        port=3306,
        database='money_bot_1',
        auth_plugin='mysql_native_password')
    return conn