🛎️ Leveraging data analytics and machine learning to improve customer service satisfaction
==============================
[Udacity Nanodegree in Data Science](https://www.udacity.com/course/data-scientist-nanodegree--nd025) - Capstone

Customer Satisfaction is a cornerstone of e-commerce. In this project, I leveraged [data analysis](#analysis), [machine learning](#ml) (including [NLP](#nlp)) and [deployment tools](https://csatisfaction-app.herokuapp.com/) to provide insights and recommendations on how to improve customer service experience.

If you have any questions or suggestions, just send me a 💬 via [LinkedIn](https://www.linkedin.com/in/josecruz-phd/). Enjoy!


Table of Contents
---

1. [About](#about)
  - [Problem Introduction](#overview)
  - [Strategy to solve the problem](#strategy)
  - [Metrics](#metrics)
  - [EDA](#analysis)
  - [Modelling](#model)
  - [Hyperparameter tuning](#ht)
  - [Results](#results)
  - [Conclusion/Reflection/Recommendations](#conclusion)
  - [Improvements](#improve)
2. [Repository Contents](#contents)
3. [Installation & Requirements](#installation)
4. [The Data](#data)
5. [Licensing and Acknowledgements](#licensing)



<a id="about"><a/>
## 1. About

<a id="overview"><a/>
### 🔎Problem Introduction
---

Customer Satisfaction is a cornerstone of e-commerce. Having a strong customer service satisfaction builds trust and brand reputation which leads to more sales and revenue. Also, improving customer experience improves retention of clients. Bad customer service represents a missed opportunity for revenue.


**How can we leverage customer service data to improve customer satisfaction?**



<a id="strategy"><a/>
### 🧭Strategy to solve the problem
---

To solve the problem, I first divided the main questions into 3 sub questions where I could combine analytics and machine learning to provide the answers:

**Problem 1:** How do the service current KPIs look like?
**Strategy:** Perform exploratory data analysis on the KPIs and extract insights about the current state of the service.

**Problem 2:** Can we extract the 3 main complaints associated with bad  satisfaction based on comments summited by customers?
**Strategy:** Combine NLP and perform topic extraction on the comment data available in the dataset.

**Problem 3:** Can we predict customer satisfaction for missing labels using machine learning?
**Strategy:** Use a supervised classification model that can be easily explainable to management to predict the binary satisfaction score (ie Good/Bad).

<a id="metrics"><a/>
### 🎯Metrics
---

To evaluate the current customer satisfaction with the service, I used 5 metrics:
- Proportion of customer satisfaction scores
- Average Reply time
- Full Resolution time
- Number of contacts per case (CPC)
- First time Resolution

In the machine learning task, for the binary classification model I used the metric `accuracy` since the target class distribution was balanced.


<a id="analysis"><a/>
### 📊EDA
---
**source:** `notebooks/nb01_data-exploration.ipynb`
**source:** `notebooks/nb03_modeling-part2.ipynb`

**Problem 1: How does the service current KPIs look like?**
In the notebook `notebooks/nb01_data-exploration.ipynb`, I prepared the data and performed the exploratory data analysis (EDA).

 > I used dash/plotly/heroku to prepare and **[deploy a dashboard](https://csatisfaction-app.herokuapp.com/)** with all the main findings based on the EDA.


**Problem 2: Can we extract the 3 main complaints associated with bad  satisfaction based on comments summited by customers?**

After each interaction with the customer service, customers can leave an optional comment to support their review. Based on these comments, I used **NLP** for **topic modeling** with Latent Dirichlet allocation (**LDA**) to perform an unsupervised extraction of the 3 main topics of complaints.


 Briefly, [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar.


<a id="model"><a/>
### 📊Modeling
---

**source:** `notebooks/nb02_modeling-part1.ipynb`


**Problem 3: Can we predict customer satisfaction for missing labels using machine learning?**

Around ~30% the ticket data have missing customer satisfaction label. Using information from EDA, I built a decision tree classifier to predict Good/Bad customer satisfaction based on `replytime`, `fullresolutiontime` and `cpc`(contacts per case).



<a id="ht"><a/>
### 🚧Hyperparameter tuning
---

**source:** `notebooks/nb02_modeling-part1.ipynb`

Steps to find the best parameters:
- Split dataset in train/test sub datasets
- Use Grid Search Cross validation to find the best parameters: `criterion = ['gini', 'entroyy']`. I fixed the `max_depth` at 2 to prevent overfitting and also to make the tree easily explainable.
- Run Cross Validation with the best model/parameters on the entire training dataset
- Evaluate the model on the testing dataset


<a id="results"><a/>
### 📈Results
---


Model performance on the both training and test dataset was ~95%. I observed that **longer `replytime` and longer `fullresolutiontime` are associated with Bad satisfaction (in orange)**:

![Decision Process](reports/figures/decision_tree.jpeg)


Based on the topic modeling analysis, the **3 main topics found in the bad complaints** and some of the words related are:
- Poor service: *Delivery*, *Inefficient* and *Bad*
- Agent Behavior: *Communication*, *Behavior*, *Slow*
- Customer Experience: *Unreliable*, *Resolution*, *Useless*


<a id="conclusion"><a/>
### 💡Conclusion/Reflection/Recommendations
---


**1.** "Payment methods", "wrong passwords" and "items not showing up" are the top complaints. Improving service on these areas will likely reduce the number of tickets and free resources in customer service.

**2.** Reply time and full resolution time are critical CSAT KPIs. Focusing resources on solving tickets that linger without reply will improve CSAT.

**3.** Topic Modeling suggests that agent behavior is sometimes inappropriate and that service is somewhat unreliable. Retrain agents to improve agent satisfaction.

**4.** It is possible to predict customer satisfaction scores with high accuracy using the decision tree. Use the tree to find tickets with predicted bad scores and build a retention campaign on the at-risk users.

<a id="improve"><a/>
### 🔭Improvements
---

**Topic Modeling**
The comments contained additional languages (e.g. French, Spanish) but during this analysis only English was considered. It would be important to also analyze the remaining data and evaluate the consistence with the current findings.

**Decision Tree Model**
Although the tree seems to be accurate, it was only trained on ~5500 of tickets handled from ~80 agents and therefore the true predictive power can be substantially lower. It would be important to further segment the data and understand whether tickets from different countries/agents impact the performance of the model.


<a id="contents"><a/>
## 2. Repository Contents

    ├── README.md        
    ├── LICENSE
    ├── Procfile
    ├── app.py             <- Dash webapp    
    ├── fig_preparation.py <- Prepare figures for dashboard
    ├── requirements.txt   <- For Heroku web deployment
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- Support documentation
    │
    ├── notebooks          <- Jupyter notebooks.
    ├── reports            <- PowerPoint Presentation
    │   └── figures        <- Generated graphics and figures
    │
    └── environment.yml    <- conda environment with required python packages


<a id="installation"><a/>
## 3. Installation & Requirements

1. Install a python environment with jupyter notebooks (e.g., [anaconda distribution](https://www.anaconda.com/products/individual)).

2. Create an environment with the required packages by running on the anaconda shell:
```
conda env create -f environment.yml --name myenv
conda activate myenv
```

3. Run notebooks:

  - `notebooks/nb01_data-exploration.ipynb`
  - `notebooks/nb02_modeling-part1.ipynb`
  - `notebooks/nb03_modeling-part2.ipynb`

<a id="data"><a/>
## 4. The Data

The data and original project scope was made freely available by [5CA](https://5ca.com/) and it is composed by __entirely simulated data__ that mimics real customer service data.

<a id="licensing"><a/>
## 5. Licensing and Acknowledgements

The analysis and code generated during this project are licensed under a MIT License.


## Disclaimer
2022, [José Oliveira da Cruz](https://www.linkedin.com/in/josecruz-phd/)

**_Disclaimer_**
The author is **not affiliated** with any of the entities mentioned nor received any kind of compensation. The information contained in this work is provided on an "as is" basis with no guarantees of completeness, accuracy, usefulness or timeliness. The author does not own/have any ownership rights on this data.
