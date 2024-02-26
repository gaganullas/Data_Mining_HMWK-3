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
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Improving cohesion (SSE) in K-means doesn't necessarily enhance separation (SSB) as they represent distinct optimization objectives. Tightening clusters reduces SSE but doesn't inherently maximize the dissimilarity between clusters."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "When clustering data with K-means, the sum of within-cluster sum of squares (SSE) and between-cluster sum of squares (BSS) remains constant, equaling the total sum of squares (TSS)."

    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Cohesion and separation are independent metrics in K-means clustering, and improving one doesn't necessarily guarantee improvement in the other."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Testing"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Testing"

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Testing"

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    string_number = "0.00"
    

    # type: a string that evaluates to a float
    answers["(a) SSE"] = float(string_number)

    # type: a string that evaluates to a float
    answers["(b) SSE"] = float(string_number)

    # type: a string that evaluates to a float
    answers["(c) SSE"] = float(string_number)

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
    answers["(a)"] = set('A','B')

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Groups A and B are going to be combined because their distance, measured from the furthest right point in A to the furthest left point in B, is shorter than the distance between A and C, as well as between B and C."

    # type: set
    answers["(b)"] = set('A','C')

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Groups A and C are going to be combined because they have the shortest complete link distance, which is measured between a boundary point of A and the farthest point in C. This distance is shorter than the complete link distances between A and B (measured from the left-most point in A to the right-most point in B) and between B and C (measured from the right-most point in B to the farthest point in C)"

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = set('B','C','D','E','F','G','I','J','L','M')

    # type: set
    answers["(a) boundary"] = set()

    # type: set
    answers["(a) noise"] = set('A','H')

    # type: set
    answers["(b) cluster 1"] = set('B','C','D','E','F','G')

    # type: set
    answers["(b) cluster 2"] = set('I','J','L','M')

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
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The cluster with the largest clustering entropy is Cluster 4 because it has a more balanced distribution of objects across different classes compared to the other clusters."

    # type: string
    answers["(b)"] = "Cluster 2"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "It primarily contains objects from the Forest class, with very few objects from other classes. The dominance of one class within the cluster leads to lower entropy"

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
    answers["(a)"] = ['Hierarchical','overlapping','partial']

    # type: list
    answers["(b)"] = ['Partitional','exclusive','complete']

    # type: list
    answers["(c)"] = ['Partitional','fuzzy','partial']

    # type: list
    answers["(d)"] = ['Hierarchical','overlapping','partial']

    # type: list
    answers["(e)"] = ['Partitional','Exclusive','complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "It can also be hierarchical structure ,where students with similar performance levels can be grouped together"

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The points in the nose, eyes, and mouth are much closer together than the points between these areas."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "No"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means may partition data based on overall density in both scenarios, lacking specificity to identify distinct nose, eyes, and mouth patterns amidst surrounding facial regions"

    # type: string
    answers["(c)"] = "Gaussian Mixture Models"

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
