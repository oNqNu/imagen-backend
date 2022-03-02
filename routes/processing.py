import shutil
import os
import cv2
import numpy as np
import base64


from flask import Blueprint, request, current_app
from werkzeug.utils import secure_filename

bp = Blueprint('processing', __name__, url_prefix='/processing')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def cv_to_base64(img):
	_, encoded = cv2.imencode(".jpg", img)
	img_str = base64.b64encode(encoded).decode("ascii")

	return img_str

def clear_uploads():
	shutil.rmtree('uploads')
	os.mkdir('uploads')

@bp.route("/grayscale", methods=['POST'])
def grayscale():
	if request.files['image'].filename != u'':
		file_data = request.files['image'].read()
		nparr = np.fromstring(file_data, np.uint8)
		img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
		im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		img_str = cv_to_base64(im_gray)
		return img_str
	
	return '処理失敗'

@bp.route("/smoothing", methods=['POST'])
def smoothing():
	if request.files['image'].filename != u'':
		file_data = request.files['image'].read()
		nparr = np.fromstring(file_data, np.uint8)
		img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
		im_smooth = cv2.blur(img,(11,11))
		img_str = cv_to_base64(im_smooth)
		return img_str
	
	return '処理失敗'

@bp.route("/edge_detection", methods=['POST'])
def edge_detection():
	if request.files['image'].filename != u'':
		file_data = request.files['image'].read()
		nparr = np.fromstring(file_data, np.uint8)
		img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
		im_edge = cv2.Canny(img,180,300)
		img_str = cv_to_base64(im_edge)
		return img_str
	
	return '処理失敗'

@bp.route("/binary", methods=['POST'])
def binary():
	if request.files['image'].filename != u'':
		file_data = request.files['image'].read()
		nparr = np.fromstring(file_data, np.uint8)
		img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
		# 一度グレスケール化
		im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		ret, im_binary = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
		img_str = cv_to_base64(im_binary)
		return img_str
	
	return '処理失敗'
