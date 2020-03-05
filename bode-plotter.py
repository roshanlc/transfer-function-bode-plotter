#Author : Roshan Lamichhane
#github: roshanlc

from scipy import signal
import matplotlib.pyplot as plt

#--------- Transfer function

""" A transfer H(s)= [20(s+2) ]/[ s(s*s + 4*s + 16) ] 
    should be represented as H(s) = [20*s + 40]/[s^3 + 4 * s^2 + 16*s]
    i.e It should be in expanded form.

    Thus, num = coefficients of respective powers at numerator
    and, den =  coefficients of respective powers at denomenator

    For this case,
    num = [20,40]
    den = [1,4,16,0] #Go upto the power =0 
"""

num = [20,40] #coeff at numerator
den = [1,4,16,0] #coeff at denomenator
sys = signal.TransferFunction(num,den)


# -----------------------

w, mag, phase = signal.bode(sys)
plt.figure()
plt.title("Magnitude plot")
plt.grid(True,which='both') #It enables semi-log griding
plt.xlabel("[rad/s]")
plt.ylabel("[dB]")
plt.semilogx(w,mag) #Bode magnitude plot


plt.figure()
plt.grid(True,which='both') #It enables semi-log griding
plt.title("Phase plot")
plt.xlabel("[rad/s]")
plt.ylabel("[Degree]")
plt.semilogx(w,phase) #Bode phase plot


plt.show() #Display the graphs