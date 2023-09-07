# OncoVision
 ![OncoVision logo](https://github.com/Rocco000/OncoVision/blob/main/OncoVisionLogo.png)
 
 In this project  we will focus on skin cancer, namely the melanoma. Melanoma is a malignancy of melanocytes, which are pigment-producing cells of neuroectodermal origin that can be found throughout the body (including in the skin, iris and rectum). The cutaneous form of the disease is common in the Western world accounts for the majority (75%) of skin cancer-related death; its global incidence is 15–25 per 100,000 individuals. Survival rates in patients with melanoma (cumulative for all forms) have shown a huge differences between countries in Europe, ranging between <50% in Eastern Europe to >90% in northern and central Europe for 5-year survival after primary diagnosis. The biggest problem with this cancer type is a lack of early detection that does not allow therapy to treat the disease on time. That is why we decided to develop a melanoma detection AI system to help physicians.
 
 We decided to call our model OncoVision because this name combines "oncology", the study and treatment of cancer, with "vision", emphasizing the system's ability to "see" the tumour mass.

 ## 📂 ​Datasets
 
  We used three datasets, namley [Skin Cancer MNIST: HAM10000](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000), [Melanoma Detection Dataset](https://www.kaggle.com/datasets/wanderdust/skin-lesion-analysis-toward-melanoma-detection) and some data from [ISIC archive](https://api.isic-archive.com/collections/?pinned=true). For the first dataset we had different classes, therefore, we had to collapse these different categories into fewer classes:
  * _bkl_, df, nv and vasc classes into __benign folder__
  * _bcc_ class in __carcinoma folder__
  * _akiec_ class in __bowenDisease folder__
  * _mel_ class in __melanoma folder__
 For the second dataset, we extracted the contents of the train, test and valid folders. We then moved the images contained in the seborrheic_keratosis folder into the benign folder.
 From ISIC archive, we used ISIC 2018, ISIC 2019 and ISIC 2020 dataset to extract only the malanoma images.
 All the data collected was cropped due to the presence of black borders and some other types of noise like pieces of colored cloth. Then we resized them into 450x600px.

## 🧠​🧬 ​Models

 We developed three AI models:
 * [Base model](https://github.com/Rocco000/OncoVision/blob/main/Scripts/ModelsScripts/ModelArchitecture1.ipynb) is a simple convolutional neural network;
 * Two genetic algorithms that produce a population of Convolutional Neural Networks (CNNs) optimized from two points of view:
  * The [GA1](https://github.com/Rocco000/OncoVision/blob/main/Scripts/ModelsScripts/GAapproach1.ipynb) goal is to improve the training algorithm hyperparameters of the base mode;
  * The [GA2](https://github.com/Rocco000/OncoVision/blob/main/Scripts/ModelsScripts/GAApproach2.ipynb) goal is to improve both training algorithm hyperparameters and network architecture.
  We defined the same objective function for both GA versions and it is the follows : $f(x)= w_1 * accuracy+w_2 * precision+w_3 * recall$ where $w_1=0.2$, $w_2=0.35$ and $w_3=0.45$.

## 📊 Results

 To sum up, the best solution is the output of the GA1 because it represents a good trade-off between accuracy, precision and recall. Indeed, it achieved 81% accuracy, 68% precision and 86% recall on the test set. Instead, the best solution of GA2 obtained a high false positive rate, which may be due to the high number of random substitutions, whereas the base model reached good results despite its default hyperparameters configuration. Further insights are provided in the [report](https://github.com/Rocco000/OncoVision/blob/main/Documentation/OncoVision.pdf).

## 🛠️ Future works

 - [ ] Collect new data, especially samples of different ethnicities, to address potential fairness issues;
 - [ ] Increase the population size and the number of generations of genetic algorithms to explore the search space further;
 - [ ] Change the substitution techniques in genetic algorithms to reduce the randomness;
 - [ ] Consider energy consumption during training to improve the sustainability of the model.

## ⚙️ ​Project structure

 * Data directory contains the data quality and survey results;
 * Documentation directory contains the project documentation;
 * Model directory contrains the evaluation metrics of the models and the results of the genetic algorithms;
 * Scripts directory contains two subfolders:
  * DataPreprocessingScripts contains all scripts to pre-process the collected data;
  * ModelsScripts contains all code necessary to develop melanoma detection AI system.

## 💻 Project environment

 Please download the necessary library indicated in requirements.txt to run the pre-processing scripts.
 `code(pip install -r requirements.txt)`
 To run models, you can modify the code snippet and insert the appropriate path. MLflow was used to track the performance of the models. If you don't want to use it, remove the corresponding code.

## 📧 ​Contact

 Rocco Iuliano - rocco.iul2000@gmail.com
 
 Simone Della Porta - sdellaporta34@gmail.com
