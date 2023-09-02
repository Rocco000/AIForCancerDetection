import matplotlib.pyplot as plt
import pandas as pd

file_path='Data/AllSolutionsGA2.csv'
df=pd.read_csv(file_path)

def plot_genes_trend():
    plt.figure(figsize=(11, 6))
    plt.subplots_adjust(hspace=0.38)
    plt.suptitle('PyGAD genes trend')

    plt.subplot(2,2,1) #nRow,nColumn,index
    plt.title('Learning rate')
    plt.plot(df['generation'], df['learning_rate'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.ylabel('Value')

    plt.subplot(2,2,2) #nRow,nColumn,index
    plt.title('Batch size')
    plt.plot(df['generation'], df['batch_size'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2])
    plt.ylabel('Value')

    plt.subplot(2,2,3) #nRow,nColumn,index
    plt.title('Number of epochs')
    plt.plot(df['generation'], df['num_epoch'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3])
    plt.ylabel('Value')

    plt.subplot(2,2,4) #nRow,nColumn,index
    plt.title('Optimizer')
    plt.plot(df['generation'], df['optimizer'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3])
    plt.ylabel('Value')
    plt.savefig('Scripts/Model/EvaluationGASecondApproach/TrendsPlots/genesTrend1.png')
    plt.show()

    plt.figure(figsize=(11, 6))
    plt.subplots_adjust(hspace=0.38)
    plt.suptitle('PyGAD genes trend')

    plt.subplot(2,2,1) #nRow,nColumn,index
    plt.title('Layer 1')
    plt.plot(df['generation'], df['layer1'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,2) #nRow,nColumn,index
    plt.title('Layer 2')
    plt.plot(df['generation'], df['layer2'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,3) #nRow,nColumn,index
    plt.title('Layer 3')
    plt.plot(df['generation'], df['layer3'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,4) #nRow,nColumn,index
    plt.title('Layer 4')
    plt.plot(df['generation'], df['layer4'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')
    plt.savefig('Scripts/Model/EvaluationGASecondApproach/TrendsPlots/genesTrend2.png')
    plt.show()

    plt.figure(figsize=(11, 6))
    plt.subplots_adjust(hspace=0.38)    
    plt.subplot(2,2,1) #nRow,nColumn,index
    plt.title('Layer 5')
    plt.plot(df['generation'], df['layer5'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,2) #nRow,nColumn,index
    plt.title('Layer 6')
    plt.plot(df['generation'], df['layer6'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,3) #nRow,nColumn,index
    plt.title('Layer 7')
    plt.plot(df['generation'], df['layer7'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,4) #nRow,nColumn,index
    plt.title('Layer 8')
    plt.plot(df['generation'], df['layer8'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')
    plt.savefig('Scripts/Model/EvaluationGASecondApproach/TrendsPlots/genesTrend3.png')
    plt.show()

    plt.figure(figsize=(11, 6))
    plt.subplots_adjust(hspace=0.38)
    plt.subplot(2,2,1) #nRow,nColumn,index
    plt.title('Layer 9')
    plt.plot(df['generation'], df['layer9'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,2) #nRow,nColumn,index
    plt.title('Layer 10')
    plt.plot(df['generation'], df['layer10'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,3) #nRow,nColumn,index
    plt.title('Layer 11')
    plt.plot(df['generation'], df['layer11'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,4) #nRow,nColumn,index
    plt.title('Layer 12')
    plt.plot(df['generation'], df['layer12'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')
    plt.savefig('Scripts/Model/EvaluationGASecondApproach/TrendsPlots/genesTrend4.png')
    plt.show()

    plt.figure(figsize=(11, 6))
    plt.subplots_adjust(hspace=0.38)
    plt.subplot(2,2,1) #nRow,nColumn,index
    plt.title('Layer 13')
    plt.plot(df['generation'], df['layer13'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,2) #nRow,nColumn,index
    plt.title('Layer 14')
    plt.plot(df['generation'], df['layer14'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,3) #nRow,nColumn,index
    plt.title('Layer 15')
    plt.plot(df['generation'], df['layer15'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')

    plt.subplot(2,2,4) #nRow,nColumn,index
    plt.title('Layer 16')
    plt.plot(df['generation'], df['layer16'])
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13])
    plt.ylabel('Value')
    plt.savefig('Scripts/Model/EvaluationGASecondApproach/TrendsPlots/genesTrend4.png')
    plt.show()


def plot_fitness_trend():
    df['part']= df.index // 8
    result=df.groupby('part')['fitness_value'].max()
    plt.figure(figsize=(7, 5))
    plt.title('Fitness value trend')
    plt.plot(result)
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.savefig('Scripts/Model/EvaluationGASecondApproach/TrendsPlots/fitnessTrend.png')
    plt.show()


def plot_new_solution_trend():
    solution_already_seen=list()
    number_new_individuals=list()
    df['part']= df.index // 8
    i=0
    new_solutions=0
    for _, row in df.iterrows():
        i+=1
        individual=[[row['learning_rate'], row['batch_size'], row['num_epoch'],row['optimizer'],row['layer1'],row['layer2'],row['layer3'],row['layer4'],row['layer5'],row['layer6'],row['layer7'],row['layer8'],row['layer9'],row['layer10'],row['layer11'],row['layer12'],row['layer13'],row['layer14'],row['layer15'],row['layer16']]]
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
    plt.xticks([0,1,2,3,4,5,6])
    plt.xlabel('Generation')
    plt.ylabel('Value')
    plt.savefig('Scripts/Model/EvaluationGASecondApproach/TrendsPlots/newSolutionsTrend.png')
    plt.show()



plot_genes_trend()
plot_fitness_trend()
plot_new_solution_trend()


    