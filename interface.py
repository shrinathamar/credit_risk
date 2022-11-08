

from flask import Flask, jsonify, request, render_template

from utils import CreditRisk
import config

# ACreating app:
app = Flask(__name__)

# home page :
@app.route("/")
def home():
    return render_template("index.html")

#  for prediction :
@app.route("/predict", methods=["POST", "GET"])
def predict_credit_risk():
    data = request.form

    person_age        = int(data["age"])
    person_income     = eval(data["income"])
    person_emp_length = int(data["emp_length"])
    loan_grade        = data["grade"]
    loan_amnt         = eval(data["loan_amnt"])
    loan_int_rate     = eval(data["interest"])
    loan_percent_income        = eval(data["perc_inc"])
    cb_person_cred_hist_length = int(data["hist_length"])
    person_home_ownership = data["home_own"]
    loan_intent   = data["loan_intent"]
    cb_person_default_on_file = data["on_file"]
    

    loan = CreditRisk(person_age, person_income, person_emp_length, loan_grade, loan_amnt, loan_int_rate, loan_percent_income, cb_person_cred_hist_length, person_home_ownership, loan_intent, cb_person_default_on_file)
    status = loan.predict_loam_status()[0]
    if status == 1:
        eligible = "Eligible"
        messsage = "We will be Happy To Work With You ! Have a Good Day"
        
    else:
        eligible = "Not Eligible"
        messsage = "Try Next Time... This IS Not The End"
    
    return  render_template("index2.html", eligibility=eligible, mesg = messsage)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT_NUM1)


# person_age = 40
# person_income = 90000000
# person_emp_length = 10
# loan_grade = "B"
# loan_amnt = 2000000
# loan_int_rate = 16
# loan_percent_income = 0.57
# cb_person_cred_hist_length = 4
# person_home_ownership = "MORTGAGE"
# loan_intent = "EDUCATION"
# cb_person_default_on_file = "N"

    # if status == 0:
    #     eligibility = "Eligible"
    #     mesg = "We Can't Wait to do Business with You !"
    #     return  render_template("index2.html", eligibility=eligibility, mesg=mesg)
    # else :
    #     eligibility = " Not Eligible"
    #     mesg = "Try Next Time !"