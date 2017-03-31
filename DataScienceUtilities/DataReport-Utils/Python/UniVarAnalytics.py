import matplotlib.pyplot as plt
import scipy.stats as stats

class TargetAnalytics():
	ReportedVariables = []
	@staticmethod
	def custom_barplot(df,filename='',col1='', Export=False):
		f, (ax0,ax1) = plt.subplots(1, 2)
		df[col1].value_counts().plot(ax=ax0, kind='bar')
		ax0.set_title('Bar Plot of {}'.format(col1))
		df[col1].value_counts().plot(ax=ax1, kind='pie')
		ax1.set_title('Pie Chart of {}'.format(col1))
		#return f
	
class NumericAnalytics():
	@staticmethod
	def shapiro_test(x):
		p_val = round(stats.shapiro(x)[1],6)
		status = 'passed'
		color = 'blue'
		if p_val < 0.05:
			status = 'failed'
			color = 'red'
		return status, color, p_val
	
	@staticmethod
	def custom_barplot(df, filename='', col1='', Export=False):
		fig, axes = plt.subplots(2,2)
		axes = axes.reshape(-1)
	#     print df[col].describe()
		df[col1].plot(ax=axes[0], kind='hist')
		axes[0].set_title('Histogram of {}'.format(col1))
		df[col1].plot(ax=axes[1], kind='kde')
		axes[1].set_title('Density Plot of {}'.format(col1))
		ax3 = plt.subplot(223)
		stats.probplot(df[col1], plot=plt)
		axes[2].set_title('QQ Plot of {}'.format(col1))
		df[col1].plot(ax=axes[3], kind='box')
		axes[3].set_title('Box Plot of {}'.format(col1))
		status, color, p_val = NumericAnalytics.shapiro_test(df[col1])
		fig.suptitle('Normality test for {} {} (p_value = {})'.format(col1, status, round(p_val, 6)), color=color, fontsize=12)

	#     return f
	
class CategoricAnalytics():
	@staticmethod
	def custom_barplot(df, filename='', col1='', Export=False):
		f, (ax0,ax1) = plt.subplots(1,2)
		df[col1].value_counts().nlargest(10).plot(ax=ax0, kind='bar')
		ax0.set_xlabel(col1)
		ax0.set_title('Bar chart of {}'.format(col1))
		df[col1].value_counts().nlargest(10).plot(ax=ax1, kind='pie')
		ax1.set_title('Pie chart of {}'.format(col1))
	#     return f
