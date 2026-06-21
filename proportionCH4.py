def concentration_CH4(annee):
    """
    Calcule la concentration estimée en ppb pour une année donnée.
    Parameters
    ----------
    annee : int
        Année pour laquelle on souhaite estimer la concentration de CH4.

    Returns
    -------
    float
        Concentration estimée de CH4 en ppb.
    """
    if annee <=1786 :
        return 675
   
    else:
        return  5.07 * annee - 8.38 *(10**3)  
   
def concentration_CH4_altitude(altitude):
    """
    Estime la concentration, de CH4 en fonction de l'altitude.

    Parameters
    ----------
    altitude : float
        Altitude considérée.

    Returns
    -------
    float
        Concentration estimée de CH4 en ppb à cette altitude.
    """
    if  altitude < 9:
        return 1800   # valeur à basse altitude en ppb
   
    elif  9 <= altitude <= 45:
        return   -45.2 * altitude + 2190 #valeur à haute altitude
    else:
        return 100  #valeur avec la fonction affine
   
def coef_augmentation(concentration):
    """
    Calcule le coefficient d'augmentation de la concentration de CH4 par rapport à l'année de référence 2020.

    Parameters
    ----------
    concentration : float
        Concentration de CH4 pour une année donnée.

    Returns
    -------
    float
        Coefficient d'augmentation par rapport a l'année 2020.
    """
    ref = concentration_CH4(2020) #année de référence du graphique des altitudes
    coef = (concentration /ref)  
    return coef    

def augmentation_altitude(coef, altitude):
    """
    Ajuste la concentration de CO2 à une altitude donnée en utilisant le coefficient d'augmentation calculé auparavant.

    Parameters
    ----------
    coef : float
        Coefficient d'augmentation du CH4.

    altitude : float
        Altitude étudiée.

    Returns
    -------
    float
        Concentration estimée de CH4 prenant en compte à la fois l'année et l'altitude.
    """
    prop_altitude = concentration_CH4_altitude(altitude) #proportion de CH4 à une altitude donnée en 2020
    prop_annee = prop_altitude * coef
    return prop_annee

prop = concentration_CH4(2000)
c=coef_augmentation(prop)
print (concentration_CH4_altitude(20))
print (augmentation_altitude(c,20))
