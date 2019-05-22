import win32com.client
sdf = win32com.client.Dispatch("Scripting.FileSystemObject")
d = sdf.GetDrive(sdf.GetDriveName(sdf.GetAbsolutePathName("C:/")))
sum = int(d.TotalSize / 1024) | d.SerialNumber | 939881100
id = sum + 5*100 + 0*10 + 7

regfile = r'''Windows Registry Editor Version 5.00

[HKEY_USERS\S-1-5-93-2-1\SOFTWARE\VB and VBA Program Settings\C:\Program Files (x86)\HEC\HEC-RAS\5.0.7\ras.exe]

[HKEY_USERS\S-1-5-93-2-1\SOFTWARE\VB and VBA Program Settings\C:\Program Files (x86)\HEC\HEC-RAS\5.0.7\ras.exe\Form Position]
"RAS"="1935,1545,2147483647,2147483647"
"DSS Export"="2147483647,2147483647,2147483647,2147483647"
"Open Dialog"="2147483647,2147483647,2147483647,2147483647"
"Profile Dialog"="2147483647,2147483647,2147483647,2147483647"
"General Dialog"="2147483647,2147483647,2147483647,2147483647"
"HTML Dialog"="2147483647,2147483647,2147483647,2147483647"
"Steady Data"="2147483647,2147483647,2147483647,2147483647"
"Boundary Conditions"="2147483647,2147483647,2147483647,2147483647"
"Steady Set"="2147483647,2147483647,2147483647,2147483647"
"Observed WS"="2147483647,2147483647,2147483647,2147483647"
"Observed RC"="2147483647,2147483647,2147483647,2147483647"
"Gate Opening"="2147483647,2147483647,2147483647,2147483647"
"Gate Optimize"="2147483647,2147483647,2147483647,2147483647"
"Initial Splits"="2147483647,2147483647,2147483647,2147483647"
"DSS Flow Conn"="2147483647,2147483647,2147483647,2147483647"
"DSS Flow Import"="2147483647,2147483647,2147483647,2147483647"
"DSS Plot"="2147483647,2147483647,2147483647,2147483647"
"SF Storage Area Elev"="2147483647,2147483647,2147483647,2147483647"
"SF OutletTS"="2147483647,2147483647,2147483647,2147483647"
"UnSteady Data"="2147483647,2147483647,2147483647,2147483647"
"UnSteady Boundary"="2147483647,2147483647,2147483647,2147483647"
"IC Stages"="2147483647,2147483647,2147483647,2147483647"
"Observed DSS Data"="2147483647,2147483647,2147483647,2147483647"
"Unsteady Observed RC"="2147483647,2147483647,2147483647,2147483647"
"Observed HWM Data"="2147483647,2147483647,2147483647,2147483647"
"Unsteady QMinMult"="2147483647,2147483647,2147483647,2147483647"
"Unsteady Rule Editor"="2147483647,2147483647,2147483647,2147483647"
"Unsteady DSS Table"="2147483647,2147483647,2147483647,2147483647"
"Unsteady DSS Path Picker"="2147483647,2147483647,2147483647,2147483647"
"WQ Data"="2147483647,2147483647,2147483647,2147483647"
"WQ Data TS"="2147483647,2147483647,2147483647,2147483647"
"WQ Data Analysis"="2147483647,2147483647,2147483647,2147483647"
"WQ Data NSMII"="2147483647,2147483647,2147483647,2147483647"
"WQ Data TDG"="2147483647,2147483647,2147483647,2147483647"
"Steady Analysis"="8205,4387,2147483647,2147483647"
"Vel Dist"="2147483647,2147483647,2147483647,2147483647"
"Encroachments"="2147483647,2147483647,2147483647,2147483647"
"Unsteady Analysis"="2147483647,2147483647,2147483647,2147483647"
"Unsteady Encroachment"="2147483647,2147483647,2147483647,2147483647"
"HTAB"="2147483647,2147483647,2147483647,2147483647"
"IW Breach"="2147483647,2147483647,2147483647,2147483647"
"LW Breach"="2147483647,2147483647,2147483647,2147483647"
"SA Conn Breach"="2147483647,2147483647,2147483647,2147483647"
"Flow Roughness"="2147483647,2147483647,2147483647,2147483647"
"Seasonal Roughness"="2147483647,2147483647,2147483647,2147483647"
"Ungaged Area"="2147483647,2147483647,2147483647,2147483647"
"Unsteady Calibrate Mann"="2147483647,2147483647,2147483647,2147483647"
"Sediment Analysis"="2147483647,2147483647,2147483647,2147483647"
"Sediment Dredging"="2147483647,2147483647,2147483647,2147483647"
"Sediment Energy Slope"="2147483647,2147483647,2147483647,2147483647"
"HD Scour"="2147483647,2147483647,2147483647,2147483647"
"HD Uniform"="2147483647,2147483647,2147483647,2147483647"
"HD Stable"="2147483647,2147483647,2147483647,2147483647"
"HD Sediment"="2147483647,2147483647,2147483647,2147483647"
"HD RipRap"="2147483647,2147483647,2147483647,2147483647"
"HD Siam"="2147483647,2147483647,2147483647,2147483647"
"Geom Data"="2147483647,2147483647,2147483647,2147483647"
"Geom Data View Options"="2147483647,2147483647,2147483647,2147483647"
"Geom Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Desc Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Node Name Table"="2147483647,2147483647,2147483647,2147483647"
"Geom RS Name Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Picture Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Ineff Elev Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Obstruction Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Preissmann Slot Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Land Cover Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Polylines"="2147483647,2147483647,2147483647,2147483647"
"Geom Weir Coef Table"="2147483647,2147483647,2147483647,2147483647"
"Geom HTab IB Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Linear Routing Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Datum Table"="2147483647,2147483647,2147483647,2147483647"
"Geom Channel Mod"="2147483647,2147483647,2147483647,2147483647"
"Geom Chan Mod"="2147483647,2147483647,2147483647,2147483647"
"Geom Chan Mod Template"="2147483647,2147483647,2147483647,2147483647"
"Geom Chan Mod XS"="2147483647,2147483647,2147483647,2147483647"
"Geom Chan Mod CutFill"="2147483647,2147483647,2147483647,2147483647"
"Geom Graphical Editor"="2147483647,2147483647,2147483647,2147483647"
"Geom Pilot Channel"="2147483647,2147483647,2147483647,2147483647"
"Geom Sediment Elev"="2147483647,2147483647,2147483647,2147483647"
"Geom Raster"="2147483647,2147483647,2147483647,2147483647"
"Geom HTab"="2147483647,2147483647,2147483647,2147483647"
"Geom Flow Roughness"="2147483647,2147483647,2147483647,2147483647"
"Geom Seasonal Roughness"="2147483647,2147483647,2147483647,2147483647"
"Geom Reach Order"="2147483647,2147483647,2147483647,2147483647"
"Geom Modified Puls"="2147483647,2147483647,2147483647,2147483647"
"Junction"="2147483647,2147483647,2147483647,2147483647"
"XS"="2147483647,2147483647,2147483647,2147483647"
"XS with Plot"="2147483647,2147483647,2147483647,2147483647"
"XS Ineffective"="2147483647,2147483647,2147483647,2147483647"
"XS Levee"="2147483647,2147483647,2147483647,2147483647"
"XS Block Obstruction"="2147483647,2147483647,2147483647,2147483647"
"XS Add Lid"="2147483647,2147483647,2147483647,2147483647"
"XS Ice"="2147483647,2147483647,2147483647,2147483647"
"XS RC"="2147483647,2147483647,2147483647,2147483647"
"XS Verticaln"="2147483647,2147483647,2147483647,2147483647"
"BC"="2147483647,2147483647,2147483647,2147483647"
"BC Deck"="2147483647,2147483647,2147483647,2147483647"
"BC Pier"="2147483647,2147483647,2147483647,2147483647"
"BC Abutment"="2147483647,2147483647,2147483647,2147483647"
"BC Coeff"="2147483647,2147483647,2147483647,2147483647"
"BC WSPRO"="2147483647,2147483647,2147483647,2147483647"
"BC Culvert"="2147483647,2147483647,2147483647,2147483647"
"BC Mutliple"="2147483647,2147483647,2147483647,2147483647"
"BC XS"="2147483647,2147483647,2147483647,2147483647"
"BC Design"="2147483647,2147483647,2147483647,2147483647"
"BC HTAB"="2147483647,2147483647,2147483647,2147483647"
"BC HTAB Curves"="2147483647,2147483647,2147483647,2147483647"
"IW"="2147483647,2147483647,2147483647,2147483647"
"IW Weir"="2147483647,2147483647,2147483647,2147483647"
"IW Gate"="2147483647,2147483647,2147483647,2147483647"
"IW Culvert"="2147483647,2147483647,2147483647,2147483647"
"IW OutletRC"="2147483647,2147483647,2147483647,2147483647"
"IW OutletTS"="2147483647,2147483647,2147483647,2147483647"
"LW"="2147483647,2147483647,2147483647,2147483647"
"LW Gate"="2147483647,2147483647,2147483647,2147483647"
"LW Weir"="2147483647,2147483647,2147483647,2147483647"
"LW Culv"="2147483647,2147483647,2147483647,2147483647"
"LW Simple Spillway"="2147483647,2147483647,2147483647,2147483647"
"LW Diversion RC"="2147483647,2147483647,2147483647,2147483647"
"LW Outlet TS"="2147483647,2147483647,2147483647,2147483647"
"Storage Area"="2147483647,2147483647,2147483647,2147483647"
"2D Flow Area"="2147483647,2147483647,2147483647,2147483647"
"Connection"="2147483647,2147483647,2147483647,2147483647"
"Connection Weir"="2147483647,2147483647,2147483647,2147483647"
"Connection Gate"="2147483647,2147483647,2147483647,2147483647"
"Connection Culv"="2147483647,2147483647,2147483647,2147483647"
"Connection OutletRC"="2147483647,2147483647,2147483647,2147483647"
"Connection OutletTS"="2147483647,2147483647,2147483647,2147483647"
"Connection hTab"="2147483647,2147483647,2147483647,2147483647"
"Connection Simple Spill"="2147483647,2147483647,2147483647,2147483647"
"Pump Station"="2147483647,2147483647,2147483647,2147483647"
"BC Line"="2147483647,2147483647,2147483647,2147483647"
"Picture"="2147483647,2147483647,2147483647,2147483647"
"Sediment Transport"="2147483647,2147483647,2147483647,2147483647"
"Sediment Load Specification"="2147483647,2147483647,2147483647,2147483647"
"Quasi-Steady Editor"="2147483647,2147483647,2147483647,2147483647"
"Quasi-Steady Temperature Editor"="2147483647,2147483647,2147483647,2147483647"
"Quasi-Steady TimeSeries Editor"="2147483647,2147483647,2147483647,2147483647"
"Quasi-Steady Rating Curve Editor"="2147483647,2147483647,2147483647,2147483647"
"Quasi-Steady Normal Depth Editor"="2147483647,2147483647,2147483647,2147483647"
"Quasi-Steady Gate TimeSeries Editor"="2147483647,2147483647,2147483647,2147483647"
"RAS-ADH Window"="2147483647,2147483647,2147483647,2147483647"
"RAS-MODFLOW Window"="2147483647,2147483647,2147483647,2147483647"
"Computation Window"="6292,1395,11415,10710"
"XS Plot"="2147483647,2147483647,2147483647,2147483647"
"PF Plot"="2147483647,2147483647,2147483647,2147483647"
"RC Plot"="2147483647,2147483647,2147483647,2147483647"
"XYZ Plot"="2147483647,2147483647,2147483647,2147483647"
"XY Plot"="2147483647,2147483647,2147483647,2147483647"
"HY Plot"="2147483647,2147483647,2147483647,2147483647"
"Node Table"="2147483647,2147483647,2147483647,2147483647"
"PF Table"="2147483647,2147483647,2147483647,2147483647"
"DSS View"="2147483647,2147483647,2147483647,2147483647"
"EWN Summary"="2147483647,2147483647,2147483647,2147483647"
"Animate"="2147483647,2147483647,2147483647,2147483647"

[HKEY_USERS\S-1-5-93-2-1\SOFTWARE\VB and VBA Program Settings\C:\Program Files (x86)\HEC\HEC-RAS\5.0.7\ras.exe\Geom Chan Mod CFTable]
"Details"="0"
"Vol Net"="-1"
"Vol Cut"="-1"
"Vol Fill"="-1"
"Area Net"="0"
"Area Cut"="0"
"Area Fill"="0"
"Lengths"="0"

[HKEY_USERS\S-1-5-93-2-1\SOFTWARE\VB and VBA Program Settings\C:\Program Files (x86)\HEC\HEC-RAS\5.0.7\ras.exe\Plot Defaults]
"XYZ Azimuth"="10"
"XYZ Rotation"="-10"
"XYZ Z Factor"="10"
"XYZ Plot Labels"="-1"
"XYZ Plot Legend"="-1"
"XYZ Plot Reverse WS"="0"
"XYZ Plot RS"="-1"
"Plot WS"="-1"
"Plot EG"="-1"
"Plot Critical"="-1"
"Plot Ice"="0"
"Animation Delay"="0"
"Plot Flow HY"="True"
"Plot Stage HY"="True"
"Plot Flow HY Observed"="True"
"Plot Stage HY Observed"="True"
"PlotSF Use Ref Stage"="False"
"Plot Flow Stage nDec"="2"
"Plot LOB"="0"
"Plot ROB"="0"
"Plot Reach Labels"="-1"
"Profile X Axis Scale"="0"
"Plot Observed WS"="-1"
"Plot Left Levee"="-1"
"Plot Right Levee"="-1"
"Plot Pilot Channel"="0"
"Plot Sediment Elev"="0"
"Plot Left LW"="-1"
"Plot Right LW"="-1"
"Plot WS Filled"="-1"
"Plot Mann"="-1"
"Plot Vel Dist"="0"
"Add Zero Point"="-1"
"XS Add HTab Increments"="0"
"HTab Plot Vars"="127"
"HTab Tabel nDec"="2"
"XS Data View Plot"="-1"
"XS Data View Terrain"="True"
"BC Highlight HLG"="-1"
"BC Highlight Piers"="0"
"BC Highlight Clip"="0"

[HKEY_USERS\S-1-5-93-2-1\SOFTWARE\VB and VBA Program Settings\C:\Program Files (x86)\HEC\HEC-RAS\5.0.7\ras.exe\Program Defaults]
"Rule Editor Font Size"="10"
"Rule Editor Font Bold"="0"
"WQ Divider Location"="0"

[HKEY_USERS\S-1-5-93-2-1\SOFTWARE\VB and VBA Program Settings\C:\Program Files (x86)\HEC\HEC-RAS\5.0.7\ras.exe\Projects]
"Project1"=""
"Project2"=""
"Project3"=""
"Project4"=""
"Project5"=""
"Project6"=""
"Project7"=""
"Project8"=""
"System Statistic"="%d"

[HKEY_USERS\S-1-5-93-2-1\SOFTWARE\VB and VBA Program Settings\C:\Program Files (x86)\HEC\HEC-RAS\5.0.7\ras.exe\Table Defaults]
"PF Plot Profile Name"="-1"
"PF Plot Node Name"="-1"

[HKEY_USERS\S-1-5-93-2-1\SOFTWARE\VB and VBA Program Settings\C:\Program Files (x86)\HEC\HEC-RAS\5.0.7\ras.exe\User Defined General PF Plots]
"Count"="0" ''' % (id)

f = open(r'C:\ras07reg.reg','w')
f.write(regfile)
f.close()