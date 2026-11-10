from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import uiautomator2 as u2
import time
import os

app = Flask("specter", static_folder='.')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/hide-followers', methods=['POST'])
def hide_followers():
    data = request.json
    hide = data.get('hide')

    try:
        d = u2.connect()
        
        # 1. فتح التطبيق
        d.app_start("com.nerogram.instagram", stop=True)
        time.sleep(4)
        
        # 2. فتح الإعدادات (السداسي)
        d.click(180, 180) 
        time.sleep(2)
        
        # 3. إعدادات NeroGram
        d(text="إعدادات NeroGram").click_exists(timeout=3)
        time.sleep(2)
        
        # 4. خصوصية المتابعين
        d(text="خصوصية المتابعين").click_exists(timeout=3)
        time.sleep(2)
        
        # 5. الضغط على الزر
        if hide:
            if d(text="تفعيل الإخفاء").exists:
                d(text="تفعيل الإخفاء").click()
        else:
            if d(text="تفعيل الإخفاء").exists:
                d(text="تفعيل الإخفاء").click()

        return jsonify({"message": "تمت العملية بنجاح!"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if True:
    app.run(host='0.0.0.0', port=3000)