# Spotify-Song-Cohort-Analysis-using-Clustering
Performed EDA and clustering on Spotify song data to group tracks into meaningful cohorts based on audio features like energy, tempo, and danceability. Cleaned data, engineered features, and applied K-Means with Elbow and Silhouette methods to identify optimal clusters, enabling better understanding of song similarity and recommendation insights.



# 🎧 Spotify Song Cohort Analysis (Clustering Project)

## 📌 Project Overview

Spotify, with over 456 million monthly active users and 195 million premium subscribers, relies heavily on personalized recommendations to enhance user experience. This project focuses on grouping songs into **cohorts (clusters)** based on their characteristics, enabling better recommendation systems.

As a data scientist, the goal is to:

* Understand the structure and quality of the dataset
* Explore relationships between song features
* Engineer meaningful features
* Apply clustering techniques to group similar songs

---

## 🎯 Problem Statement

Create **cohorts of similar songs** using clustering techniques based on audio and metadata features. These cohorts can later be used to improve recommendation systems by suggesting songs with similar characteristics.

---

## 🗂️ Dataset Description

The dataset is described in data_dictionary.xlsx

---

## 🔍 Project Workflow

### 1. 🧹 Data Inspection & Cleaning

* Checked for **duplicate records**
* Handled **missing values** 
* Identified and corrected **erroneous or irrelevant entries**
* Detected and treated **outliers** using statistical methods

---

### 2. 📊 Exploratory Data Analysis (EDA)

* Univariate analysis (distribution of features)
<img width="800" height="400" alt="Figure_2 5" src="https://github.com/user-attachments/assets/1f13d639-67ad-4e47-a61b-f074511a710d" />
<img width="800" height="400" alt="Figure_2 4" src="https://github.com/user-attachments/assets/76763fba-6c71-4bc1-b6ca-90e246a07cad" />
<img width="800" height="400" alt="Figure_2 3" src="https://github.com/user-attachments/assets/efda10bf-d6bf-4faf-87c5-981e26beae9b" />
<img width="800" height="400" alt="Figure_2 2" src="https://github.com/user-attachments/assets/ac46b41d-3252-4445-bb8c-ec548262f32c" />
<img width="800" height="400" alt="Figure_2 1" src="https://github.com/user-attachments/assets/275aab5b-c617-4ad9-928d-1eb2e26c66fd" />
<img width="1000" height="600" alt="Figure_1" src="https://github.com/user-attachments/assets/2a9548ce-dc9b-4e22-9474-ad0b49c96b00" />

* Bivariate/multivariate analysis (correlation heatmaps)

<img width="1440" height="749" alt="Figure_3" src="https://github.com/user-attachments/assets/23441e57-d943-4f40-b8f7-94fa996bc9fa" />

<img width="1000" height="700" alt="Figure_6" src="https://github.com/user-attachments/assets/4dc85960-1ee2-40b3-8779-67e766e72d9f" />

  
* Feature relationships and trends

<img width="1200" height="600" alt="Figure_7" src="https://github.com/user-attachments/assets/7d709398-7241-4022-a66a-84dabc8b1811" />

<img width="1000" height="600" alt="Figure_8" src="https://github.com/user-attachments/assets/d677b2a3-4ca8-40fe-aac9-2fb72d01a732" />


---

### 3. ⚙️ Feature Engineering

* Feature scaling (Normalization)
* Transformation of skewed variables
* Dimensionality reduction (PCA)

---

### 4. 🤖 Cluster Analysis

Applied unsupervised learning techniques to group songs:

#### Algorithms Used:

* **K-Means Clustering**
* Hierarchical Clustering (optional)
* DBSCAN (optional)

#### Steps:

* Determined optimal number of clusters using:

  * Elbow Method
  * Silhouette Score
* Trained clustering models
* Visualized clusters in reduced dimensions (PCA/2D plots)

---

## 📈 Results & Insights

* Identified distinct **song cohorts** based on musical characteristics
* Observed patterns such as:

  * High-energy vs low-energy clusters
  * Acoustic vs instrumental groupings
* Insights can be used to:

  * Improve recommendation systems
  * Enhance playlist generation
  * Understand listener preferences

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy** (Data Processing)
* **Matplotlib, Seaborn** (Visualization)
* **Scikit-learn** (Clustering & ML)
* **Jupyter Notebook**

---

## 📁 Project Structure

```
├── rolling_stones_spotify.csv
├── data_dictionary.xlsx
├── VSCode_Spotify project/
│   └── main.py
│   └── missing_values.py
│   └── outlayers.py
│   └── requirments.txt
├── outputs/
│   └── visualizations (.png)
├── README.md
```
---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## ✨ Author

**Ujjwal Manikya Nath**
Data Science | Machine Learning | Computer Vision

