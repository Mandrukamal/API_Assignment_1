import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# Set default theme
sns.set_theme()

# Import your data into Python
df = pd.read_csv("/Users/mkmac/Documents/API_assignment_1/data/ImputedStudentPerformanceFactors.csv")
print(df.index)

# 1.1 Box Plot
sns.boxplot(df['Hours_Studied'])
plt.title('1. Box Plot of Hours_Studied')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/boxplot_hours_studied.png")
plt.show()

# 1.2 Strip Plot
sns.stripplot(y=df['Hours_Studied'])
plt.title('2. Strip Plot of Hours_Studied')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/stripplot_hours_studied.png")
plt.show()

# 1.3 Swarm Plot
sns.swarmplot(x=df['Hours_Studied'])
plt.title('3. Swarm Plot of Hours_Studied')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/swarmplot_hours_studied.png")
plt.show()

sns.swarmplot(x=df['Attendance'])
plt.title('4. Swarm Plot of Attendance')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/swarmplot_attendance.png")
plt.show()

# 1.4 Histogram
plt.hist(df['Hours_Studied'])
plt.title('5. Histogram of Hours_Studied')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/histogram_hours_studied.png")
plt.show()

# 1.5 Distplot
sns.distplot(df['Hours_Studied'], kde=False, color='blue', bins=5)
plt.title('6. Dist Plot of Hours_Studied with 5 bins')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/distplot_hours_studied.png")
plt.show()

# 1.6 Countplot
sns.countplot(df['Gender'])
plt.title('7. Count Plot of Gender (Categorical)')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/countplot_gender.png")
plt.show()

# 2.1 Boxplot for Bivariate Analysis
sns.boxplot(x=df['Exam_Score'], y=df['Attendance'], data=df)
plt.title('8. Box Plot of Exam_Score vs Attendance')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/boxplot_exam_score_attendance.png")
plt.show()

# 2.2 Scatter Plot
sns.scatterplot(x=df['Attendance'], y=df['Hours_Studied'])
plt.title('9. Scatter Plot of Hours_Studied vs Attendance')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/scatterplot_hours_studied_attendance.png")
plt.show()

sns.scatterplot(x=df['Attendance'], y=df['Hours_Studied'], hue=df['Exam_Score'])
plt.title('10. Scatter Plot of Hours_Studied vs Attendance vs Exam_Score')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/scatterplot_hours_studied_attendance_exam_score.png")
plt.show()

# 2.3 FacetGrid for Gender vs Extracurricular_Activities
g = sns.FacetGrid(df, col="Gender", height=6.5, aspect=.85)
g.map(sns.histplot, "Extracurricular_Activities")
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/facetgrid_gender_extracurricular.png")
plt.show()

# Multivariate Analysis - FacetGrid
g = sns.FacetGrid(df, col="Extracurricular_Activities", hue="Gender", margin_titles=True, height=6.5, aspect=.85)
g.map(sns.histplot, "Hours_Studied")
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/facetgrid_hours_studied_extracurricular.png")
plt.show()

# 2.4 lmplot
sns.lmplot(data=df, x="Hours_Studied", y="Extracurricular_Activities", hue="Gender")
plt.title('13. lmplot of Hours_Studied vs Extracurricular_Activities vs Gender')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/lmplot_hours_studied_extracurricular.png")
plt.show()

sns.lmplot(data=df, x="Hours_Studied", y="Attendance", hue="Gender")
plt.title('14. lmplot of Hours_Studied vs Attendance vs Gender')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/lmplot_hours_studied_attendance_gender.png")
plt.show()

sns.lmplot(data=df, x="Attendance", y="Hours_Studied", hue="Extracurricular_Activities")
plt.title('15. lmplot of Hours_Studied vs Attendance vs Extracurricular Activities')
plt.savefig("/Users/mkmac/Documents/API_assignment_1/output/visualization_plots/lmplot_attendance_hours_studied_extracurricular.png")
plt.show()