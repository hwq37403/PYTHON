import csv

newValuesFile = r"I:\vscode workspace\PYTHON\SQL_Generator\newValues.csv"
sqlStatements = []
table = 'OSUSR_H0L_QUESTION'
column = 'displayorder'

#open file 
with open(newValuesFile, newline='') as csvfile:
    #save file contents to object
    reader = csv.DictReader(csvfile)

    #insert file object contents into string template
    for row in reader:
        if(row['newvalue'] == ''):
            pass
        else:
            #Set up sql string template
            newValue = row['newvalue']
            rowId = row['id']
            sqlString = f"update {table} set {column} = '{newValue}' where id = {rowId}\n"

            sqlStatements.append(sqlString)
print(sqlStatements)

#save sql to new file
with open('sqlFile.txt', 'w') as sqlFile:
    for statement in sqlStatements:
        sqlFile.write(statement)