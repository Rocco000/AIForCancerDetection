def get_duplicates_names(path):
    duplicate_names=list()
    with open(path,'r') as file:
        for row in file:
            row=row.split('/')
            duplicate_names.append(row[len(row)-1])
    return duplicate_names
            

file09=get_duplicates_names('D:/datasets/duplicates_analysis/09 - 2017_train_vs_2017_test_duplicates_deleted.txt')
file06=get_duplicates_names('D:/datasets/duplicates_analysis/06 - all_train_duplicates_deleted_(all but newest).txt')
file12=get_duplicates_names('D:/datasets/duplicates_analysis/12 - all_test_duplicates_deleted_(all but newest).txt')
duplicate_names=file09+file06+file12
with open('Data/duplicates.txt','w') as file:
    for row in duplicate_names:
        file.write(row)