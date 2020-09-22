from scipy.stats import wilcoxon as wcx
import numpy as np

# Wilcoxon signed-rank test: ############################################

# Execution time results:
euc2d = [0.00139451026917,
         0.00725555419922,
         0.0253758430481,
         0.0173027515411,
         0.0226023197174,
         0.0223479270935,
         0.0282788276672,
         0.0500631332397,
         0.0331380367279,
         0.0379276275635,
         0.070552110672,
         0.0790808200836]

man2d = [0.00124502182007,
         0.00663304328918,
         0.00998258590698,
         0.01060962677,
         0.0105848312378,
         0.0102360248566,
         0.0119721889496,
         0.0115096569061,
         0.0125303268433,
         0.0132446289062,
         0.0126175880432,
         0.0131969451904]

euc3d = [0.000442028045654,
         0.022136926651,
         0.0503289699554,
         0.03116106987,
         0.113832950592,
         0.0994560718536,
         0.104541063309,
         0.509521007538,
         0.303666830063,
         0.181762933731,
         0.621114969254,
         1.39144301414]

man3d = [0.000449895858765,
         0.00956606864929,
         0.0171241760254,
         0.0186679363251,
         0.0184979438782,
         0.0177659988403,
         0.019238948822,
         0.0188870429993,
         0.0186719894409,
         0.020350933075,
         0.0198798179626,
         0.0197379589081]

reduc = [0.00139451026917,
         0.00725555419922,
         0.0253758430481,
         0.0173027515411,
         0.0226023197174,
         0.0223479270935,
         0.0282788276672,
         0.0500631332397,
         0.0331380367279,
         0.0379276275635,
         0.070552110672,
         0.0790808200836]

origi = [0.0166418552399,
         0.118990659714,
         1.41100072861,
         0.698022842407,
         1.24974441528,
         1.88481593132,
         1.29890036583,
         4.14102673531,
         3.89638662338,
         2.04275345802,
         7.76353287697,
         8.89313721657]


# Comparison between 2D A* with Euclidean and Manhattan heuristics:     
stat, pvalue = wcx(euc2d, man2d)

print("Results for 2D A*: ")
print("Sum of the ranks: " + str(stat))
print("p_value = " + str(pvalue))
print("\n")

# Comparison between 3D A* with Euclidean and Manhattan heuristics:
stat, pvalue = wcx(euc3d, man3d)

print("Results for 3D A*: ")
print("Sum of the ranks: " + str(stat))
print("p_value = " + str(pvalue))
print("\n")

# Comparison between 2D A* with and without map reduction:
stat, pvalue = wcx(reduc, origi)

print("Results for reduced vs original maps: ")
print("Sum of the ranks: " + str(stat))
print("p_value = " + str(pvalue))
print("\n")

# Comparison between 2D and 3D A* with Euclidean heuristics:
stat, pvalue = wcx(euc2d, euc3d)

print("Results for A* with Euclidean: ")
print("Sum of the ranks: " + str(stat))
print("p_value = " + str(pvalue))
print("\n")

# Comparison between 2D and 3D A* with Manhattan heuristics:
stat, pvalue = wcx(man2d, man3d)

print("Results for A* with Manhattan: ")
print("Sum of the ranks: " + str(stat))
print("p_value = " + str(pvalue))
print("\n")


#########################################################################

