from flask import Flask

app=Flask(__name__)

@app.route('/soyunaruta',method=['POST'])
def otra():
    return "cualquier otra cosa"

if __name__ == '__main__':
    app.run(debug=True)