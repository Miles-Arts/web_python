from flask import Flask 
from flask import render_template


#Aplicacion Flask = app
app=Flask(__name__)

# @app.route('/') 
# def principal():
#       return   "🚀 Bienvenido a mi Web con Python 🤖"   

# @app.route('/contacto')
# def contacto():
#       return "Página de contacto"

# if __name__=='__main__':
#       app.run(debug=True, port=5017)  


@app.route('/')
def principal():
      return render_template('index.html')

@app.route('/lenguajes')
def mostrar_lenguajes():
      web_lenguajes=( 'Python', 'Java', 'C++', 'JavaScript', 'Cobol', 'Pascal', 'Fortran', 'C#', 'PHP', 'Ruby', 'Swift', 'Go', 'Rust', 'Kotlin', 'Dart')
      return render_template('lenguajes.html',lenguajes=web_lenguajes)

@app.route('/contacto')
def contacto():
      return render_template('contacto.html')

@app.route('/proyecto')
def proyetocs():
      return render_template('proyecto.html')


if __name__=='__main__':
      app.run(debug=True, port=5017)