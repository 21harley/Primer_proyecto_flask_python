from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def hello_wordl():
    return render_template("index.html")

@app.route("/contacto",defaults={"correo":'-'})
@app.route("/contacto/<correo>")
def fn_contacto(correo):
    return render_template('contacto.html',usuario=correo)

if __name__ == "__main__":
    app.run(debug=True)

