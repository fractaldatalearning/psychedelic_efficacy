# Psychedelic Efficacy: NLP Modeling & Predictions
### How well might psychedelic drugs work to treat mental illness, compared with prescription psych meds? What insights can be drawn from anonymously-submitted psychedelic experience reports?

![pink and purple chemical lab environment](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/reports/figures/cover_img.png)

[Please see a summary of findings and explanation of methodoligical judgements in the final report.](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/reports/Katin_Capstone3_Report.pdf) For a breakdown of how to explore the underlying work throughout this project, read on:

Functions used throughout the notebook are saved in the [source folder](https://github.com/fractaldatalearning/psychedelic_efficacy/tree/main/src) and [tested here](https://github.com/fractaldatalearning/psychedelic_efficacy/tree/main/tests/test_nlp). 

In [notebook 1](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/notebooks/1-kl-wrangle-tabular.ipynb) and [notebook 2](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/notebooks/2-kl-wrangle_duplicates.ipynb), I wrangle data from multiple scientific studies measuring the efficacy of prescription psych meds based on user ratings with accompanying reviews. In [notebook 3](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/notebooks/3-kl-studies-early-eda-parse.ipynb), I begin to conduct exploratory data analysis comparing the target variable "rating" and other variables such as "drug," "condition," or the "date" the review was subitted. I begin parsing the tet of the narratve reviews. In [notebook 4](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/notebooks/4-kl-studies-nlp.ipynb), I conduct natural language processing to remove symbols other than those associated with sentiment (emoji or !!!), correct spelling, remove stopwords other than those associated with sentiment (i.e. 'not', 'very'), and lemmatize the text.

In [notebook 5](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/notebooks/5-kl-studies-lang-eda-preprocess.ipynb), I engineer features based on the text of the drug reviews, for example, length, complexity, subjectivity, and polarity. The feature most correlated with the target variable "rating" is text sentiment polarity, as seen below. In [notebook 6](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/notebooks/6-kl-studies-finish-preprocess.ipynb), I explore options for quantify the words of the text itself for each  review and settle upon creating a sparse matrix using CountVectorizer. 

![Boxplot demonstrating the relationship between a drug's rating and its review's sentiment polarity.](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/reports/figures/studes_rating_polarity.png) 

In [notebook 7](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/notebooks/7-kl-studies-modeling.ipynb), I use a randomized grid search to selet a best model and hyperparameters. Final ComplementNB model evaluation metrics include: 0.58 F1 score, 1.27 log loss, 0.75 roc_auc, and accuracy with best k=2 of 0.73. 

![Confusion matrix of true and predicted ratings.](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/reports/figures/confusion_matrix.png)

In [notebook 8](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/notebooks/8-kl-scraping.ipynb), I scrape psychedelic experience reports from erowid.org. In [notebook 9](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/notebooks/9-kl-reports-clean-engineer.ipynb), I clean these reports and engineer features to mimic those of the prescription psych med reviews from the trained model. 

In [notebook 10](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/notebooks/10-kl-reports-engineer-ratings.ipynb), I apply the model to the new scraped data and use predicted ratings to compare psychedelic and prescription drugs. 
###The average rating of psychedelics turns out to be 4.49, compared with 3.93 for presription meds. 
This is likely due to the fact that more psychedeli experience reports' sentiment is positive. 

![Figure deomonstrating the relative distributions of sentiment polarity among psychedelic reports and prescription med reviews.](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/reports/figures/compare_polarity.png)


--------
[Please see the project proposal for citations/links to original data sources](https://github.com/fractaldatalearning/psychedelic_efficacy/blob/main/references/kl_cap3_proposal_psychedelic_efficacy.pdf)

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
