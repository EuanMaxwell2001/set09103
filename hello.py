from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
        <body> 
            <h1>OH HELLO THERE</h1>
            <img src="https://i.pinimg.com/originals/22/b7/3d/22b73ddfc4cbe22a4a6a4799bb37488b.jpg">
        </body>
    </html>
    '''
