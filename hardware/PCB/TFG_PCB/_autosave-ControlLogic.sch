EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 4
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Raspberry_Pi_2_3 J18
U 1 1 5E97206E
P 3700 3450
F 0 "J18" H 3700 4931 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 3700 4840 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H 3700 3450 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 3700 3450 50  0001 C CNN
	1    3700 3450
	1    0    0    -1  
$EndComp
Text HLabel 2100 1900 0    50   Output ~ 0
5V_HP
Wire Wire Line
	3500 2150 3500 1900
Wire Wire Line
	3500 1900 2100 1900
Wire Wire Line
	3600 2150 3600 1900
Wire Wire Line
	3600 1900 3500 1900
Connection ~ 3500 1900
Wire Wire Line
	3300 4750 3300 4850
Wire Wire Line
	3300 4850 3400 4850
Wire Wire Line
	4000 4850 4000 4750
Wire Wire Line
	3900 4750 3900 4850
Connection ~ 3900 4850
Wire Wire Line
	3900 4850 4000 4850
Wire Wire Line
	3800 4750 3800 4850
Connection ~ 3800 4850
Wire Wire Line
	3800 4850 3900 4850
Wire Wire Line
	3700 4750 3700 4850
Connection ~ 3700 4850
Wire Wire Line
	3700 4850 3800 4850
Wire Wire Line
	3600 4750 3600 4850
Connection ~ 3600 4850
Wire Wire Line
	3600 4850 3650 4850
Wire Wire Line
	3500 4750 3500 4850
Connection ~ 3500 4850
Wire Wire Line
	3500 4850 3600 4850
Wire Wire Line
	3400 4750 3400 4850
Connection ~ 3400 4850
Wire Wire Line
	3400 4850 3500 4850
$Comp
L power:GND #PWR041
U 1 1 5E9AD34B
P 3650 4850
F 0 "#PWR041" H 3650 4600 50  0001 C CNN
F 1 "GND" H 3655 4677 50  0000 C CNN
F 2 "" H 3650 4850 50  0001 C CNN
F 3 "" H 3650 4850 50  0001 C CNN
	1    3650 4850
	1    0    0    -1  
$EndComp
Connection ~ 3650 4850
Wire Wire Line
	3650 4850 3700 4850
Text HLabel 6700 1900 0    50   Output ~ 0
9V_HP
Wire Wire Line
	7250 1900 6700 1900
Wire Wire Line
	2900 4150 2750 4150
Wire Wire Line
	2750 4150 2750 5150
Wire Wire Line
	2900 4050 2650 4050
Wire Wire Line
	2650 4050 2650 5250
Wire Wire Line
	2900 3950 2550 3950
Wire Wire Line
	2550 3950 2550 5350
Wire Wire Line
	2900 3850 2450 3850
Wire Wire Line
	2450 3850 2450 5450
Wire Wire Line
	2900 3750 2350 3750
Wire Wire Line
	2350 3750 2350 5550
Wire Wire Line
	2750 5150 6200 5150
Wire Wire Line
	6200 5150 6200 3250
Wire Wire Line
	6300 3350 6300 5250
Wire Wire Line
	6300 5250 2650 5250
Wire Wire Line
	2550 5350 6400 5350
Wire Wire Line
	6400 5350 6400 3450
Wire Wire Line
	6500 5450 2450 5450
Wire Wire Line
	2350 5550 6600 5550
$Comp
L TFG_PCB-rescue:MCP3021A0T-E_OT-SamacSys_Parts IC1
U 1 1 5E64EE7F
P 5750 2950
F 0 "IC1" H 6250 2485 50  0000 C CNN
F 1 "MCP3021A0T-E_OT" H 6250 2576 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23-5" H 6600 3050 50  0001 L CNN
F 3 "https://componentsearchengine.com/Datasheets/1/MCP3021A0T-E_OT.pdf" H 6600 2950 50  0001 L CNN
F 4 "MICROCHIP - MCP3021A0T-E/OT - ADC, AEC-Q100, SAR, 10BIT, SOT-23-5" H 6600 2850 50  0001 L CNN "Description"
F 5 "1.45" H 6600 2750 50  0001 L CNN "Height"
F 6 "579-MCP3021A0T-E/OT" H 6600 2650 50  0001 L CNN "Mouser Part Number"
F 7 "https://www.mouser.com/Search/Refine.aspx?Keyword=579-MCP3021A0T-E%2FOT" H 6600 2550 50  0001 L CNN "Mouser Price/Stock"
F 8 "Microchip" H 6600 2450 50  0001 L CNN "Manufacturer_Name"
F 9 "MCP3021A0T-E/OT" H 6600 2350 50  0001 L CNN "Manufacturer_Part_Number"
	1    5750 2950
	-1   0    0    1   
