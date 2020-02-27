EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 4
Title "ROVER Main PCB"
Date "2020-01-24"
Rev "0.1"
Comp "Jorge Huete"
Comment1 "Top level sheet and block diagram"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Sheet
S 3350 1850 1100 800 
U 5E6BD4F2
F0 "Power Bus Generation" 50
F1 "PowerPCB.sch" 50
F2 "VCC" O R 4450 1950 50 
F3 "5V_LP" O R 4450 2100 50 
F4 "9V_HP" O R 4450 2250 50 
F5 "5V_HP" O R 4450 2400 50 
F6 "BCKP_EN" O L 3350 2100 50 
F7 "9V_HP_EN" O L 3350 2250 50 
F8 "ALG_BUS" O R 4450 2550 50 
$EndSheet
Wire Wire Line
	4450 2400 4850 2400
Wire Bus Line
	4450 2550 6050 2550
$Sheet
S 5200 3450 1250 850 
U 5E691C3E
F0 "Motor Control" 50
F1 "MotorControl.sch" 50
F2 "9V_HP" I L 5200 3900 50 
F3 "LT_R" I R 6450 3500 50 
F4 "LT_F" I R 6450 3600 50 
F5 "RT_R" I R 6450 3700 50 
F6 "RT_F" I R 6450 3800 50 
F7 "L_Hall1" I R 6450 3900 50 
F8 "L_Hall2" I R 6450 4000 50 
F9 "R_Hall1" I R 6450 4100 50 
F10 "R_Hall2" I R 6450 4200 50 
F11 "5V_LP" I L 5200 3800 50 
$EndSheet
Wire Wire Line
	4450 2250 4750 2250
Wire Wire Line
	5200 3800 4850 3800
Wire Wire Line
	4850 3800 4850 2400
Connection ~ 4850 2400
Wire Wire Line
	4850 2400 6050 2400
Wire Wire Line
	5200 3900 4750 3900
Wire Wire Line
	4750 3900 4750 2250
Connection ~ 4750 2250
Wire Wire Line
	4750 2250 6050 2250
$Sheet
S 6050 1850 1100 800 
U 5E96FE61
F0 "Control Logic" 50
F1 "ControlLogic.sch" 50
F2 "5V_HP" O L 6050 2400 50 
F3 "9V_HP" O L 6050 2250 50 
F4 "ALG_BUS" O L 6050 2550 50 
F5 "LT_R" I R 7150 2600 50 
F6 "LT_L" I R 7150 2500 50 
F7 "RT_R" I R 7150 2400 50 
F8 "RT_L" I R 7150 2300 50 
F9 "LHall1" I R 7150 2200 50 
F10 "LHall2" I R 7150 2100 50 
F11 "RHall1" I R 7150 2000 50 
F12 "RHall2" I R 7150 1900 50 
F13 "BCKP_EN" I L 6050 1900 50 
F14 "9V_HP_EN" I L 6050 2000 50 
$EndSheet
Wire Wire Line
	7150 2600 7250 2600
Wire Wire Line
	7250 2600 7250 3500
Wire Wire Line
	7250 3500 6450 3500
Wire Wire Line
	6450 3600 7350 3600
Wire Wire Line
	7350 3600 7350 2500
Wire Wire Line
	7350 2500 7150 2500
Wire Wire Line
	7150 2400 7450 2400
Wire Wire Line
	7450 2400 7450 3700
Wire Wire Line
	7450 3700 6450 3700
Wire Wire Line
	6450 3800 7550 3800
Wire Wire Line
	7550 3800 7550 2300
Wire Wire Line
	7550 2300 7150 2300
Wire Wire Line
	7150 2200 7650 2200
Wire Wire Line
	7650 2200 7650 3900
Wire Wire Line
	7650 3900 6450 3900
Wire Wire Line
	6450 4000 7750 4000
Wire Wire Line
	7750 4000 7750 2100
Wire Wire Line
	7750 2100 7150 2100
Wire Wire Line
	7150 2000 7850 2000
Wire Wire Line
	7850 2000 7850 4100
Wire Wire Line
	7850 4100 6450 4100
Wire Wire Line
	6450 4200 7950 4200
Wire Wire Line
	7950 4200 7950 1900
Wire Wire Line
	7950 1900 7150 1900
Wire Wire Line
	3350 2100 3200 2100
Wire Wire Line
	3200 2100 3200 1650
Wire Wire Line
	3200 1650 5750 1650
Wire Wire Line
	5750 1650 5750 1900
Wire Wire Line
	5750 1900 6050 1900
Wire Wire Line
	6050 2000 5650 2000
Wire Wire Line
	5650 2000 5650 1550
Wire Wire Line
	5650 1550 3100 1550
Wire Wire Line
	3100 1550 3100 2250
Wire Wire Line
	3100 2250 3350 2250
$EndSCHEMATC
