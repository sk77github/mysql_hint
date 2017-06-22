# -*- coding:utf-8 -*-
#coding=utf-8
__author__ = 'xuwu'

from app import app
from flask import render_template, flash, redirect,session,url_for,request
from forms import InceptionTableStructure
import MySQLdb
import inception

#首页
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

#Inception_表结构评审
@app.route('/inception_table_structure',methods=['GET','POST'])
def inception_table_structure():
    form = InceptionTableStructure()
    sql_review = {}
    if request.method == "POST":
        mysql_structure = request.form.get('mysql_structure')
        mysql_ip = request.form['mysql_host']
        mysql_port = request.form['mysql_port']
        mysql_user = request.form['mysql_user']
        mysql_password = request.form['mysql_password']
        mysql_database = request.form['mysql_database']
        mysql_action = request.form['mysql_action']
        sql_review = inception.table_structure(mysql_structure,mysql_ip,mysql_port,mysql_user,mysql_password,mysql_database,mysql_action)
        return render_template('dba_tool/inception_table_structure.html',sql_review = sql_review,abc = mysql_structure)
    return render_template('dba_tool/inception_table_structure.html')
