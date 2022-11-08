import config
import pickle
import json
import numpy as np


# Creating class
class CreditRisk():

    #  custumer inputes
    def __init__(self,person_age, person_income, person_emp_length, loan_grade, loan_amnt, loan_int_rate, loan_percent_income, cb_person_cred_hist_length, person_home_ownership, loan_intent, cb_person_default_on_file):
        self.person_age           = person_age
        self.person_income        = person_income
        self.person_emp_length    = person_emp_length
        self.loan_grade           = loan_grade
        self.loan_amnt            = loan_amnt
        self.loan_int_rate        = loan_int_rate
        self.loan_percent_income  = loan_percent_income
        self.cb_person_cred_hist_length = cb_person_cred_hist_length
        self.person_home_ownership      = "person_home_ownership_" + person_home_ownership
        self.loan_intent                = "loan_intent_" + loan_intent
        self.cb_person_default_on_file  = "cb_person_default_on_file_" + cb_person_default_on_file


    
    # "loading models"
    def load_model(self):
        with open(config.MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_PATH, "r") as f:
            self.json_data = json.load(f)

    # predicting load status
    def predict_loam_status(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.person_age
        test_array[1] = self.person_income
        test_array[2] = self.person_emp_length
        test_array[3] = self.json_data["loan_grade"][self.loan_grade]
        test_array[4] = self.loan_amnt
        test_array[5] = self.loan_int_rate
        test_array[6] = self.loan_percent_income
        test_array[7] = self.cb_person_cred_hist_length


        idx1 = self.json_data["columns"].index(self.person_home_ownership)
        test_array[idx1] = 1

        idx2 = self.json_data["columns"].index(self.loan_intent)
        test_array[idx2] = 1

        idx3 = self.json_data["columns"].index(self.cb_person_default_on_file)
        test_array[idx3] = 1

        status = self.model.predict([test_array])
        return status

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