$EndComp
$Comp
L Device:R R36
U 1 1 5E65FE45
P 5850 3300
F 0 "R36" H 5920 3346 50  0000 L CNN
F 1 "10k" H 5920 3255 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 5780 3300 50  0001 C CNN
F 3 "~" H 5850 3300 50  0001 C CNN
	1    5850 3300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5850 3150 6150 3150
$Comp
L power:GND #PWR0113
U 1 1 5E6630D9
P 5850 3450
F 0 "#PWR0113" H 5850 3200 50  0001 C CNN
F 1 "GND" H 5855 3277 50  0000 C CNN
F 2 "" H 5850 3450 50  0001 C CNN
F 3 "" H 5850 3450 50  0001 C CNN
	1    5850 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	6150 3150 6150 2750
Wire Wire Line
	6150 2750 5750 2750
Wire Wire Line
	5750 2950 5950 2950
Wire Wire Line
	5750 2850 6100 2850
Wire Wire Line
	6100 2850 6100 3450
Wire Wire Line
	6100 3450 5850 3450
Connection ~ 5850 3450
Wire Wire Line
	5950 1900 3600 1900
Wire Wire Line
	5950 1900 5950 2950
Connection ~ 3600 1900
Wire Wire Line
	4500 2850 4600 2850
Wire Wire Line
	4600 2850 4600 3000
Wire Wire Line
	4600 3000 4750 3000
Wire Wire Line
	4750 3000 4750 2950
Wire Wire Line
	4500 2950 4650 2950
Wire Wire Line
	4650 2950 4650 2850
Wire Wire Line
	4650 2850 4750 2850
Text HLabel 2350 2850 0    50   Input ~ 0
LT_R
Text HLabel 2350 2950 0    50   Input ~ 0
LT_L
Text HLabel 2350 3050 0    50   Input ~ 0
RT_R
Text HLabel 2350 3250 0    50   Input ~ 0
RT_L
Wire Wire Line
	2350 2850 2900 2850
Wire Wire Line
	2900 2950 2350 2950
Wire Wire Line
	2350 3050 2900 3050
Wire Wire Line
	2900 3250 2350 3250
Text HLabel 2350 3350 0    50   Input ~ 0
LHall1
Text HLabel 2350 3450 0    50   Input ~ 0
LHall2
Text HLabel 2350 3650 0    50   Input ~ 0
RHall1
Wire Wire Line
	2350 3350 2900 3350
Wire Wire Line
	2900 3450 2350 3450
Wire Wire Line
	2350 3650 2900 3650
Text HLabel 4950 3150 2    50   Input ~ 0
RHall2
Wire Wire Line
	4950 3150 4500 3150
Text HLabel 4950 3250 2    50   Input ~ 0
BCKP_EN
Text HLabel 4950 3350 2    50   Input ~ 0
9V_HP_EN
Wire Wire Line
	4950 3350 4500 3350
Wire Wire Line
	4500 3250 4950 3250
Connection ~ 6150 3150
Wire Wire Line
	6750 3400 6750 3450
Wire Wire Line
	6500 3400 6750 3400
Wire Wire Line
	6500 3400 6500 5450
Wire Wire Line
	6600 3550 6750 3550
Wire Wire Line
	6600 3450 6600 3550
Wire Wire Line
	6400 3450 6600 3450
Wire Wire Line
	7750 2950 10000 2950
Wire Wire Line
	7750 2850 10000 2850
Wire Wire Line
	9450 3650 10000 3650
Text GLabel 10000 3650 2    50   Input ~ 0
BAT2_3S
Wire Wire Line
	9150 3450 10000 3450
Text GLabel 10000 3450 2    50   Input ~ 0
BAT1_3S
Wire Wire Line
	7750 2750 10000 2750
Wire Wire Line
	7750 2650 10000 2650
Wire Wire Line
	8850 3250 10000 3250
Text GLabel 10000 2850 2    50   Input ~ 0
BAT2_2S
Text GLabel 10000 2950 2    50   Input ~ 0
BAT2_1S
Text GLabel 10000 2650 2    50   Input ~ 0
BAT1_2S
Text GLabel 10000 2750 2    50   Input ~ 0
BAT1_1S
Text GLabel 10000 3250 2    50   Input ~ 0
BCKP_3S
Wire Wire Line
	7750 3150 10000 3150
Wire Wire Line
	7750 3050 10000 3050
Text GLabel 10000 3050 2    50   Input ~ 0
9V_HP
Text GLabel 10000 3150 2    50   Input ~ 0
5V_HP
Wire Wire Line
	6150 3150 6500 3150
Wire Wire Line
	6500 2850 6750 2850
$Comp
L Device:R R37
U 1 1 5E65D601
P 6500 3000
F 0 "R37" H 6570 3046 50  0000 L CNN
F 1 "10k" H 6570 2955 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 6430 3000 50  0001 C CNN
F 3 "~" H 6500 3000 50  0001 C CNN
	1    6500 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	6600 3950 6750 3950
