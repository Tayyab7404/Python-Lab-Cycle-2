def get_key(d, val):
    for key, value in d.items():
        if val == value:
            return key
    return 'key doesnot exist'

specialities = {"P":"Pediatrics",
                "O":"Orthopedics",
                "E":"ENT"}

patients = {"P":0,
            "O":0,
            "E":0}

l = input("Enter id of patients along with specialities visited: ").split(',')

for i in range(1,len(l), +2):
    patients[l[i]] += 1

m = max(patients.values())
print("Maximum visited speciality in the hospital: ", specialities[get_key(patients, m)])