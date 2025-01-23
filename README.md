# BRAPPED
## The Better and Upgraded Version of Spotify Wrapped<br>
#
**Purpose**
- To have more clarity than the original version of Spotify Wrapped.
- To allow users to interact with it.
# 
**Dataset**
- It contains the streaming history data, alongside the playlist information and artist segment(for more clarity over this head over to my medium articles).
- The original data source is in comple JSON object.
- This contains data till 18th November 2024(this is the first constraint)
#
### **Methodology**
#
**Tools and Libraries Used**
- Python
- Power BI
- Power Query
- pandas
- requests
- json
- dotenv
- pickle, etc.
#
**Analytical Technique Used**
- Descriptive Analytics
- Diaganostic Analytics
#
**WorkFlow**<br>
![](https://github.com/gauraVwrites/BRAPPED/blob/main/images/introImage.png)<br>
To start working on this dataset and reach my end goal of a fully functioning and interactive dashboard, I need to made sure that I've all the data that I need for this.<br>
Therefore I divided this project into several parts.
1. *Requirements Gathering*:<br>
In this part I've set my priorities regarding all the data points that I need, and then made and executed plans to achieve them.<br>
You can refer to these articles to get more deep understanding of it.<br>
[**How I created a BETTER version of Spotify Wrapped using Python and Power BI**](https://medium.com/p/74ec648f1f0c)<br>
[**Brapped: Requirements Gathering and Data Modelling (I)**](https://medium.com/p/1051bfc1b240)<br>
[**Brapped: Requirements Gathering and Data Modelling (II)**](https://medium.com/p/38e8de8a7524)<br>
[**Brapped: Requirements Gathering and Data Modelling (III)**](https://medium.com/p/04cc2ebcbf32)<br>
[**Brapped: Requirements Gathering and Data Modelling (IV)**](https://medium.com/p/4dde6f4d1fb1)<br>
2. *Data Modelling*:<br>
This is the part in which I've used pandas alongside Power Query to organize our data so that it's light and fast.<br>
You can refer to these articles to get more deep understanding of it.<br>
[**Brapped: Requirements Gathering and Data Modelling (V)**](https://medium.com/p/a0c604fbdabf)<br>
3. *Dashboarding*:<br>
This part is regading creating features for our dashboards, that will make it an advanced and more interactive version of Spotify's Original Wrapped.<br>
You can refer to my article regarding this.<br>
[**Brapped: Dashboarding and DAX logic (final part with project video)**](https://medium.com/p/7fdd1f6c8894)<br>
I've also created some videos regarding these topics:<br>
Both of these videos contains my voiceover, I've tried to implement same logic live(please plugin your headphones, for more clear voice, and sped up video as per your comfort).<br>
**API calls:** [**Part1**](https://youtu.be/Cy8DPKAO3U4?si=cnbi0Q1dwGDiZgv5) [**Part2**](https://youtu.be/JoBmyjuOTDk?si=ACpG0YL6Enny5y6h)<br>
**Dashboard Presentation and DAX logic(for visual building):** [**Both Parts Combined**](https://youtu.be/Oegr4tQ88cA?si=J9zDIAunkx7KLiCp)<br>
#
**Challenges**<br>
![](https://github.com/gauraVwrites/BRAPPED/blob/main/images/dataCluster.png)<br>
- To create a more dynamic and interactive dashboard, I was short on overall data.
- The existing data contained errors that were hard to find(refer to articles, if you want to know more).
- Initial data model was heavy and for some reasons relationships were of type Many-To-Many instead of One-To-Many.
- The data source was in complex JSON object, that was pretty hard to understand, and much more at granular level.
#
**Solutions**<br>
![](https://github.com/gauraVwrites/BRAPPED/blob/main/images/cleanDataModel.png)<br>
There's no definite solution to the problems I encountered in this project. But inshort these are some solutions I came up with:<br>
- Used Spotify's Web API, to get more data.
- Used advanced logics to find the errors in Pandas.
- Used SET logic to create primary keys in my dataframes.
- Took help from JSON beautifiers and API documentaion, to make meaning of data.
#
This is the end of this project refer to this file for understanding the data modelling in Python using pandas. [MyJupyterNotebook](https://github.com/gauraVwrites/BRAPPED/blob/main/SpotifyDataModelling.ipynb), for understanding the logic behind API calls refer to this [PythonFile](https://github.com/gauraVwrites/BRAPPED/blob/main/main.py)<br>
Thanks for sticking to the very end, see you soon with a more unique project just like this one.