Wire Wire Line
	6600 5550 6600 3950
Wire Wire Line
	6750 3350 6300 3350
Wire Wire Line
	6200 3250 6750 3250
Text Label 9550 3650 0    50   ~ 0
BAT2_3S
Text Label 9550 3450 0    50   ~ 0
BAT1_3S
Text Label 9550 3250 0    50   ~ 0
BCKP_3S
Connection ~ 8850 3550
Wire Wire Line
	8850 4000 8850 3550
Connection ~ 9150 3750
Wire Wire Line
	9150 4000 9150 3750
Wire Wire Line
	8850 4300 8850 4550
Wire Wire Line
	9150 4300 9150 4550
Connection ~ 9450 3950
Wire Wire Line
	8300 3450 7750 3450
Wire Wire Line
	8300 3950 8300 3450
Wire Wire Line
	9450 3950 8300 3950
Wire Wire Line
	8400 3350 7750 3350
Wire Wire Line
	8400 3750 8400 3350
Wire Wire Line
	9150 3750 8400 3750
Wire Wire Line
	8500 3550 8850 3550
Wire Wire Line
	8500 3250 8500 3550
Wire Wire Line
	7750 3250 8500 3250
Connection ~ 8850 4550
Wire Wire Line
	7250 4550 7250 4450
Wire Wire Line
	8850 4550 7250 4550
Wire Wire Line
	8850 4550 9150 4550
Connection ~ 9150 4550
Wire Wire Line
	9450 4550 9150 4550
Wire Wire Line
	9450 4250 9450 4550
$Comp
L power:GND #PWR0112
U 1 1 5E6277F8
P 9150 4550
F 0 "#PWR0112" H 9150 4300 50  0001 C CNN
F 1 "GND" H 9155 4377 50  0000 C CNN
F 2 "" H 9150 4550 50  0001 C CNN
F 3 "" H 9150 4550 50  0001 C CNN
	1    9150 4550
	1    0    0    -1  
$EndComp
$Comp
L Device:R R39
U 1 1 5E6260BB
P 8850 4150
F 0 "R39" H 8920 4196 50  0000 L CNN
F 1 "10k" H 8920 4105 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8780 4150 50  0001 C CNN
F 3 "~" H 8850 4150 50  0001 C CNN
	1    8850 4150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R41
U 1 1 5E62517F
P 9150 4150
F 0 "R41" H 9220 4196 50  0000 L CNN
F 1 "10k" H 9220 4105 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 9080 4150 50  0001 C CNN
F 3 "~" H 9150 4150 50  0001 C CNN
	1    9150 4150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R40
U 1 1 5E624522
P 9150 3600
F 0 "R40" H 9220 3646 50  0000 L CNN
F 1 "10k" H 9220 3555 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 9080 3600 50  0001 C CNN
F 3 "~" H 9150 3600 50  0001 C CNN
	1    9150 3600
	1    0    0    -1  
$EndComp
$Comp
L Device:R R43
U 1 1 5E623E34
P 9450 4100
F 0 "R43" H 9520 4146 50  0000 L CNN
F 1 "10k" H 9520 4055 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 9380 4100 50  0001 C CNN
F 3 "~" H 9450 4100 50  0001 C CNN
	1    9450 4100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R42
U 1 1 5E621BC0
P 9450 3800
F 0 "R42" H 9520 3846 50  0000 L CNN
F 1 "10k" H 9520 3755 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 9380 3800 50  0001 C CNN
F 3 "~" H 9450 3800 50  0001 C CNN
	1    9450 3800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R38
U 1 1 5E6201A7
P 8850 3400
F 0 "R38" H 8920 3446 50  0000 L CNN
F 1 "10k" H 8920 3355 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8780 3400 50  0001 C CNN
F 3 "~" H 8850 3400 50  0001 C CNN
	1    8850 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	7250 2350 7250 1900
Text Label 9550 3150 0    50   ~ 0
5V_HP
Text Label 9550 3050 0    50   ~ 0
9V_HP
Text Label 9550 2950 0    50   ~ 0
BAT2_1S
Text Label 9550 2850 0    50   ~ 0
BAT2_2S
Text Label 9550 2750 0    50   ~ 0
BAT1_1S
Text Label 9550 2650 0    50   ~ 0
BAT1_2S
$Comp
L 74xx:CD74HC4067M U4
U 1 1 5E9A928D
P 7250 3350
F 0 "U4" H 7250 4531 50  0000 C CNN
F 1 "CD74HC4067M" H 7250 4440 50  0000 C CNN
F 2 "Package_SO:SOIC-24W_7.5x15.4mm_P1.27mm" H 8150 2350 50  0001 C CIN
F 3 "http://www.ti.com/lit/ds/symlink/cd74hc4067.pdf" H 6900 4200 50  0001 C CNN
	1    7250 3350
	1    0    0    -1  
$EndComp
$EndSCHEMATC
