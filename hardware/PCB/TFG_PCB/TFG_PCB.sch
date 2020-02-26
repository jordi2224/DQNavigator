EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 3
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
	6050 2250 4450 2250
Wire Wire Line
	4450 2400 6050 2400
Wire Bus Line
	4450 2550 6050 2550
$Sheet
S 6050 1850 1100 800 
U 5E96FE61
F0 "Control Logic" 50
F1 "ControlLogic.sch" 50
F2 "5V_HP" O L 6050 2400 50 
F3 "9V_HP" O L 6050 2250 50 
F4 "ALG_BUS" O L 6050 2550 50 
$EndSheet
$Sheet
S 5150 3550 1250 850 
U 5E691C3E
F0 "Motor Control" 50
F1 "MotorControl.sch" 50
$EndSheet
$EndSCHEMATC
