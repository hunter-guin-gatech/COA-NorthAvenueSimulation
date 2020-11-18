# COA-NorthAvenueSimulation

Date: 6 July 2020

Code for North Ave Digital Twin 

Folder contains Python 3.7 code for Vissim COM implmentation of North Ave Simulation in file "COM_Script_v5_15Dec2019_rbcedit_restart.py". Code enables Vissim 9.00 simulation model to be driven using real-time voluem and signal indication data of a Smart Corridor. This model is impelemented for North Ave Smart Corridor in Atlanta, Georgia.

The model also pushes simulation output data (vehicle trajectory information) and signal indications to visulaizations module using Flask (code present in file - "LiveConnectingScript_2-post.py" and "LiveConnectingScript_postsignals.py"). Visulaization module visualizes traffic and environmental performance indices of the corridor on the website. 

The energy and emissions estimation calculation process and code is decribed in "KPI_Estimation_From_Trajectory.ipynb" file.

