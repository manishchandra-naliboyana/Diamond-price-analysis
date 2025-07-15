# Diamond Price Analysis

## Project Overview

This project explores and analyzes the key factors that influence diamond prices. Using real-world data, the goal is to understand how features like **carat**, **cut**, **color**, and **clarity** impact price, uncover patterns, and visualize meaningful insights for jewelers, sellers, and buyers.

---

## Dataset

The analysis uses the well-known **Diamonds dataset**

**Main features:**
- **carat**: Weight of the diamond.
- **cut**: Quality of the cut (`Fair`, `Good`, `Very Good`, `Premium`, `Ideal`).
- **color**: Diamond color grade, from D (best) to J (worst).
- **clarity**: Clarity of the diamond, measuring internal flaws (`I1` (lowest) to `IF` (flawless)).
- **depth, table**: Proportional measurements of the diamond.
- **x, y, z**: Physical dimensions in millimeters.
- **price**: Price in USD.

---

## Analysis Performed

### Exploratory Data Analysis (EDA)
- Inspected data shape, types, and descriptive statistics.
- Checked for missing values and cleaned the dataset.
- Explored distributions of numerical features like **carat** and **price** using histograms.
- Analyzed **cut**, **color**, and **clarity** with countplots.
- Examined relationships between **carat** and **price** using scatterplots.
- Compared price trends across different **cuts**, **colors**, and **clarities** with boxplots and violin plots.
- Created correlation heatmaps to find patterns among numerical variables.
- Identified outliers and trends that could impact diamond valuation.

---

## Key Insights

- **Carat** shows a strong positive correlation with price — heavier diamonds tend to be significantly more expensive.
- **Cut**, **color**, and **clarity** also have clear effects on price, with higher-quality grades generally raising the value.
- Outliers highlight rare diamonds or potential data anomalies.
- Visualizations reveal that combining a high **carat** with the best **cut**, **color**, and **clarity** greatly increases price.

---

## Requirements

- Python 3.x
- pandas
- numpy
- matplotlib
- seaborn
- jupyter

To install dependencies, run:

```bash
pip install -r requirements.txt
```

---

## How to Run

**1. Clone this repository:**
```bash
git clone https://github.com/your-username/diamond-price-analysis.git
```

**2. Install the required libraries:**
```bash
pip install -r requirements.txt
```

**3. Launch the notebook:**
```bash
jupyter notebook
```

**4. Open the EDA notebook and run the cells step by step.**

---
