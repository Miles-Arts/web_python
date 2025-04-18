from flask import Flask 

#Aplicacion Flask = app
app=Flask(__name__)

@app.route('/') 
def principal():
      return   "🚀 Bienvenido a mi Web con Python 🤖"   

@app.route('/contacto')
def contacto():
      return "Página de contacto"

if __name__=='__main__':
      app.run(debug=True, port=5017)  
