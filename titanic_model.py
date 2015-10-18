import pandas as pd
import csv

train_file = "train.csv"
test_file = "test.csv"
predictions_file = "mymodel.csv"

# reading and writing nessesary files
train_df = pd.read_csv(train_file)
test_df = pd.read_csv(test_file)
predictions_file = open("mymodel1.csv", "w")
predictions_file_object = csv.writer(predictions_file)
predictions_file_object.writerow(["PassengerId", "Survived"])


# iterate thought test data and make a prediction for each row
for p_index, p in test_df.iterrows():
    p_id = p['PassengerId']        
    if (p['Sex'] == 'female') or (p['Age'] < 18 and p['Pclass'] < 3 and p['Parch'] > 0):
        # survival criteria go here
        predictions_file_object.writerow([p[0], "1"])	
    else:
        predictions_file_object.writerow([p[0], "1"])
												
# Close out the files.
predictions_file.close()