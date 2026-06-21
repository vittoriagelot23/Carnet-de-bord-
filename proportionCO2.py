import numpy as np
import matplotlib.pyplot as plt

def concentration_CO2(annee):
    """
    Calcule la concentration estimée en ppm pour une année donnée.
    Parameters
    ----------
    annee : int
        Année pour laquelle on souhaite estimer la concentration de CO2.

    Returns
    -------
    float
        Concentration estimée de CO2 en ppm.
    """

    if 1838 <= annee <= 1972:
        return 0.294 * annee - 262
    elif annee < 1838:
        return 278 # valeur moyenne avant l'ère industrielle
    else:
        return 1.9 * annee - 3430


def concentration_CO2_altitude(altitude): 
    """
    Estime la concentration, de CO2 en fonction de l'altitude.

    Parameters
    ----------
    altitude : float
        Altitude considérée.

    Returns
    -------
    float
        Concentration estimée de CO2 en ppm à cette altitude.
    """
    
    if 0 <= altitude <= 60:
        return 380 # valeur à basse altitude
    elif altitude > 132:
        return 0 #valeur à haute altitude
    else:
        return -5.26 * altitude + 736 #valeur avec la fonction affine
    
def coef_augmentation (concentration):
    """
    Calcule le coefficient d'augmentation de la concentration de CO2 par rapport à l'année de référence 2000.

    Parameters
    ----------
    concentration : float
        Concentration de CO2 pour une année donnée.

    Returns
    -------
    float
        Coefficient d'augmentation par rapport a l'année 2000.
    """
    ref = concentration_CO2(2000) #année de référence du graphique des altitudes
    coef = (concentration /ref)
    return coef


def augmentation_altitude(coef, altitude):
    """
    Ajuste la concentration de CO2 à une altitude donnée en utilisant le coefficient d'augmentation calculé auparavant.

    Parameters
    ----------
    coef : float
        Coefficient d'augmentation du CO2.

    altitude : float
        Altitude étudiée.

    Returns
    -------
    float
        Concentration estimée de CO2 prenant en compte à la fois l'année et l'altitude.
    """
    prop_altitude = concentration_CO2_altitude(altitude) #proportion de CO2 à une altitude donnée en
    prop_annee = prop_altitude * coef
    return prop_annee

prop = concentration_CO2(2026)
c=coef_augmentation(prop)
print (concentration_CO2_altitude(100))
print (augmentation_altitude(c,100))

