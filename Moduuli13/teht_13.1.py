from flask import Flask, request
app=Flask(__name__)
@app.route('/alkuluku')
def alkuluku():
    luku_str=request.args.get("luku")
    jako=0
    luku=int(luku_str)
    if luku <=1:
        return(f"Luku {luku} ei ole alkuluku")
    if luku == 2:
        return(f"Luku {luku}  ei ole alkuluku")
    for i in range(2, luku,):
        if luku % i == 0:
            jako +=1
        if jako ==0:
            return(f"Luku {luku} on alkuluku")
        else:
            return(f"Luku {luku} ei ole alkuluku")
  

if __name__=='__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)