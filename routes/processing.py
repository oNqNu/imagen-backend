import shutil
import os
import cv2
import base64


from flask import Blueprint, request, current_app
from werkzeug.utils import secure_filename

bp = Blueprint('processing', __name__, url_prefix='/processing')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allwed_file(filename):
    # .があるかどうかのチェックと、拡張子の確認
    # OKなら１、だめなら0
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def cv_to_base64(img):
    _, encoded = cv2.imencode(".jpg", img)
    img_str = base64.b64encode(encoded).decode("ascii")

    return img_str

def clear_uploads():
    shutil.rmtree('uploads')
    os.mkdir('uploads')

@bp.route('/hello')
def hello():
    return 'Hello, oNqNu!'

@bp.route("/test", methods=['POST'])
def test():
    if 'file0' not in request.files:
            return 'ファイルがありません．'

    img = request.files.get('file0')
    print(type(img))


    if img.filename == '':
            return 'ファイル名が確認できない．'

    if img and allwed_file(img.filename):
            # 危険な文字を削除（サニタイズ処理）
            filename = secure_filename(img.filename)
            # ファイルの保存
            img.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            # アップロード後のページに転送
            img = cv2.imread('uploads/' + filename)
            print(img.shape)
            im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('uploads/gray.jpg', im_gray)
            clear_uploads()
            img_str = cv_to_base64(im_gray)
            return img_str
    

    return 'qqq'
