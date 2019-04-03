# Pandas module is used for data manipulation and analysis.
# i)Tabular data with heterogeneously-typed columns.
# ii)Ordered and unordered time  series data.
# iii)Arbitary matrix data with row and column labels
# iv)Any other form of observational /Statistical data sets.The data actually need not be labeled at all to be placed into a pandas data structure.
################################################################################
 # 1 Converting dictionary into a tabular form
################################################################################
# import pandas as pd
# XYZ_web={"Day":[1,2,3,4,5,6],"Visitors":[1000,200,145,4566,656,663],"Bounce_rate":[425,52,4,52,656,466]}
# df = pd.DataFrame(XYZ_web)
# print(df)
################################################################################
# Pandas Operations
# i)Slicing the DataFrame
# ii)changing the index
# iii)Data Conversion
# iv)Joining and Merging
# v)Concatenation
# vi)Changing the column headers
# ################################################################################
# SLICING THE DATAFRAME
################################################################################
# print(pf.head(2))
#first two rows and for bottom  two rows
# print(pf.tail(2))
################################################################################
# MERGING operation is used to combine on the bases on columns of the data frame
################################################################################
# import pandas as pd
# df1 = pd.DataFrame({"HPI":[80,90,70,60],"int_rate":[2,1,2,3],"ind_GDP":[30,40,50,55]},index =[2001,2002,2003,2004])
# df2 = pd.DataFrame({"HPI":[80,90,70,60],"int_rate":[1,2,3,4],"ind_GDP":[55,56,60,62]}, index =[2005,2006,2007,2008])
# merge = pd.merge(df1,df2) #common the column use on= "mention the column the name which you wanna do"
# print(merge)
# ###############################################################################
#Joining operation is similar to the merging and combine on bases of  the indexvalue
################################################################################
# import pandas as pd
# df1 = pd.DataFrame({"int_rate":[2,1,2,3],"IND_GDP":[50,45,45,67]}, index = [2001,2002,2003,2004])
# df2 = pd.DataFrame({"Low_tier_HPI":[50,45,67,34],"Unermployment":[1,3,5,6]}, index = [2001,2003,2004,2004])
# joined = df1.join(df2)
# print(joined)
################################################################################
#Changing index and column headers
################################################################################
# import pandas as pd
# df = pd.DataFrame({"day":[1,2,3,4],"visitors":[200,100,123,212],"Bounce_rate":[20,25,41,10]})
# df.set_index("day",inplace=True)
# print(df)
################################################################################
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import style
# style.use("fivethirtyeight")
# df = pd.DataFrame({"day":[1,2,3,4],"visitors":[200,100,230,133],"Bounce_rate":[20,45,60,10]})
# df.set_index("day",inplace=True)
# df.plot()
# plt.show()
##################################################################################
#Changing the name of a column
# import pandas as pd
# # import matplotlib.pyplot as plt
# # from matplotlib import style
# # style.use("fivethirtyeight")
# df = pd.DataFrame({"day":[1,2,3,4],"visitors":[200,100,230,133],"Bounce_rate":[20,45,60,10]})
# # df.set_index("day",inplace=True)
# # df.plot()
# # plt.show()
#
# df = df.rename(columns={"visitors":"users"})
# print(df)
################################################################################
#Concatenation is adding a column or a row to the given table
################################################################################
# import pandas as pd
# df1 = pd.DataFrame({"HPI":[80,90,70,60],"int_rate":[2,1,2,3],"ind_GDP":[30,40,50,55]},index =[2001,2002,2003,2004])
# df2 = pd.DataFrame({"HPI":[80,90,70,60],"int_rate":[1,2,3,4],"ind_GDP":[55,56,60,62]}, index =[2005,2006,2007,2008])
# Concat = pd.concat([df1,df2])
# print(Concat)
################################################################################
# Data munging used to convert one data format to other data format.
################################################################################
#-----------------------------------------------
###############################################################################
#Statistics
###############################################################################
# There are four main functions will be there in Statistics
# i) Mean  #Average of the list is called Mean
# ii)Median # Middle value of a list is called Median ,if there are two middle values are there then its called lower Median and High Median
# iii)Mode  # Most repeted element in a list is called Mode
# iv)variance #
################################################################################
# Python for Hadoop : Pydoop
#Pydoop is a Python interface to Hadoop that allows you to write Map reduce applications and interact with HDFS in pure Python
