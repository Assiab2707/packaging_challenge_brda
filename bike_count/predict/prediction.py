import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures


def non_linear_regression(regression_data):
    X = np.array(range(len(regression_data.index)))
    X = X[:, np.newaxis]
    y = np.array(regression_data.TotalDateSinceMidnight)
    y = y[:, np.newaxis]

    poly_reg = PolynomialFeatures(degree=7)
    X_poly = poly_reg.fit_transform(X)
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, y)
    plot_regression(X, y, poly_reg, pol_reg, X_poly, regression_data)
    print("\n Le nombre de vélos prédit le vendredi 02 Avril entre 00h \
           et 09h est  : ")
    print(pol_reg.predict(poly_reg.fit_transform([[len(X)]])))


# Visualizing the Polymonial Regression results
def plot_regression(X, y, poly_reg, pol_reg, X_poly, regression_data):
    plt.figure(figsize=(20, 5))
    plt.scatter(X, y, color='blue')
    plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='orange')
    plt.title('Representation du nombre de vélos les Vendredi \
               entre 00h et 09h')
    plt.xlabel('Vendredi')
    plt.ylabel('Nombre de vélos')
    plt.text(0, 500,
             'R2 = ' + str(round(r_squared(X_poly, y, pol_reg) * 100, 2)))
    plt.show()
    plt.savefig('regression_plot.pdf')  


def r_squared(X_poly, y, pol_reg):
    return pol_reg.score(X_poly, y)
