import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures


def non_linear_regression(regression_data):
    X = np.array(range(len(regression_data.index)))
    X = X[:, np.newaxis]
    y = np.array(regression_data.TotalDateSinceMidnight)
    y = y[:, np.newaxis]

    poly_reg = PolynomialFeatures(degree=5)
    X_poly = poly_reg.fit_transform(X)
    pol_reg = LinearRegression()
    pol_reg.fit(X_poly, y)
    plot_linear(X, y)
    plot_regression(X, y, poly_reg, pol_reg, X_poly, regression_data)
    print("\n Le nombre de vélos prédit le vendredi 02 Avril entre 00h et 09h est  : ")
    print(pol_reg.predict(poly_reg.fit_transform([[len(X)]])))


def plot_regression(X, y, poly_reg, pol_reg, X_poly, regression_data):
    plt.figure(figsize=(20, 5))
    plt.scatter(X, y, color='blue')
    plt.plot(X, pol_reg.predict(poly_reg.fit_transform(X)), color='orange', label="Régression polynomiale")
    plt.title("Représentation de l'intensité du trafic les vendredis entre 00h et 09h")
    plt.xlabel('Vendredi')
    plt.ylabel('Nombre de vélos')
    plt.text(0, 500,
             'R2 = ' + str(round(r_squared(X_poly, y, pol_reg) * 100, 2)))
    plt.legend()
    plt.show()


def plot_linear(x, y,):
    model = LinearRegression()
    model.fit(x, y)
    y_pred = model.predict(x)
    plt.figure(figsize=(20, 5))
    plt.scatter(x, y, s=10)
    plt.plot(x, y_pred, color='green', label='Régression linéaire')
    plt.title("Représentation de l'intensité du trafic les vendredis entre 00h et 09h")
    plt.xlabel('Vendredi')
    plt.ylabel('Nombre de vélos')
    plt.legend()



def r_squared(X_poly, y, pol_reg):
    pol_reg
    return pol_reg.score(X_poly, y)
