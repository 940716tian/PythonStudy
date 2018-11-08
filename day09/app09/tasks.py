from celery import task
import time

# @task
# def hello_celery(loop):
# 	for i in range(loop):
# 		print('hello')
# 		time.sleep(2)

@task
def my_task():
    time.sleep(5)
    #假设在发送邮件
    print("执行")


@task
def task2(n):
	for i in range(n):
		print(i)
		time.sleep(2)

@task
def res_task(n):
	print(n)
	#也可以通过缓存保存结果
	return {"data":n}

@task
def write_task():
	print("我是定时炸弹")