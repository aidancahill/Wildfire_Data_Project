Wildfire Data Project (EDA)

Software Project Specification

Aidan Cahill
3/11/2022

Introduction

The data source that is used for this project was a publicly disclosed source through this link. 
https://gis.data.ca.gov/datasets/CALFIRE-Forestry::california-fire-perimeters-all/about This data 
is published by CAL FIRE (California Department of Forestry) and is all of CAL FIREs fire history. 
The software created around this data was an exploratory data analysis project that explored the data 
through three main visualizations. Apart from the visualizations the software explores the idea of risk 
and analyzing risk from wildfires.

Purpose

The purpose of this software was first to explore the wildfire data and see if there could be any insights 
that could be gained other than already conclusive ideals about wildfires. Second from the insights gained
could there be any further use of the data as to create a functional program that accomplishes a task? 
Exploration of data can be useful to some sense but once some knowledge about the data is gained, can that 
knowledge be used for actionable decisions. So the main purpose would then be to extrapolate the data so that 
insights can be used to make actionable decisions about wildfires and their risk. 

Intended Audience

The audience of this software is intended to be firefighting resources, wildfire risk analysts, wildfire 
mitigation groups, insurance risk analysts, and anyone looking to gain insight into the data, its visualizations, 
and the risk assessment software. 

Intended Use

The use of the software is mainly the risk assessment calculator which takes input from the user a number 1-19 to analyze 
either the overall risk or the risk associated with a certain month of a specific source of fire ignition type such as 
lightning, powerline, vehicle, ect

Assumptions

First some definitions that are frequently used throughout the software, and the documentation surrounding the software. 
Ignition source/ignition type is defined as the source that ignited the fire or the specific event/physical occurrence that 
caused the fire to start. Risk is used and must be defined as the possibility of loss, in particular loss of vegetation due 
to the combustion of fire, and is based on four levels of risk: low, moderate, high, and extreme. A risk matrix is a tool that 
assists the decision-making process. It takes into consideration the category of probability, or likelihood, against the category 
of consequence severity. Risk is assessed in the software using the matrix by describing the likelihood that a particular fire 
ignition source would happen out of 21,318 fires, and the category of consequence severity is described by the average fire size 
of that particular fire ignition source. Within the software the term df is used and refers to a pandas class known as a dataframe. 

Dependencies

This software is dependent mostly on the data and its validity, although the data is sparse in terms of numerical features, it is 
the most comprehensive set of fires from 1950-2021. Other data sets are not as consistent in terms of features that are agreed to 
be useful. The software is also dependent upon a competent user that needs to run the program and enter specific commands into the 
console when necessary. Other dependents are the python libraries that are used in the software for ease of use. These libraries are 
pandas, matplotlib, and numpy in the order of their importance from most important to least. 
 
Scope

The scope of the software can first be described as the scope of the data that the software uses for its insights. 
So the data is specifically only California wildfire data and not data from other states. The data does not include 
information regarding the time from Sep 24, 2021 until present. As well it does not include any data earlier than the year 
1950. The data contains seventeen features YEAR describes the year the fire started, STATE describes the state the fire originated, 
1951. AGENCY describes the agency or territory the fire originated (public, state, or private land), UNIT_ID is the the id of the 
1952. resource taking control of the fires suppression, FIRE_NAME is the english lexicon used to identify the fire usually is similar 
1953. to its origin location, INC_NUM is the number that is assigned to the fire via the governing agency taking control, ALARM_DATE 
1954. is the date and time associated with the broadcast over the radio of emergency traffic regarding the fire, CONT_DATE is the take 
1955. of containment or the date the fire is surrounded by suppression line and mopped up(extinguishing hot spots within the fire line, 
1956. CAUSE is a number 1-19 associated with a certain or event that explains what perpetuated the fire, COMMENTS is any comments from 
1957. the governing agency about the fire, C_METHOD is a number associated with the suppression type being used on the fire (aerial, ground, ect), 
1958. OBJECTIVE describes the end state that fire should be in for the suppression of the fire to be called completed, FIRE_NUM is an identifying 
1959. number that all fires are assigned so that a unique identifier is used for each fire, SHAPE_AREA describes the geometric polygonal shape of 
1960. the fire, SHAPE_LENGTH is the length of all sides of the polygon added up. The encompassing scope of the program explores this data 
1961. specifically with 21,318 records to gain its insights. 
1962. 
Overall Description

The description of the software is the components of its makeup and how those components are used in order to gain value. 
Those components or rather functions  in order in which they appear in the program are as follows. First the dataset is read into 
an overall encompassing dataframe, that data frame is broken into smaller data frames based on the ignition source of the fire. 
The function which comes first is total_acres_burned and is one that calculates the total acres burned by each ignition source, and 
plots that data into a bar graph.The second function named number_of_fires calculates how many fires happened in each respective from 
Jan - Dec 1950-2021 and then outputs a bar graph showing the data.  Next a function calculates the average fire size average_acres_burned 
by a particular ignition source, and plots that again on a bar graph. The fourth and largest function of the software breaks the subset of 
data frames that describe each ignition source and the associated fires is broken down even further into dataframes that are composed of the 
months of the year in which those ignition sources happened. For example all lightning fires that happened in january from 1950-2021 are 
collected in a dataframe, this is extrapolated by every ignition source and the months of that ignition source happened. From these subsets 
of the ignition source dataframe the program function outputs the greatest fire ignition source count by month of the year. The last function 
of the software is risk_calculator that calculates the risk of an ignition source overall and the risk that ignition source has within a particular 
month of the year. It does this by assessing the likelihood of that fire occurring overall and within a specific month and the average 
acres burned by that fire ignition source overall and within a particular month. Either the overall risk level or the risk level within 
that month is gained by traversing the risk risk matrix by finding the average acres burned on the x axis and is a range, then finding 
the likelihood of occurrence on the y axis and coming to the cross section of those two data points which will yield a number or the 
associated risk 1-16(1-3 low risk, 4-6 moderate risk, 8-10 high risk, and 12-16 extreme risk). The user is asked to input the specific 
number that correlates to a month that needs to be assessed in terms of risk or the overall risk. Within the main software source code 
the user is asked to input a number that correlates to the ignition source that needs to be assessed and calls the risk calculator with 
the arguments of a pandas dataframe that is the ignition source dataframe. 

Conclusion

Upon visualizing the total acres burned by ignition source and comparing that to average fire size per ignition source it became 
evident that unidentified fires had the highest total acres burned but the average fire size of an unidentified ignition source was 
relatively low. Following that knowledge a risky ignition source can be categorized as one that has on the overall time horizon of 
the data has burned a substantial amount of acres in total but its average fire size is more than 3000 acres. Using this logic lightning 
fires would bear the most consequence in severity. I think this can be explained by the inclement weather that comes along with lightning. 
Strong winds and storm fronts are often associated with lightning so a strike ignites a fire the winds then moves this fire at a rapid rate, 
paired with many lightning strikes and small bodies of fire come together as a large moving mass of fire driven by wind. Once these insights 
were gleaned from the visualizations it became apparent that the software needed a cherry on top so to speak, something that would help the 
decision making process based on the type of ignition source and the time of year. So the risk calculator was then assembled to identify risk 
by each ignition source and the time of year the specified ignition source happened to come to a conclusion of the risk level that fire would 
pose to life, property, and land in which the fire originates. 

