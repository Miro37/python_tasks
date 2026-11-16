from flask import Flask, request
app=Flask(__name__)
@app.route('/helloworld')
def printtaus():
    maara_str = request.args.get('maara', '1')
    numero=int(maara_str)

    palautus=numero*" Hello world"
    return palautus


if __name__=='__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
