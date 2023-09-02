import matplotlib.pyplot as plt
import pandas as pd

file_path='Data/AllSolutionsGA1.csv'
df=pd.read_csv(file_path)

def plot_genes_trend():
    plt.figure(figsize=(11, 6))
    plt.subplots_adjust(hspace=0.38)
    plt.suptitle('PyGAD genes trend')

    plt.subplot(2,2,1) #nRow,nColumn,index
    plt.title('Learning rate')
    plt.plot(df['generation'], df['learning_rate'])
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
    plt.xlabel('Generation')
    plt.ylabel('Value')

    plt.subplot(2,2,2) #nRow,nColumn,index
    plt.title('Batch size')
    plt.plot(df['generation'], df['batch_size'])
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
    plt.xlabel('Generation')
    plt.yticks([1,2])
    plt.ylabel('Value')

    plt.subplot(2,2,3) #nRow,nColumn,index
    plt.title('Number of epochs')
    plt.plot(df['generation'], df['num_epoch'])
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
    plt.xlabel('Generation')
    plt.yticks([1,2,3])
    plt.ylabel('Value')

    plt.subplot(2,2,4) #nRow,nColumn,index
    plt.title('Optimizer')
    plt.plot(df['generation'], df['optimizer'])
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
    plt.xlabel('Generation')
    plt.yticks([1,2,3])
    plt.ylabel('Value')
    plt.savefig('Scripts/Model/EvaluationGAFirstApproach/TrendsPlots/genesTrend.png')
    plt.show()


def plot_fitness_trend():
    df['part']= df.index // 8
    result=df.groupby('part')['fitness_value'].max()
    plt.figure(figsize=(7, 5))
    plt.title('Fitness value trend')
    plt.plot(result)
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.savefig('Scripts/Model/EvaluationGAFirstApproach/TrendsPlots/fitnessTrend.png')
    plt.show()


def plot_new_solution_trend():
    solution_already_seen=list()
    number_new_individuals=list()
    df['part']= df.index // 8
    i=0
    new_solutions=0
    for _, row in df.iterrows():
        i+=1
        individual=[[row['learning_rate'], row['batch_size'], row['num_epoch'],row['optimizer']]]
        if  not (individual in solution_already_seen):
            new_solutions+=1
            solution_already_seen.append(individual)
        
        if i==8:
            number_new_individuals.append(new_solutions)
            new_solutions=0
            i=0

    plt.figure(figsize=(7, 5))
    plt.title('New solutions trend')
    plt.plot(number_new_individuals)
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10])
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.savefig('Scripts/Model/EvaluationGAFirstApproach/TrendsPlots/newSolutionsTrend.png')
    plt.show()



plot_genes_trend()
plot_fitness_trend()
plot_new_solution_trend()


    