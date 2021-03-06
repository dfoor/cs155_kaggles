    
def get_error(G, Y):
    error=0
    for i in xrange(len(G)):
        if G[i] != Y[i]:
            error += 1
    return 1.0 * error / len(G)


def demo(train,test):

    import os
    import sys
    import csv
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn import svm
    from sklearn import tree
    from sklearn import manifold
    from sklearn import neural_network
    from sklearn import cross_validation
    from sklearn import linear_model
    from sklearn.cross_validation import cross_val_score
    from sklearn.ensemble import ExtraTreesClassifier
    from sklearn.ensemble import AdaBoostRegressor
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.cross_validation import train_test_split
    from sklearn.grid_search import GridSearchCV
    from sklearn.metrics import classification_report
    

    from sklearn.svm import SVC
    from sklearn.preprocessing import StandardScaler
    from sklearn.datasets import load_iris
    from sklearn.cross_validation import StratifiedKFold
    from sklearn.grid_search import GridSearchCV
    
    import pprint

    with open(train, 'rb') as csvfile:
        data=np.array(list(csv.reader(csvfile))).astype(float)
    with open(test, 'rb') as csvfile:
        data2=np.array(list(csv.reader(csvfile))).astype(float)
    
    num_dim= len(data[0])-2

    x_train = data[::, 1:-1]
    y_train = data[::, -1]
    x_test = data2[::, 1:]
    print y_train
    print 'data read'
    

    X, y = x_train, y_train
    Y=y

    from sklearn.ensemble import GradientBoostingClassifier
    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,
        max_depth=1, random_state=0).fit(x_train, y_train)

    from sklearn.lda import LDA
    clf = LDA()

    ##88.4
    #from sklearn.ensemble import RandomForestClassifier
    #clf = RandomForestClassifier()

    ##70% ish
    #from sklearn.cluster import KMeans
    #clf = KMeans(n_clusters=2)
    
    
    

    #clf.score(x_test, y_test)      
    #scores = cross_val_score(clf, X, y)


    ## gridsearch # Split the dataset in two equal parts
    ## gridsearch X_train, X_test, y_train, y_test = train_test_split(
    ## gridsearch     X, y, test_size=0.5, random_state=0)

    ## gridsearch # Set the parameters by cross-validation
    ## gridsearch tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4], 'C': [.0001,1, 10, 100, 1000]},
    ## gridsearch                     {'kernel': ['poly'], 'C': [1, 10, 100, 1000], 'degree':[2,3,4]},
    ## gridsearch                     {'kernel': ['linear'], 'C': [.0001,.01, 1, 10, 100, 1000]}]

    ## gridsearch scores = ['precision', 'recall']

    ## gridsearch for score in scores:
    ## gridsearch     print("# Tuning hyper-parameters for %s" % score)
    ## gridsearch     print()

    ## gridsearch     clf = GridSearchCV(SVC(C=1), tuned_parameters, cv=5, scoring=score)
    ## gridsearch     clf.fit(X_train, y_train)

    ## gridsearch     print("Best parameters set found on development set:")
    ## gridsearch     print()
    ## gridsearch     print(clf.best_estimator_)
    ## gridsearch     print()
    ## gridsearch     print("Grid scores on development set:")
    ## gridsearch     print()
    ## gridsearch     for params, mean_score, scores in clf.grid_scores_:
    ## gridsearch         print("%0.3f (+/-%0.03f) for %r"
    ## gridsearch               % (mean_score, scores.std() / 2, params))
    ## gridsearch     print()

    ## gridsearch     print("Detailed classification report:")
    ## gridsearch     print()
    ## gridsearch     print("The model is trained on the full development set.")
    ## gridsearch     print("The scores are computed on the full evaluation set.")
    ## gridsearch     print()
    ## gridsearch     y_true, y_pred = y_test, clf.predict(X_test)
    ## gridsearch     print(classification_report(y_true, y_pred))
    ## gridsearch     print()

    ## gridsearch sys.exit()
    from sklearn.ensemble import AdaBoostClassifier
    from sklearn.ensemble import GradientBoostingClassifier
    for C in [1,3,5,10]:

        ##winner so far! 2/10/15
        #clf = AdaBoostClassifier(n_estimators=1000, learning_rate=C)

        clf = GradientBoostingClassifier(n_estimators=1000, learning_rate=1.0,
            max_depth=C, random_state=0)

        X1 = x_train
        results_to_num = y_train

        #clf = svm.LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True,
        #intercept_scaling=1, loss='l2', multi_class='ovr', penalty='l2',
        #random_state=None, tol=C, verbose=0)
        
        #clf = linear_model.Lasso(alpha=C, copy_X=True, fit_intercept=True, max_iter=1000,
        #   normalize=False, positive=False, precompute='auto', tol=0.0001,
        #   warm_start=False)
        
        #clf = tree.DecisionTreeClassifier() #no winner even with 83 percent

        #86%
        #clf = tree.DecisionTreeRegressor(random_state=0)
        #cross_val_score(clf, X1, results_to_num, cv=10)

        #clf = ExtraTreesClassifier()
        #print 'fitting data 1'
        #x_new   = clf.fit(X1, y_train).transform(X1)
        #x_test2 = clf.fit(X1, y_train).transform(x_test)
        #print x_new[0]
        #print x_test[0]

        #print x_test2[0]
        #
        #
        #clf2 = ExtraTreesClassifier()
        #new   = clf2.fit(x_new, y_train)

        #X, y = x_train, y_train

        #clf = DecisionTreeClassifier(max_depth=None, min_samples_split=3,
        #    random_state=0)
        #scores = cross_val_score(clf, X, y)
        #print scores.mean()                             
        
        #clf = ExtraTreesClassifier(n_estimators=30, max_depth=None,
        #    min_samples_split=C, random_state=0)
        #scores = cross_val_score(clf, X, y)
        #print scores.mean()

        #clf = RandomForestClassifier(n_estimators=30, max_depth=None,
        #    min_samples_split=C, random_state=0)
        #scores = cross_val_score(clf, X, y)
        #print scores.mean()                             
        
        ##### previous clf = svm.LinearSVC(
        ##### previous         #loss='l1',
        ##### previous         #penalty='l1',
        ##### previous         #dual=False,
        ##### previous         fit_intercept=False,
        ##### previous         C=.0001)


        
        #from sklearn.preprocessing import scale
        #from sklearn.preprocessing import normalize
        #X = normalize(X, norm='l2')
        #for C in [.0001,.00015,.001,.01,1,10,100]:
        #    clf = linear_model.LogisticRegression(C=C)
        #clf = svm.SVC(C=1e-5, #rbf mol
        #          kernel='poly',
        #          gamma=.01,
        #          degree=2,
        #          #class_weight='auto',
        #          #max_iter=-1,
        #          #probability=False,
        #          #random_state=None,
        #          #shrinking=True,
        #          #tol=0.001,
        #          cache_size=2000,
        #          verbose=False)


        scores = cross_val_score(clf, X, y)
        print scores.mean(), ' for C = ', C

        print 'fitting data 1'
        clf.fit(X, Y)

        print 'predicting results'
        G_train = clf.predict(x_train)
        G_test = clf.predict(x_test)
        #for neural net G_train = clf.score_samples(x_train)
        #for neural net G_test = clf.score_samples(x_test)

        train_error = get_error(G_train, y_train)
        print 'train_error ', train_error

        tally = 0
        f = open("output_best_crossval_%s.csv" % C, "w")
        f.write('Id,Prediction\n')
        for i in xrange(len(x_test)):
            if G_test[i]==0: tally+=1
            f.write('%s,'% (i+1))
            f.write('%s\n'% G_test[i])
            
        f.close()
        print 'full classified ', tally/float(len(x_test)), '% as non-recession for C=', C

        


        
        #clf = svm.SVC(C=1.0, #rbf mol
        #          cache_size=200,
        #          class_weight=None,
        #          coef0=0.0,
        #          degree=C,
        #          gamma=0.0,
        #          kernel='rbf',
        #          max_iter=-1,
        #          probability=False,
        #          random_state=None,
        #          shrinking=True,
        #          tol=0.001,
        #          verbose=False)

        ##current winner
        ##run svm over the sparse set
        #clf2 = svm.SVC(
        #        kernel='poly',
        #        C=1,
        #        degree=3,
        #        shrinking=False,
        #        gamma=1,
        #        coef0=1)

        #print 'fitting data 1'
        ##clf.fit(X1, results_to_num)
        #print 'fitting data 2'




        #print 'predicting results for sparse'
        #clf2.fit(x_sparse_train, results_to_num)
        #G_train = clf2.predict(x_sparse_train)
        #G_test = clf2.predict(x_sparse_test)

        #train_error = get_error(G_train, y_train)
        #print 'train_error ', train_error

        #tally = 0
        #f = open("output_decision_tree_sparse.csv", "w")
        #f.write('Id,Prediction\n')
        #for i in xrange(len(x_test)):
        #    if G_test[i]==0: tally+=1
        #    f.write('%s,'% (i+1))
        #    f.write('%s\n'% G_test[i])
        #f.close()
        #print 'Sparse classified ', tally/float(len(x_test)), '% as non-recession for C=', C

        #used for linear_model.Lasso
        #f = open("coefs_coef_%s" % C, "w")
        #f.write('%s' % clf.coef_)
        #print('wrote coef file to coefs_coef_%s' % C)
        #f.close()
        #print(clf.intercept_)

        #used for poly svm
        #print 'print(len(clf.dual_coef_))'
        #print(len(clf.dual_coef_))
        #print 'print(len(clf.support_vectors_))'
        #print(len(clf.support_vectors_))



    
if __name__ == '__main__':
    print('original')
    demo('kaggle_train_wc.csv','kaggle_test_wc.csv')
    #print('pruned')
    #demo('dave_train_prune.csv','dave_test_prune.csv')
