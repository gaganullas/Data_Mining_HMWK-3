# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Agglomerative hierarchical clustering merges clusters based on proximity, progressively forming a hierarchical structure and effectively mitigating the influence of outliers by grouping them with nearby points.while k-means assigns points to centroids, making it sensitive to outliers influence on centroid positions."

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "In k-means, the initial placement of centroids is random, leading to varying clusterings in different runs. However, agglomerative hierarchical clustering always produces the same clustering because it follows a deterministic process of merging clusters based on proximity."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "While k-means is generally more computationally efficient and memory-friendly than agglomerative hierarchical clustering for large datasets, it's not accurate to say it's the most efficient clustering algorithm possible. Other algorithms may outperform k-means under certain conditions or have advantages in specific scenarios."

    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "SSE of the clustering typically decreases.This is because splitting a cluster into two allows the centroids to better represent the data points within each smaller cluster, resulting in reduced distances between data points and their respective centroids."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "When the Sum of Squared Errors (SSE) decreases during the clustering process in K-means, it means that the data points within each cluster are getting closer to their respective centroids. This implies that the clusters are becoming more cohesive."

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "When SSB increases, it means that the centroids are farther apart from each other, indicating more separation between the clusters."

    # type: bool (True/False)
    answers["(g)"] = -1

    # type: explanatory string (at least four words)
    answers["(g) explain"] = ""

    # type: bool (True/False)
    answers["(h)"] = -1

    # type: explanatory string (at least four words)
    answers["(h) explain"] = ""

    # type: bool (True/False)
    answers["(i)"] = -1

    # type: explanatory string (at least four words)
    answers["(i) explain"] = ""

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = -1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: bool (True/False)
    answers["(b)"] = -1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: bool (True/False)
    answers["(c)"] = -1

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = 7.5

    # type: a string that evaluates to a float
    answers["(b) SSE"] = 7.5

    # type: a string that evaluates to a float
    answers["(c) SSE"] = 7.5

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 0

    # type: int
    answers["(a) Circle (b)"] = 0

    # type: int
    answers["(a) Circle (c)"] = 0

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: int
    answers["(b) Circle (a)"] = 0

    # type: int
    answers["(b) Circle (b)"] = 0

    # type: int
    answers["(b) Circle (c)"] = 0

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 0

    # type: explanatory string (at least four words)
    answers["(c) explain"] = ""

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = set()

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: set
    answers["(b)"] = set()

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set()

    # type: set
    answers["(a) boundary"] = set()

    # type: set
    answers["(a) noise"] = set()

    # type: set
    answers["(b) cluster 1"] = set()

    # type: set
    answers["(b) cluster 2"] = set()

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = set()

    # type: set
    answers["(c)-a boundary"] = set()

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = set()

    # type: set
    answers["(c)-b cluster 2"] = set()

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b)"] = ""

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = ""

    # type: string
    answers["(a) Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = ""

    # type: string
    answers["(a) Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = ""

    # type: string
    answers["(b) Row 1"] = ""

    # type: string
    answers["(b) Row 2"] = ""

    # type: string
    answers["(b) Row 3"] = ""

    # type: string
    answers["(b) Row 4"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = ""

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = ""

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = []

    # type: list
    answers["(b)"] = []

    # type: list
    answers["(c)"] = []

    # type: list
    answers["(d)"] = []

    # type: list
    answers["(e)"] = []

    # type: explanatory string (at least four words)
    answers["(e) explain"] = ""

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = ""

    # type: string
    answers["(a) Figure (b)"] = ""

    # type: explanatory string (at least four words)
    answers["(a) explain"] = ""

    # type: string
    answers["(b) Figure (a)"] = ""

    # type: string
    answers["(b) Figure (b)"] = ""

    # type: explanatory string (at least four words)
    answers["(b) explain"] = ""

    # type: string
    answers["(c)"] = ""

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
