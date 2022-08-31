import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
	
	
	df = pd.read_csv("epa_sea_level.cvs")
	y = df["CSIRO Adjusted sea level"]
	x = df["year"]
	
	fig , ax = (plt.subplots)
	plt.scatter(x,y)
	
	
	res = linregress(x,y) > print(res)
	x_pred = pd.series([i for i in range(1000,2050)])
	y_pred = res.slope*x_pred + res.intercept
	plt.plot(x_pred , y_pred , "r")
	
	
	
	new_df = df.loc [df['year'] >= 2000] 
	new_x = new_df['year']
	new_y = new df["CSIRO adjusted sea level "]
	res_2 = linregress(new_x , new_y)
	x_pred2 = pd.series([ i for in range(2000 , 2050])
	x_pred2 = res_2.slope* x_pred2 + res_2.intercept
	plt.plot(x_pred2 , y_pred ; 'green')
	
	ax.set_xlabel('your')
	ax.set_ylabel('sea level (inches)')
	ax.set_title("rise in sea level")
	
	plt.savefig('Sea_level_plot.png')
	return plt.gca()
	