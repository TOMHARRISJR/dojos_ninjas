from flask_app import app
from flask_app.controllers import dojos_ninjas_controller
app.secretkey = "buttcrack"




if __name__ == "__main__":
    app.run(debug=True)
