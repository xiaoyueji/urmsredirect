from flask import render_template
from app import app

@app.route('/')
@app.route('/reservation')
def reservation():
	url = {'link': 'https://link.jiandaoyun.com/f/5cff9c21f115a814c62f070c'}
	return render_template('index.html', title='预约', url=url)

@app.route('/enrollfarm')
def enrollfarm():
	url = {'link': 'https://link.jiandaoyun.com/f/5cf79b82c3b0b415b7661602'}
	return render_template('index.html', title='创意农场自助报名', url=url)

@app.route('/enrollbus')
def enrollbus():
	url = {'link': 'https://link.jiandaoyun.com/f/5cf7c9b51e9f5215bd747d85'}
	return render_template('index.html', title='律动巴士自助报名', url=url)

@app.route('/managefarm')
def managefarm():
	url = {'link': 'https://link.jiandaoyun.com/f/5cf7a0a7f115a814c6c95c94'}
	return render_template('index.html', title='创意农场课时管理', url=url)

@app.route('/managebus')
def managebus():
	url = {'link': 'https://link.jiandaoyun.com/f/5cf89f8449075414d81e2fef'}
	return render_template('index.html', title='律动巴士课时管理', url=url)