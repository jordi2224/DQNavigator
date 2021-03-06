EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 4
Title "Power buses generation and control"
Date "2020-01-24"
Rev "0.1"
Comp "Jorge Huete"
Comment1 "Uses 3 3S LiPo batteries for VCC (12.6 - 9.9V), 9V and 5V"
Comment2 "BMS are off the shelf for cell leveling"
Comment3 "LiPo 3 is backup and default state is off"
Comment4 ""
$EndDescr
Wire Wire Line
	1900 6650 2150 6650
Wire Wire Line
	1900 6250 2150 6250
Wire Wire Line
	2150 6250 2150 6650
Wire Wire Line
	1900 5950 2050 5950
Wire Wire Line
	2050 5950 2050 6550
Wire Wire Line
	2050 6550 1900 6550
Wire Wire Line
	2600 6650 2350 6650
Connection ~ 2150 6650
Wire Wire Line
	2050 5950 3150 5950
Wire Wire Line
	3150 5950 3150 5750
Connection ~ 2050 5950
Connection ~ 2350 6650
Wire Wire Line
	2350 6650 2150 6650
Wire Wire Line
	2800 6950 2800 7000
Wire Wire Line
	2800 7000 2600 7000
Wire Wire Line
	2350 7000 2350 6950
Text GLabel 2450 7250 0    50   Input ~ 0
BCKP_EN
Wire Wire Line
	2600 7000 2600 7250
Wire Wire Line
	2600 7250 2450 7250
Connection ~ 2600 7000
Wire Wire Line
	2600 7000 2350 7000
Wire Wire Line
	3250 5750 3250 6650
Wire Wire Line
	3250 6650 3000 6650
Wire Wire Line
	3950 6650 3250 6650
Connection ~ 3250 6650
Wire Wire Line
	1900 6150 3850 6150
Wire Wire Line
	3850 6150 3850 5750
Wire Wire Line
	3750 5750 3750 6050
Wire Wire Line
	3750 6050 1900 6050
Wire Wire Line
	3650 5750 3650 5950
Wire Wire Line
	3650 5950 3150 5950
Connection ~ 3150 5950
Text GLabel 4300 5950 2    50   Input ~ 0
BCKP_3S
Wire Wire Line
	4300 5950 3650 5950
Connection ~ 3650 5950
Wire Wire Line
	3950 5750 3950 6650
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5E6E7A4A
P 5150 5550
AR Path="/5E6E7A4A" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E6E7A4A" Ref="J11"  Part="1" 
F 0 "J11" H 5258 5731 50  0000 C CNN
F 1 "Conn_01x02_Male" H 5258 5640 50  0000 C CNN
F 2 "Connector_Wire:SolderWirePad_1x02_P7.62mm_Drill2mm" H 5150 5550 50  0001 C CNN
F 3 "~" H 5150 5550 50  0001 C CNN
	1    5150 5550
	0    -1   1    0   
$EndComp
Wire Wire Line
	5250 5750 5250 6650
Wire Wire Line
	5250 6650 4200 6650
Connection ~ 3950 6650
Text GLabel 5500 5850 2    50   Input ~ 0
VCC
Wire Wire Line
	5150 5850 5150 5750
Wire Wire Line
	5150 5850 5500 5850
$Comp
L power:GND #PWR?
U 1 1 5E6E7A56
P 4200 6950
AR Path="/5E6E7A56" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E6E7A56" Ref="#PWR07"  Part="1" 
F 0 "#PWR07" H 4200 6700 50  0001 C CNN
F 1 "GND" H 4205 6777 50  0000 C CNN
F 2 "" H 4200 6950 50  0001 C CNN
F 3 "" H 4200 6950 50  0001 C CNN
	1    4200 6950
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 6950 4200 6650
Connection ~ 4200 6650
Wire Wire Line
	4200 6650 3950 6650
Wire Wire Line
	2250 1900 2250 2300
Wire Wire Line
	2250 2300 1900 2300
Wire Wire Line
	2250 3600 1900 3600
Wire Wire Line
	2350 4300 2350 2000
Wire Wire Line
	2350 2000 1900 2000
Wire Wire Line
	2850 2500 2850 2750
Wire Wire Line
	1900 3800 2850 3800
Wire Wire Line
	1900 2500 2850 2500
Connection ~ 3650 1900
Wire Wire Line
	3650 1900 3800 1900
Connection ~ 3650 4200
Wire Wire Line
	3650 4200 3800 4200
Wire Wire Line
	3650 2200 3650 2250
Wire Wire Line
	3650 2250 4200 2250
Wire Wire Line
	4200 2250 4200 2200
Wire Wire Line
	3650 4500 3650 4550
Wire Wire Line
	4200 4550 4200 4500
Wire Wire Line
	4200 4700 4200 4550
Connection ~ 4200 4550
$Comp
L power:GND #PWR?
U 1 1 5E97A711
P 4200 2400
AR Path="/5E97A711" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A711" Ref="#PWR04"  Part="1" 
F 0 "#PWR04" H 4200 2150 50  0001 C CNN
F 1 "GND" H 4205 2227 50  0000 C CNN
F 2 "" H 4200 2400 50  0001 C CNN
F 3 "" H 4200 2400 50  0001 C CNN
	1    4200 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	4200 2400 4200 2250
Connection ~ 4200 2250
Wire Wire Line
	2250 1900 3650 1900
Wire Wire Line
	2250 4200 3650 4200
Wire Wire Line
	2250 1900 1900 1900
Connection ~ 2250 1900
Wire Wire Line
	2250 4200 2250 3600
Wire Wire Line
	2250 4200 1900 4200
Connection ~ 2250 4200
Wire Wire Line
	2350 4300 3500 4300
Wire Wire Line
	3500 4300 3500 4550
Wire Wire Line
	3500 4550 3650 4550
Connection ~ 2350 4300
Connection ~ 3650 4550
Wire Wire Line
	3650 2250 3500 2250
Wire Wire Line
	3500 2250 3500 2000
Wire Wire Line
	3500 2000 2350 2000
Connection ~ 3650 2250
Connection ~ 2350 2000
$Comp
L power:GND #PWR?
U 1 1 5E97A712
P 4200 4700
AR Path="/5E97A712" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A712" Ref="#PWR06"  Part="1" 
F 0 "#PWR06" H 4200 4450 50  0001 C CNN
F 1 "GND" H 4205 4527 50  0000 C CNN
F 2 "" H 4200 4700 50  0001 C CNN
F 3 "" H 4200 4700 50  0001 C CNN
	1    4200 4700
	1    0    0    -1  
$EndComp
Wire Wire Line
	3650 4550 4200 4550
Wire Wire Line
	5150 1800 5150 1900
Wire Wire Line
	5150 1900 4650 1900
Wire Wire Line
	5150 3600 5150 4200
Wire Wire Line
	5150 4200 4650 4200
Wire Wire Line
	2250 2300 3400 2300
Wire Wire Line
	3400 2300 3400 2850
Connection ~ 2250 2300
Wire Wire Line
	2250 3600 3400 3600
Connection ~ 2250 3600
Wire Wire Line
	3100 2400 1900 2400
Wire Wire Line
	1900 3700 3100 3700
Wire Wire Line
	1900 3900 2100 3900
Wire Wire Line
	2100 3900 2100 3150
Wire Wire Line
	2100 2600 1900 2600
Wire Wire Line
	5450 1800 5450 2250
Wire Wire Line
	5450 3600 5450 4550
Wire Wire Line
	5250 1800 5250 2650
Wire Wire Line
	5250 2650 3950 2650
Connection ~ 3100 2650
Wire Wire Line
	3100 2650 3100 2400
Wire Wire Line
	2850 2750 3850 2750
Wire Wire Line
	5350 2750 5350 1800
Connection ~ 2850 2750
Wire Wire Line
	5250 3600 5250 3700
Wire Wire Line
	5250 3700 3100 3700
Connection ~ 3100 3700
Wire Wire Line
	2850 3800 5350 3800
Wire Wire Line
	5350 3800 5350 3600
Connection ~ 2850 3800
Wire Wire Line
	4650 1800 4650 1900
Connection ~ 4650 1900
Wire Wire Line
	4650 1900 4400 1900
Wire Wire Line
	4750 1800 4750 2250
Wire Wire Line
	4200 2250 4750 2250
Connection ~ 4750 2250
Wire Wire Line
	4750 2250 5450 2250
Wire Wire Line
	4650 4100 4650 4200
Connection ~ 4650 4200
Wire Wire Line
	4650 4200 4400 4200
Wire Wire Line
	4750 4100 4750 4550
Wire Wire Line
	4200 4550 4750 4550
Connection ~ 4750 4550
Wire Wire Line
	4750 4550 5450 4550
Wire Wire Line
	6200 1800 6200 1900
Wire Wire Line
	6200 1900 6600 1900
Wire Wire Line
	6600 1900 6600 1800
Connection ~ 6600 1900
Wire Wire Line
	5450 2250 6300 2250
Connection ~ 5450 2250
Wire Wire Line
	9700 4300 9550 4300
Wire Wire Line
	5850 2700 5700 2700
Wire Wire Line
	5700 2700 5700 1900
Wire Wire Line
	5700 1900 6200 1900
Connection ~ 6200 1900
$Comp
L power:GND #PWR?
U 1 1 5E762998
P 6150 3000
AR Path="/5E762998" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E762998" Ref="#PWR011"  Part="1" 
F 0 "#PWR011" H 6150 2750 50  0001 C CNN
F 1 "GND" H 6155 2827 50  0000 C CNN
F 2 "" H 6150 3000 50  0001 C CNN
F 3 "" H 6150 3000 50  0001 C CNN
	1    6150 3000
	1    0    0    -1  
$EndComp
Connection ~ 5700 2700
$Comp
L power:GND #PWR?
U 1 1 5E7629A5
P 5700 3000
AR Path="/5E7629A5" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E7629A5" Ref="#PWR09"  Part="1" 
F 0 "#PWR09" H 5700 2750 50  0001 C CNN
F 1 "GND" H 5705 2827 50  0000 C CNN
F 2 "" H 5700 3000 50  0001 C CNN
F 3 "" H 5700 3000 50  0001 C CNN
	1    5700 3000
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E7629B1
P 6600 3000
AR Path="/5E7629B1" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E7629B1" Ref="#PWR013"  Part="1" 
F 0 "#PWR013" H 6600 2750 50  0001 C CNN
F 1 "GND" H 6605 2827 50  0000 C CNN
F 2 "" H 6600 3000 50  0001 C CNN
F 3 "" H 6600 3000 50  0001 C CNN
	1    6600 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	10000 4100 9900 4100
Wire Wire Line
	9900 4100 9900 4200
Wire Wire Line
	9900 4100 9550 4100
Connection ~ 9900 4100
Wire Wire Line
	9900 4500 9900 4750
Wire Wire Line
	9900 4750 9550 4750
$Comp
L power:GND #PWR?
U 1 1 5E7629E1
P 10400 4150
AR Path="/5E7629E1" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E7629E1" Ref="#PWR039"  Part="1" 
F 0 "#PWR039" H 10400 3900 50  0001 C CNN
F 1 "GND" H 10405 3977 50  0000 C CNN
F 2 "" H 10400 4150 50  0001 C CNN
F 3 "" H 10400 4150 50  0001 C CNN
	1    10400 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	10300 4100 10400 4100
Wire Wire Line
	10400 4100 10400 4150
$Comp
L power:+5V #PWR?
U 1 1 5E97A72C
P 9550 4750
AR Path="/5E97A72C" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A72C" Ref="#PWR028"  Part="1" 
F 0 "#PWR028" H 9550 4600 50  0001 C CNN
F 1 "+5V" H 9565 4923 50  0000 C CNN
F 2 "" H 9550 4750 50  0001 C CNN
F 3 "" H 9550 4750 50  0001 C CNN
	1    9550 4750
	1    0    0    -1  
$EndComp
Connection ~ 9550 4750
Wire Wire Line
	9550 4750 9450 4750
$Comp
L power:GND #PWR?
U 1 1 5E97A72D
P 9700 4300
AR Path="/5E97A72D" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A72D" Ref="#PWR032"  Part="1" 
F 0 "#PWR032" H 9700 4050 50  0001 C CNN
F 1 "GND" H 9705 4127 50  0000 C CNN
F 2 "" H 9700 4300 50  0001 C CNN
F 3 "" H 9700 4300 50  0001 C CNN
	1    9700 4300
	1    0    0    -1  
$EndComp
Text GLabel 4050 2850 2    50   Input ~ 0
BAT1_3S
Text GLabel 4050 2950 2    50   Input ~ 0
BAT1_2S
Text GLabel 4050 3050 2    50   Input ~ 0
BAT1_1S
Text GLabel 4050 3350 2    50   Input ~ 0
BAT2_3S
Text GLabel 4050 3450 2    50   Input ~ 0
BAT2_2S
Text GLabel 4050 3550 2    50   Input ~ 0
BAT2_1S
Wire Wire Line
	4050 2850 3400 2850
Wire Wire Line
	4050 2950 3950 2950
Wire Wire Line
	3950 2950 3950 2650
Connection ~ 3950 2650
Wire Wire Line
	3950 2650 3100 2650
Wire Wire Line
	3850 2750 3850 3050
Wire Wire Line
	3850 3050 4050 3050
Connection ~ 3850 2750
Wire Wire Line
	3850 2750 5350 2750
Wire Wire Line
	3400 3250 3400 3350
Wire Wire Line
	3100 3250 3100 3450
Wire Wire Line
	2850 3250 2850 3550
Wire Wire Line
	3400 2950 3400 2850
Connection ~ 3400 2850
Wire Wire Line
	3100 2650 3100 2950
Wire Wire Line
	2850 2750 2850 2950
Wire Wire Line
	4050 3350 3400 3350
Connection ~ 3400 3350
Wire Wire Line
	3400 3350 3400 3600
Wire Wire Line
	4050 3450 3100 3450
Connection ~ 3100 3450
Wire Wire Line
	3100 3450 3100 3700
Wire Wire Line
	2850 3550 4050 3550
Connection ~ 2850 3550
Wire Wire Line
	2850 3550 2850 3800
Text GLabel 10700 4750 2    50   Input ~ 0
5V_HP
Connection ~ 9900 4750
Wire Wire Line
	6300 1800 6300 2250
Wire Wire Line
	6700 2250 6300 2250
Wire Wire Line
	6700 1800 6700 2250
Connection ~ 6300 2250
Wire Wire Line
	6600 2700 6450 2700
Wire Wire Line
	8100 4750 8150 4750
Wire Wire Line
	8100 4750 8100 4850
Wire Wire Line
	8100 4850 8150 4850
$Comp
L power:GND #PWR?
U 1 1 5E97A72E
P 8100 5000
AR Path="/5E97A72E" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A72E" Ref="#PWR020"  Part="1" 
F 0 "#PWR020" H 8100 4750 50  0001 C CNN
F 1 "GND" H 8105 4827 50  0000 C CNN
F 2 "" H 8100 5000 50  0001 C CNN
F 3 "" H 8100 5000 50  0001 C CNN
	1    8100 5000
	1    0    0    -1  
$EndComp
Wire Wire Line
	8100 5000 8100 4850
Connection ~ 8100 4850
Text GLabel 7150 2700 2    50   Input ~ 0
5V_LP
Wire Wire Line
	7150 2700 7100 2700
Connection ~ 6600 2700
$Comp
L power:+5VL #PWR?
U 1 1 5E97A72F
P 6850 2700
AR Path="/5E97A72F" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A72F" Ref="#PWR016"  Part="1" 
F 0 "#PWR016" H 6850 2550 50  0001 C CNN
F 1 "+5VL" H 6865 2873 50  0000 C CNN
F 2 "" H 6850 2700 50  0001 C CNN
F 3 "" H 6850 2700 50  0001 C CNN
	1    6850 2700
	1    0    0    -1  
$EndComp
Connection ~ 6850 2700
Wire Wire Line
	6850 2700 6600 2700
Wire Wire Line
	7600 1550 7450 1550
Wire Wire Line
	7450 1550 7450 1700
Wire Wire Line
	8100 4650 8100 4850
Wire Wire Line
	8100 4350 8100 4300
$Comp
L power:+5VL #PWR?
U 1 1 5E762A80
P 8350 3550
AR Path="/5E762A80" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E762A80" Ref="#PWR021"  Part="1" 
F 0 "#PWR021" H 8350 3400 50  0001 C CNN
F 1 "+5VL" H 8365 3723 50  0000 C CNN
F 2 "" H 8350 3550 50  0001 C CNN
F 3 "" H 8350 3550 50  0001 C CNN
	1    8350 3550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E762AB8
P 9950 5050
AR Path="/5E762AB8" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E762AB8" Ref="#PWR035"  Part="1" 
F 0 "#PWR035" H 9950 4800 50  0001 C CNN
F 1 "GND" H 9955 4877 50  0000 C CNN
F 2 "" H 9950 5050 50  0001 C CNN
F 3 "" H 9950 5050 50  0001 C CNN
	1    9950 5050
	1    0    0    -1  
$EndComp
Connection ~ 10350 4750
Wire Wire Line
	9900 4750 9950 4750
Connection ~ 9950 4750
Wire Wire Line
	9950 4750 10350 4750
Connection ~ 9950 5050
Wire Wire Line
	9550 5050 9950 5050
Wire Wire Line
	9950 5050 10350 5050
Wire Wire Line
	10350 4750 10650 4750
Connection ~ 7600 4100
Wire Wire Line
	7600 4100 7200 4100
Wire Wire Line
	8100 4850 7600 4850
Wire Wire Line
	7600 4850 7600 4400
Connection ~ 7600 4400
Wire Wire Line
	7200 4400 7600 4400
Wire Wire Line
	1900 4300 2350 4300
$Comp
L power:GND #PWR?
U 1 1 5E762AE9
P 2250 3250
AR Path="/5E762AE9" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E762AE9" Ref="#PWR01"  Part="1" 
F 0 "#PWR01" H 2250 3000 50  0001 C CNN
F 1 "GND" H 2255 3077 50  0000 C CNN
F 2 "" H 2250 3250 50  0001 C CNN
F 3 "" H 2250 3250 50  0001 C CNN
	1    2250 3250
	1    0    0    -1  
$EndComp
Wire Wire Line
	2250 3250 2250 3150
Wire Wire Line
	2250 3150 2100 3150
Connection ~ 2100 3150
Wire Wire Line
	2100 3150 2100 2600
Wire Wire Line
	7600 1700 7450 1700
Connection ~ 7450 1700
Wire Wire Line
	7450 1700 7450 1900
$Comp
L Connector:Conn_01x04_Male J?
U 1 1 5E6E7A02
P 1700 6050
AR Path="/5E6E7A02" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E6E7A02" Ref="J5"  Part="1" 
F 0 "J5" H 1808 6331 50  0000 C CNN
F 1 "Conn_01x04_Male" H 1808 6240 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" H 1700 6050 50  0001 C CNN
F 3 "~" H 1700 6050 50  0001 C CNN
	1    1700 6050
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5E6E7A08
P 1700 6550
AR Path="/5E6E7A08" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E6E7A08" Ref="J6"  Part="1" 
F 0 "J6" H 1808 6731 50  0000 C CNN
F 1 "Conn_01x02_Male" H 1808 6640 50  0000 C CNN
F 2 "Connector_Wire:SolderWirePad_1x02_P7.62mm_Drill2mm" H 1700 6550 50  0001 C CNN
F 3 "~" H 1700 6550 50  0001 C CNN
	1    1700 6550
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x04_Male J?
U 1 1 5E6E7A14
P 3750 5550
AR Path="/5E6E7A14" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E6E7A14" Ref="J8"  Part="1" 
F 0 "J8" H 3858 5831 50  0000 C CNN
F 1 "Conn_01x04_Male" H 3858 5740 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" H 3750 5550 50  0001 C CNN
F 3 "~" H 3750 5550 50  0001 C CNN
	1    3750 5550
	0    -1   1    0   
$EndComp
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5E6E7A1A
P 3150 5550
AR Path="/5E6E7A1A" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E6E7A1A" Ref="J7"  Part="1" 
F 0 "J7" H 3258 5731 50  0000 C CNN
F 1 "Conn_01x02_Male" H 3258 5640 50  0000 C CNN
F 2 "Connector_Wire:SolderWirePad_1x02_P7.62mm_Drill2mm" H 3150 5550 50  0001 C CNN
F 3 "~" H 3150 5550 50  0001 C CNN
	1    3150 5550
	0    -1   1    0   
$EndComp
$Comp
L Transistor_FET:IRF540N Q?
U 1 1 5E6E7A20
P 2800 6750
AR Path="/5E6E7A20" Ref="Q?"  Part="1" 
AR Path="/5E6BD4F2/5E6E7A20" Ref="Q1"  Part="1" 
F 0 "Q1" V 3142 6750 50  0000 C CNN
F 1 "IRF540N" V 3051 6750 50  0000 C CNN
F 2 "Package_TO_SOT_THT:TO-220-3_Vertical" H 3050 6675 50  0001 L CIN
F 3 "http://www.irf.com/product-info/datasheets/data/irf540n.pdf" H 2800 6750 50  0001 L CNN
	1    2800 6750
	0    1    -1   0   
$EndComp
$Comp
L Device:R R?
U 1 1 5E97A703
P 2350 6800
AR Path="/5E97A703" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E97A703" Ref="R2"  Part="1" 
F 0 "R2" H 2420 6846 50  0000 L CNN
F 1 "10k" H 2420 6755 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 2280 6800 50  0001 C CNN
F 3 "~" H 2350 6800 50  0001 C CNN
	1    2350 6800
	1    0    0    -1  
$EndComp
Text GLabel 2450 7250 0    50   Input ~ 0
BCKP_EN
Text GLabel 4300 5950 2    50   Input ~ 0
BCKP_3S
Text GLabel 5500 5850 2    50   Input ~ 0
VCC
$Comp
L power:GND #PWR?
U 1 1 5E97A705
P 4200 6950
AR Path="/5E97A705" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A705" Ref="#PWR08"  Part="1" 
F 0 "#PWR08" H 4200 6700 50  0001 C CNN
F 1 "GND" H 4205 6777 50  0000 C CNN
F 2 "" H 4200 6950 50  0001 C CNN
F 3 "" H 4200 6950 50  0001 C CNN
	1    4200 6950
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x04_Male J?
U 1 1 5E97A706
P 1700 2400
AR Path="/5E97A706" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E97A706" Ref="J2"  Part="1" 
F 0 "J2" H 1808 2681 50  0000 C CNN
F 1 "Conn_01x04_Male" H 1808 2590 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" H 1700 2400 50  0001 C CNN
F 3 "~" H 1700 2400 50  0001 C CNN
	1    1700 2400
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x04_Male J?
U 1 1 5E97A707
P 1700 3700
AR Path="/5E97A707" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E97A707" Ref="J3"  Part="1" 
F 0 "J3" H 1808 3981 50  0000 C CNN
F 1 "Conn_01x04_Male" H 1808 3890 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_1x04_P2.54mm_Vertical" H 1700 3700 50  0001 C CNN
F 3 "~" H 1700 3700 50  0001 C CNN
	1    1700 3700
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5E762890
P 1700 1900
AR Path="/5E762890" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E762890" Ref="J1"  Part="1" 
F 0 "J1" H 1808 2081 50  0000 C CNN
F 1 "Conn_01x02_Male" H 1808 1990 50  0000 C CNN
F 2 "Connector_Wire:SolderWirePad_1x02_P7.62mm_Drill2mm" H 1700 1900 50  0001 C CNN
F 3 "~" H 1700 1900 50  0001 C CNN
	1    1700 1900
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5E762896
P 1700 4200
AR Path="/5E762896" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E762896" Ref="J4"  Part="1" 
F 0 "J4" H 1808 4381 50  0000 C CNN
F 1 "Conn_01x02_Male" H 1808 4290 50  0000 C CNN
F 2 "Connector_Wire:SolderWirePad_1x02_P7.62mm_Drill2mm" H 1700 4200 50  0001 C CNN
F 3 "~" H 1700 4200 50  0001 C CNN
	1    1700 4200
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E97A70A
P 3400 3100
AR Path="/5E97A70A" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E97A70A" Ref="R5"  Part="1" 
F 0 "R5" H 3470 3146 50  0000 L CNN
F 1 "10k" H 3470 3055 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3330 3100 50  0001 C CNN
F 3 "~" H 3400 3100 50  0001 C CNN
	1    3400 3100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E97A70B
P 2850 3100
AR Path="/5E97A70B" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E97A70B" Ref="R3"  Part="1" 
F 0 "R3" H 2920 3146 50  0000 L CNN
F 1 "10k" H 2920 3055 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 2780 3100 50  0001 C CNN
F 3 "~" H 2850 3100 50  0001 C CNN
	1    2850 3100
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7628AD
P 3100 3100
AR Path="/5E7628AD" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E7628AD" Ref="R4"  Part="1" 
F 0 "R4" H 3170 3146 50  0000 L CNN
F 1 "10k" H 3170 3055 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3030 3100 50  0001 C CNN
F 3 "~" H 3100 3100 50  0001 C CNN
	1    3100 3100
	1    0    0    -1  
$EndComp
$Comp
L TFG_PCB-rescue:FDD6685-SamacSys_Parts Q?
U 1 1 5E97A70D
P 4200 2200
AR Path="/5E97A70D" Ref="Q?"  Part="1" 
AR Path="/5E6BD4F2/5E97A70D" Ref="Q2"  Part="1" 
F 0 "Q2" V 4767 2300 50  0000 C CNN
F 1 "FDD6685" V 4676 2300 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:TO-252-3_TabPin2" H 4650 2150 50  0001 L CNN
F 3 "https://componentsearchengine.com/Datasheets/1/FDD6685.pdf" H 4650 2050 50  0001 L CNN
F 4 "Fairchild FDD6685 P-channel MOSFET Transistor, 11 A, -30 V, 3-Pin TO-252" H 4650 1950 50  0001 L CNN "Description"
F 5 "2.39" H 4650 1850 50  0001 L CNN "Height"
F 6 "512-FDD6685" H 4650 1750 50  0001 L CNN "Mouser Part Number"
F 7 "https://www.mouser.com/Search/Refine.aspx?Keyword=512-FDD6685" H 4650 1650 50  0001 L CNN "Mouser Price/Stock"
F 8 "ON Semiconductor" H 4650 1550 50  0001 L CNN "Manufacturer_Name"
F 9 "FDD6685" H 4650 1450 50  0001 L CNN "Manufacturer_Part_Number"
	1    4200 2200
	0    -1   -1   0   
$EndComp
$Comp
L TFG_PCB-rescue:FDD6685-SamacSys_Parts Q?
U 1 1 5E97A70E
P 4200 4500
AR Path="/5E97A70E" Ref="Q?"  Part="1" 
AR Path="/5E6BD4F2/5E97A70E" Ref="Q3"  Part="1" 
F 0 "Q3" V 4767 4600 50  0000 C CNN
F 1 "FDD6685" V 4676 4600 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:TO-252-3_TabPin2" H 4650 4450 50  0001 L CNN
F 3 "https://componentsearchengine.com/Datasheets/1/FDD6685.pdf" H 4650 4350 50  0001 L CNN
F 4 "Fairchild FDD6685 P-channel MOSFET Transistor, 11 A, -30 V, 3-Pin TO-252" H 4650 4250 50  0001 L CNN "Description"
F 5 "2.39" H 4650 4150 50  0001 L CNN "Height"
F 6 "512-FDD6685" H 4650 4050 50  0001 L CNN "Mouser Part Number"
F 7 "https://www.mouser.com/Search/Refine.aspx?Keyword=512-FDD6685" H 4650 3950 50  0001 L CNN "Mouser Price/Stock"
F 8 "ON Semiconductor" H 4650 3850 50  0001 L CNN "Manufacturer_Name"
F 9 "FDD6685" H 4650 3750 50  0001 L CNN "Manufacturer_Part_Number"
	1    4200 4500
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R?
U 1 1 5E97A70F
P 3650 2050
AR Path="/5E97A70F" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E97A70F" Ref="R6"  Part="1" 
F 0 "R6" H 3720 2096 50  0000 L CNN
F 1 "100k" H 3720 2005 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3580 2050 50  0001 C CNN
F 3 "~" H 3650 2050 50  0001 C CNN
	1    3650 2050
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E97A710
P 3650 4350
AR Path="/5E97A710" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E97A710" Ref="R7"  Part="1" 
F 0 "R7" H 3720 4396 50  0000 L CNN
F 1 "100k" H 3720 4305 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 3580 4350 50  0001 C CNN
F 3 "~" H 3650 4350 50  0001 C CNN
	1    3650 4350
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E7628E5
P 4200 2400
AR Path="/5E7628E5" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E7628E5" Ref="#PWR03"  Part="1" 
F 0 "#PWR03" H 4200 2150 50  0001 C CNN
F 1 "GND" H 4205 2227 50  0000 C CNN
F 2 "" H 4200 2400 50  0001 C CNN
F 3 "" H 4200 2400 50  0001 C CNN
	1    4200 2400
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E7628FE
P 4200 4700
AR Path="/5E7628FE" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E7628FE" Ref="#PWR05"  Part="1" 
F 0 "#PWR05" H 4200 4450 50  0001 C CNN
F 1 "GND" H 4205 4527 50  0000 C CNN
F 2 "" H 4200 4700 50  0001 C CNN
F 3 "" H 4200 4700 50  0001 C CNN
	1    4200 4700
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_01x04_Male J?
U 1 1 5E762905
P 5250 1600
AR Path="/5E762905" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E762905" Ref="J13"  Part="1" 
F 0 "J13" H 5358 1881 50  0000 C CNN
F 1 "Conn_01x04_Male" H 5358 1790 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 5250 1600 50  0001 C CNN
F 3 "~" H 5250 1600 50  0001 C CNN
	1    5250 1600
	0    -1   1    0   
$EndComp
$Comp
L Connector:Conn_01x04_Male J?
U 1 1 5E97A714
P 5250 3400
AR Path="/5E97A714" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E97A714" Ref="J15"  Part="1" 
F 0 "J15" H 5358 3681 50  0000 C CNN
F 1 "Conn_01x04_Male" H 5358 3590 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 5250 3400 50  0001 C CNN
F 3 "~" H 5250 3400 50  0001 C CNN
	1    5250 3400
	0    -1   1    0   
$EndComp
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5E97A715
P 4650 1600
AR Path="/5E97A715" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E97A715" Ref="J9"  Part="1" 
F 0 "J9" H 4758 1781 50  0000 C CNN
F 1 "Conn_01x02_Male" H 4758 1690 50  0000 C CNN
F 2 "Connector_Wire:SolderWirePad_1x02_P7.62mm_Drill2mm" H 4650 1600 50  0001 C CNN
F 3 "~" H 4650 1600 50  0001 C CNN
	1    4650 1600
	0    -1   1    0   
$EndComp
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5E762934
P 4650 3900
AR Path="/5E762934" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E762934" Ref="J10"  Part="1" 
F 0 "J10" H 4758 4081 50  0000 C CNN
F 1 "Conn_01x02_Male" H 4758 3990 50  0000 C CNN
F 2 "Connector_Wire:SolderWirePad_1x02_P7.62mm_Drill2mm" H 4650 3900 50  0001 C CNN
F 3 "~" H 4650 3900 50  0001 C CNN
	1    4650 3900
	0    -1   1    0   
$EndComp
$Comp
L Device:L L?
U 1 1 5E97A71C
P 9300 4750
AR Path="/5E97A71C" Ref="L?"  Part="1" 
AR Path="/5E6BD4F2/5E97A71C" Ref="L2"  Part="1" 
F 0 "L2" V 9490 4750 50  0000 C CNN
F 1 "15u" V 9399 4750 50  0000 C CNN
F 2 "Inductor_SMD:L_7.3x7.3_H3.5" H 9300 4750 50  0001 C CNN
F 3 "~" H 9300 4750 50  0001 C CNN
	1    9300 4750
	0    -1   -1   0   
$EndComp
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5E97A71D
P 6200 1600
AR Path="/5E97A71D" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E97A71D" Ref="J16"  Part="1" 
F 0 "J16" H 6308 1781 50  0000 C CNN
F 1 "Conn_01x02_Male" H 6308 1690 50  0000 C CNN
F 2 "Connector_Wire:SolderWirePad_1x02_P7.62mm_Drill2mm" H 6200 1600 50  0001 C CNN
F 3 "~" H 6200 1600 50  0001 C CNN
	1    6200 1600
	0    -1   1    0   
$EndComp
$Comp
L Connector:Conn_01x02_Male J?
U 1 1 5E97A71E
P 6600 1600
AR Path="/5E97A71E" Ref="J?"  Part="1" 
AR Path="/5E6BD4F2/5E97A71E" Ref="J17"  Part="1" 
F 0 "J17" H 6708 1781 50  0000 C CNN
F 1 "Conn_01x02_Male" H 6708 1690 50  0000 C CNN
F 2 "Connector_Wire:SolderWirePad_1x02_P7.62mm_Drill2mm" H 6600 1600 50  0001 C CNN
F 3 "~" H 6600 1600 50  0001 C CNN
	1    6600 1600
	0    -1   1    0   
$EndComp
$Comp
L Regulator_Linear:L78L05_SOT89 U?
U 1 1 5E97A71F
P 6150 2700
AR Path="/5E97A71F" Ref="U?"  Part="1" 
AR Path="/5E6BD4F2/5E97A71F" Ref="U1"  Part="1" 
F 0 "U1" H 6150 2942 50  0000 C CNN
F 1 "L78L05_SOT89" H 6150 2851 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-89-3" H 6150 2900 50  0001 C CIN
F 3 "http://www.st.com/content/ccc/resource/technical/document/datasheet/15/55/e5/aa/23/5b/43/fd/CD00000446.pdf/files/CD00000446.pdf/jcr:content/translations/en.CD00000446.pdf" H 6150 2650 50  0001 C CNN
	1    6150 2700
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E97A720
P 6150 3000
AR Path="/5E97A720" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A720" Ref="#PWR012"  Part="1" 
F 0 "#PWR012" H 6150 2750 50  0001 C CNN
F 1 "GND" H 6155 2827 50  0000 C CNN
F 2 "" H 6150 3000 50  0001 C CNN
F 3 "" H 6150 3000 50  0001 C CNN
	1    6150 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5E97A721
P 5700 2850
AR Path="/5E97A721" Ref="C?"  Part="1" 
AR Path="/5E6BD4F2/5E97A721" Ref="C1"  Part="1" 
F 0 "C1" H 5815 2896 50  0000 L CNN
F 1 "10u" H 5815 2805 50  0000 L CNN
F 2 "Capacitor_SMD:C_2512_6332Metric_Pad1.52x3.35mm_HandSolder" H 5738 2700 50  0001 C CNN
F 3 "~" H 5700 2850 50  0001 C CNN
	1    5700 2850
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E97A722
P 5700 3000
AR Path="/5E97A722" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A722" Ref="#PWR010"  Part="1" 
F 0 "#PWR010" H 5700 2750 50  0001 C CNN
F 1 "GND" H 5705 2827 50  0000 C CNN
F 2 "" H 5700 3000 50  0001 C CNN
F 3 "" H 5700 3000 50  0001 C CNN
	1    5700 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5E97A723
P 6600 2850
AR Path="/5E97A723" Ref="C?"  Part="1" 
AR Path="/5E6BD4F2/5E97A723" Ref="C2"  Part="1" 
F 0 "C2" H 6715 2896 50  0000 L CNN
F 1 "10u" H 6715 2805 50  0000 L CNN
F 2 "Capacitor_SMD:C_2512_6332Metric_Pad1.52x3.35mm_HandSolder" H 6638 2700 50  0001 C CNN
F 3 "~" H 6600 2850 50  0001 C CNN
	1    6600 2850
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E97A724
P 6600 3000
AR Path="/5E97A724" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A724" Ref="#PWR014"  Part="1" 
F 0 "#PWR014" H 6600 2750 50  0001 C CNN
F 1 "GND" H 6605 2827 50  0000 C CNN
F 2 "" H 6600 3000 50  0001 C CNN
F 3 "" H 6600 3000 50  0001 C CNN
	1    6600 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7629BD
P 9900 4350
AR Path="/5E7629BD" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E7629BD" Ref="R11"  Part="1" 
F 0 "R11" H 9970 4396 50  0000 L CNN
F 1 "68k" H 9970 4305 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 9830 4350 50  0001 C CNN
F 3 "~" H 9900 4350 50  0001 C CNN
	1    9900 4350
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7629C9
P 10150 4100
AR Path="/5E7629C9" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E7629C9" Ref="R13"  Part="1" 
F 0 "R13" V 9943 4100 50  0000 C CNN
F 1 "22k" V 10034 4100 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 10080 4100 50  0001 C CNN
F 3 "~" H 10150 4100 50  0001 C CNN
	1    10150 4100
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E97A72A
P 10400 4150
AR Path="/5E97A72A" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A72A" Ref="#PWR040"  Part="1" 
F 0 "#PWR040" H 10400 3900 50  0001 C CNN
F 1 "GND" H 10405 3977 50  0000 C CNN
F 2 "" H 10400 4150 50  0001 C CNN
F 3 "" H 10400 4150 50  0001 C CNN
	1    10400 4150
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR?
U 1 1 5E7629F3
P 9550 4750
AR Path="/5E7629F3" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E7629F3" Ref="#PWR027"  Part="1" 
F 0 "#PWR027" H 9550 4600 50  0001 C CNN
F 1 "+5V" H 9565 4923 50  0000 C CNN
F 2 "" H 9550 4750 50  0001 C CNN
F 3 "" H 9550 4750 50  0001 C CNN
	1    9550 4750
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E7629FB
P 9700 4300
AR Path="/5E7629FB" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E7629FB" Ref="#PWR031"  Part="1" 
F 0 "#PWR031" H 9700 4050 50  0001 C CNN
F 1 "GND" H 9705 4127 50  0000 C CNN
F 2 "" H 9700 4300 50  0001 C CNN
F 3 "" H 9700 4300 50  0001 C CNN
	1    9700 4300
	1    0    0    -1  
$EndComp
Text GLabel 4050 2850 2    50   Input ~ 0
BAT1_3S
Text GLabel 4050 2950 2    50   Input ~ 0
BAT1_2S
Text GLabel 4050 3050 2    50   Input ~ 0
BAT1_1S
Text GLabel 4050 3350 2    50   Input ~ 0
BAT2_3S
Text GLabel 4050 3450 2    50   Input ~ 0
BAT2_2S
Text GLabel 4050 3550 2    50   Input ~ 0
BAT2_1S
Text GLabel 10700 4750 2    50   Input ~ 0
5V_HP
$Comp
L power:GND #PWR?
U 1 1 5E762A34
P 8100 5000
AR Path="/5E762A34" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E762A34" Ref="#PWR019"  Part="1" 
F 0 "#PWR019" H 8100 4750 50  0001 C CNN
F 1 "GND" H 8105 4827 50  0000 C CNN
F 2 "" H 8100 5000 50  0001 C CNN
F 3 "" H 8100 5000 50  0001 C CNN
	1    8100 5000
	1    0    0    -1  
$EndComp
Text GLabel 7150 2700 2    50   Input ~ 0
5V_LP
$Comp
L power:+5VL #PWR?
U 1 1 5E762A42
P 6850 2700
AR Path="/5E762A42" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E762A42" Ref="#PWR015"  Part="1" 
F 0 "#PWR015" H 6850 2550 50  0001 C CNN
F 1 "+5VL" H 6865 2873 50  0000 C CNN
F 2 "" H 6850 2700 50  0001 C CNN
F 3 "" H 6850 2700 50  0001 C CNN
	1    6850 2700
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E762A61
P 8100 4500
AR Path="/5E762A61" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E762A61" Ref="R9"  Part="1" 
F 0 "R9" H 8170 4546 50  0000 L CNN
F 1 "10k" H 8170 4455 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8030 4500 50  0001 C CNN
F 3 "~" H 8100 4500 50  0001 C CNN
	1    8100 4500
	1    0    0    -1  
$EndComp
$Comp
L power:+5VL #PWR?
U 1 1 5E97A735
P 8350 3550
AR Path="/5E97A735" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A735" Ref="#PWR022"  Part="1" 
F 0 "#PWR022" H 8350 3400 50  0001 C CNN
F 1 "+5VL" H 8365 3723 50  0000 C CNN
F 2 "" H 8350 3550 50  0001 C CNN
F 3 "" H 8350 3550 50  0001 C CNN
	1    8350 3550
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5E97A739
P 9550 4900
AR Path="/5E97A739" Ref="C?"  Part="1" 
AR Path="/5E6BD4F2/5E97A739" Ref="C6"  Part="1" 
F 0 "C6" H 9665 4946 50  0000 L CNN
F 1 "470u" H 9665 4855 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm" H 9588 4750 50  0001 C CNN
F 3 "~" H 9550 4900 50  0001 C CNN
	1    9550 4900
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5E97A73A
P 9950 4900
AR Path="/5E97A73A" Ref="C?"  Part="1" 
AR Path="/5E6BD4F2/5E97A73A" Ref="C8"  Part="1" 
F 0 "C8" H 10065 4946 50  0000 L CNN
F 1 "470u" H 10065 4855 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm" H 9988 4750 50  0001 C CNN
F 3 "~" H 9950 4900 50  0001 C CNN
	1    9950 4900
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5E97A73B
P 10350 4900
AR Path="/5E97A73B" Ref="C?"  Part="1" 
AR Path="/5E6BD4F2/5E97A73B" Ref="C10"  Part="1" 
F 0 "C10" H 10465 4946 50  0000 L CNN
F 1 "10u" H 10465 4855 50  0000 L CNN
F 2 "Diode_SMD:D_2512_6332Metric_Pad1.52x3.35mm_HandSolder" H 10388 4750 50  0001 C CNN
F 3 "~" H 10350 4900 50  0001 C CNN
	1    10350 4900
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E97A73D
P 9950 5050
AR Path="/5E97A73D" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A73D" Ref="#PWR036"  Part="1" 
F 0 "#PWR036" H 9950 4800 50  0001 C CNN
F 1 "GND" H 9955 4877 50  0000 C CNN
F 2 "" H 9950 5050 50  0001 C CNN
F 3 "" H 9950 5050 50  0001 C CNN
	1    9950 5050
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5E97A73E
P 7200 4250
AR Path="/5E97A73E" Ref="C?"  Part="1" 
AR Path="/5E6BD4F2/5E97A73E" Ref="C3"  Part="1" 
F 0 "C3" H 7315 4296 50  0000 L CNN
F 1 "470u" H 7315 4205 50  0000 L CNN
F 2 "Capacitor_SMD:CP_Elec_10x12.5" H 7238 4100 50  0001 C CNN
F 3 "~" H 7200 4250 50  0001 C CNN
	1    7200 4250
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5E97A73F
P 7600 4250
AR Path="/5E97A73F" Ref="C?"  Part="1" 
AR Path="/5E6BD4F2/5E97A73F" Ref="C4"  Part="1" 
F 0 "C4" H 7715 4296 50  0000 L CNN
F 1 "470u" H 7715 4205 50  0000 L CNN
F 2 "Capacitor_SMD:CP_Elec_10x12.5" H 7638 4100 50  0001 C CNN
F 3 "~" H 7600 4250 50  0001 C CNN
	1    7600 4250
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E97A741
P 2250 3250
AR Path="/5E97A741" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A741" Ref="#PWR02"  Part="1" 
F 0 "#PWR02" H 2250 3000 50  0001 C CNN
F 1 "GND" H 2255 3077 50  0000 C CNN
F 2 "" H 2250 3250 50  0001 C CNN
F 3 "" H 2250 3250 50  0001 C CNN
	1    2250 3250
	1    0    0    -1  
$EndComp
Text HLabel 7150 2850 2    50   Output ~ 0
5V_LP
Text HLabel 10700 4900 2    50   Output ~ 0
5V_HP
Wire Wire Line
	10700 4900 10650 4900
Wire Wire Line
	10650 4900 10650 4750
Connection ~ 10650 4750
Wire Wire Line
	10650 4750 10700 4750
Wire Wire Line
	7150 2850 7100 2850
Wire Wire Line
	7100 2850 7100 2700
Connection ~ 7100 2700
Wire Wire Line
	7100 2700 6850 2700
Text HLabel 2450 7400 0    50   Output ~ 0
BCKP_EN
Wire Wire Line
	2450 7400 2600 7400
Wire Wire Line
	2600 7400 2600 7250
Connection ~ 2600 7250
Wire Wire Line
	6600 1900 7450 1900
$Comp
L Device:R R?
U 1 1 5E5FD2A2
P 8350 3850
AR Path="/5E5FD2A2" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E5FD2A2" Ref="R15"  Part="1" 
F 0 "R15" H 8420 3896 50  0000 L CNN
F 1 "10k" H 8420 3805 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8280 3850 50  0001 C CNN
F 3 "~" H 8350 3850 50  0001 C CNN
	1    8350 3850
	1    0    0    -1  
$EndComp
Wire Wire Line
	8350 3700 8350 3550
Connection ~ 8350 3550
Wire Wire Line
	8350 4000 8350 4300
Wire Wire Line
	8100 4300 8350 4300
Connection ~ 8350 4300
Wire Wire Line
	8350 4300 8550 4300
$Comp
L power:+5VL #PWR?
U 1 1 5E97A734
P 8800 700
AR Path="/5E97A734" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A734" Ref="#PWR024"  Part="1" 
F 0 "#PWR024" H 8800 550 50  0001 C CNN
F 1 "+5VL" H 8815 873 50  0000 C CNN
F 2 "" H 8800 700 50  0001 C CNN
F 3 "" H 8800 700 50  0001 C CNN
	1    8800 700 
	1    0    0    -1  
$EndComp
Text GLabel 7600 1550 2    50   Input ~ 0
VCC
Text HLabel 7600 1700 2    50   Output ~ 0
VCC
$Comp
L power:+5VL #PWR?
U 1 1 5E762A7A
P 8800 700
AR Path="/5E762A7A" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E762A7A" Ref="#PWR023"  Part="1" 
F 0 "#PWR023" H 8800 550 50  0001 C CNN
F 1 "+5VL" H 8815 873 50  0000 C CNN
F 2 "" H 8800 700 50  0001 C CNN
F 3 "" H 8800 700 50  0001 C CNN
	1    8800 700 
	1    0    0    -1  
$EndComp
Text GLabel 7600 1550 2    50   Input ~ 0
VCC
Text HLabel 7600 1700 2    50   Output ~ 0
VCC
Connection ~ 8800 700 
Wire Wire Line
	8550 4100 7950 4100
Wire Wire Line
	7950 4100 7600 4100
Connection ~ 7450 1900
Connection ~ 7950 4100
Wire Wire Line
	9550 2100 9700 2100
Wire Wire Line
	9900 2000 9900 1900
Wire Wire Line
	9900 1900 10000 1900
Wire Wire Line
	9900 2300 9900 2550
Wire Wire Line
	9900 2550 9550 2550
Wire Wire Line
	9900 1900 9550 1900
Connection ~ 9900 1900
$Comp
L power:GND #PWR?
U 1 1 5E7629DB
P 10400 1950
AR Path="/5E7629DB" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E7629DB" Ref="#PWR037"  Part="1" 
F 0 "#PWR037" H 10400 1700 50  0001 C CNN
F 1 "GND" H 10405 1777 50  0000 C CNN
F 2 "" H 10400 1950 50  0001 C CNN
F 3 "" H 10400 1950 50  0001 C CNN
	1    10400 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	10300 1900 10400 1900
Wire Wire Line
	10400 1900 10400 1950
$Comp
L power:+9V #PWR?
U 1 1 5E97A72B
P 9550 2550
AR Path="/5E97A72B" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A72B" Ref="#PWR026"  Part="1" 
F 0 "#PWR026" H 9550 2400 50  0001 C CNN
F 1 "+9V" H 9565 2723 50  0000 C CNN
F 2 "" H 9550 2550 50  0001 C CNN
F 3 "" H 9550 2550 50  0001 C CNN
	1    9550 2550
	1    0    0    -1  
$EndComp
Connection ~ 9550 2550
Wire Wire Line
	9550 2550 9450 2550
Text GLabel 10700 2550 2    50   Input ~ 0
9V_HP
Connection ~ 9900 2550
Wire Wire Line
	8150 2550 8100 2550
Wire Wire Line
	8100 2550 8100 2650
Wire Wire Line
	8100 2650 8150 2650
Connection ~ 7950 1900
Wire Wire Line
	7950 1900 8550 1900
Wire Wire Line
	8400 2100 8550 2100
Wire Wire Line
	7450 1900 7950 1900
Wire Wire Line
	7950 1900 7950 4100
$Comp
L power:GND #PWR?
U 1 1 5E762A59
P 8100 2800
AR Path="/5E762A59" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E762A59" Ref="#PWR017"  Part="1" 
F 0 "#PWR017" H 8100 2550 50  0001 C CNN
F 1 "GND" H 8105 2627 50  0000 C CNN
F 2 "" H 8100 2800 50  0001 C CNN
F 3 "" H 8100 2800 50  0001 C CNN
	1    8100 2800
	1    0    0    -1  
$EndComp
Wire Wire Line
	8100 2800 8100 2650
Connection ~ 8100 2650
Wire Wire Line
	8100 2450 8100 2650
Wire Wire Line
	8400 2100 8100 2100
Wire Wire Line
	8100 2100 8100 2150
Connection ~ 8400 2100
Wire Wire Line
	8800 1400 8800 1600
Wire Wire Line
	8800 1600 8400 1600
Wire Wire Line
	8400 1600 8400 2100
Text GLabel 8050 1100 0    50   Input ~ 0
9V_HP_EN
Wire Wire Line
	8150 1100 8050 1100
$Comp
L power:GND #PWR?
U 1 1 5E762AB2
P 9950 2850
AR Path="/5E762AB2" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E762AB2" Ref="#PWR033"  Part="1" 
F 0 "#PWR033" H 9950 2600 50  0001 C CNN
F 1 "GND" H 9955 2677 50  0000 C CNN
F 2 "" H 9950 2850 50  0001 C CNN
F 3 "" H 9950 2850 50  0001 C CNN
	1    9950 2850
	1    0    0    -1  
$EndComp
Connection ~ 10350 2550
Wire Wire Line
	9900 2550 9950 2550
Connection ~ 9950 2550
Wire Wire Line
	9950 2550 10350 2550
Connection ~ 9950 2850
Wire Wire Line
	9550 2850 9950 2850
Wire Wire Line
	9950 2850 10350 2850
Wire Wire Line
	10350 2550 10650 2550
$Comp
L power:GND #PWR?
U 1 1 5E762AE2
P 9700 2100
AR Path="/5E762AE2" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E762AE2" Ref="#PWR029"  Part="1" 
F 0 "#PWR029" H 9700 1850 50  0001 C CNN
F 1 "GND" H 9705 1927 50  0000 C CNN
F 2 "" H 9700 2100 50  0001 C CNN
F 3 "" H 9700 2100 50  0001 C CNN
	1    9700 2100
	1    0    0    -1  
$EndComp
$Comp
L TFG_PCB-rescue:TD7590_2-Regulator_Switching U?
U 1 1 5E97A717
P 9050 2000
AR Path="/5E97A717" Ref="U?"  Part="1" 
AR Path="/5E6BD4F2/5E97A717" Ref="U2"  Part="1" 
F 0 "U2" H 9050 2367 50  0000 C CNN
F 1 "TD7590_2" H 9050 2276 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:TO-263-5_TabPin3" H 9050 1750 50  0001 L CIN
F 3 "http://www.ti.com/lit/ds/symlink/lm2576.pdf" H 9050 2000 50  0001 C CNN
	1    9050 2000
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E97A725
P 9900 2150
AR Path="/5E97A725" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E97A725" Ref="R10"  Part="1" 
F 0 "R10" H 9970 2196 50  0000 L CNN
F 1 "300k" H 9970 2105 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 9830 2150 50  0001 C CNN
F 3 "~" H 9900 2150 50  0001 C CNN
	1    9900 2150
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E7629C3
P 10150 1900
AR Path="/5E7629C3" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E7629C3" Ref="R12"  Part="1" 
F 0 "R12" V 9943 1900 50  0000 C CNN
F 1 "47k" V 10034 1900 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 10080 1900 50  0001 C CNN
F 3 "~" H 10150 1900 50  0001 C CNN
	1    10150 1900
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E97A729
P 10400 1950
AR Path="/5E97A729" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A729" Ref="#PWR038"  Part="1" 
F 0 "#PWR038" H 10400 1700 50  0001 C CNN
F 1 "GND" H 10405 1777 50  0000 C CNN
F 2 "" H 10400 1950 50  0001 C CNN
F 3 "" H 10400 1950 50  0001 C CNN
	1    10400 1950
	1    0    0    -1  
$EndComp
$Comp
L power:+9V #PWR?
U 1 1 5E7629EB
P 9550 2550
AR Path="/5E7629EB" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E7629EB" Ref="#PWR025"  Part="1" 
F 0 "#PWR025" H 9550 2400 50  0001 C CNN
F 1 "+9V" H 9565 2723 50  0000 C CNN
F 2 "" H 9550 2550 50  0001 C CNN
F 3 "" H 9550 2550 50  0001 C CNN
	1    9550 2550
	1    0    0    -1  
$EndComp
Text GLabel 10700 2550 2    50   Input ~ 0
9V_HP
$Comp
L power:GND #PWR?
U 1 1 5E97A730
P 8100 2800
AR Path="/5E97A730" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A730" Ref="#PWR018"  Part="1" 
F 0 "#PWR018" H 8100 2550 50  0001 C CNN
F 1 "GND" H 8105 2627 50  0000 C CNN
F 2 "" H 8100 2800 50  0001 C CNN
F 3 "" H 8100 2800 50  0001 C CNN
	1    8100 2800
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E762A68
P 8100 2300
AR Path="/5E762A68" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E762A68" Ref="R8"  Part="1" 
F 0 "R8" H 8170 2346 50  0000 L CNN
F 1 "10k" H 8170 2255 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8030 2300 50  0001 C CNN
F 3 "~" H 8100 2300 50  0001 C CNN
	1    8100 2300
	1    0    0    -1  
$EndComp
Text GLabel 8050 1100 0    50   Input ~ 0
9V_HP_EN
$Comp
L Device:C C?
U 1 1 5E97A736
P 9550 2700
AR Path="/5E97A736" Ref="C?"  Part="1" 
AR Path="/5E6BD4F2/5E97A736" Ref="C5"  Part="1" 
F 0 "C5" H 9665 2746 50  0000 L CNN
F 1 "470u" H 9665 2655 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm" H 9588 2550 50  0001 C CNN
F 3 "~" H 9550 2700 50  0001 C CNN
	1    9550 2700
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5E97A737
P 9950 2700
AR Path="/5E97A737" Ref="C?"  Part="1" 
AR Path="/5E6BD4F2/5E97A737" Ref="C7"  Part="1" 
F 0 "C7" H 10065 2746 50  0000 L CNN
F 1 "470u" H 10065 2655 50  0000 L CNN
F 2 "Capacitor_THT:CP_Radial_D10.0mm_P5.00mm" H 9988 2550 50  0001 C CNN
F 3 "~" H 9950 2700 50  0001 C CNN
	1    9950 2700
	1    0    0    -1  
$EndComp
$Comp
L Device:C C?
U 1 1 5E97A738
P 10350 2700
AR Path="/5E97A738" Ref="C?"  Part="1" 
AR Path="/5E6BD4F2/5E97A738" Ref="C9"  Part="1" 
F 0 "C9" H 10465 2746 50  0000 L CNN
F 1 "10u" H 10465 2655 50  0000 L CNN
F 2 "Diode_SMD:D_2512_6332Metric_Pad1.52x3.35mm_HandSolder" H 10388 2550 50  0001 C CNN
F 3 "~" H 10350 2700 50  0001 C CNN
	1    10350 2700
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E97A73C
P 9950 2850
AR Path="/5E97A73C" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A73C" Ref="#PWR034"  Part="1" 
F 0 "#PWR034" H 9950 2600 50  0001 C CNN
F 1 "GND" H 9955 2677 50  0000 C CNN
F 2 "" H 9950 2850 50  0001 C CNN
F 3 "" H 9950 2850 50  0001 C CNN
	1    9950 2850
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 5E97A740
P 9700 2100
AR Path="/5E97A740" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E97A740" Ref="#PWR030"  Part="1" 
F 0 "#PWR030" H 9700 1850 50  0001 C CNN
F 1 "GND" H 9705 1927 50  0000 C CNN
F 2 "" H 9700 2100 50  0001 C CNN
F 3 "" H 9700 2100 50  0001 C CNN
	1    9700 2100
	1    0    0    -1  
$EndComp
Text HLabel 10700 2700 2    50   Output ~ 0
9V_HP
Wire Wire Line
	10700 2700 10650 2700
Wire Wire Line
	10650 2700 10650 2550
Connection ~ 10650 2550
Wire Wire Line
	10650 2550 10700 2550
Text HLabel 8050 1250 0    50   Output ~ 0
9V_HP_EN
Wire Wire Line
	8050 1250 8150 1250
$Comp
L Transistor_FET:2N7002 Q?
U 1 1 5E97A733
P 8700 1200
AR Path="/5E97A733" Ref="Q?"  Part="1" 
AR Path="/5E6BD4F2/5E97A733" Ref="Q4"  Part="1" 
F 0 "Q4" H 8904 1246 50  0000 L CNN
F 1 "2N7002" H 8904 1155 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:SOT-23" H 8900 1125 50  0001 L CIN
F 3 "https://www.fairchildsemi.com/datasheets/2N/2N7002.pdf" H 8700 1200 50  0001 L CNN
	1    8700 1200
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E586C94
P 8300 1400
AR Path="/5E586C94" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E586C94" Ref="R14"  Part="1" 
F 0 "R14" H 8370 1446 50  0000 L CNN
F 1 "10k" H 8370 1355 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8230 1400 50  0001 C CNN
F 3 "~" H 8300 1400 50  0001 C CNN
	1    8300 1400
	1    0    0    -1  
$EndComp
$Comp
L Device:R R?
U 1 1 5E588A0C
P 8300 1000
AR Path="/5E588A0C" Ref="R?"  Part="1" 
AR Path="/5E6BD4F2/5E588A0C" Ref="R1"  Part="1" 
F 0 "R1" H 8370 1046 50  0000 L CNN
F 1 "10k" H 8370 955 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder" V 8230 1000 50  0001 C CNN
F 3 "~" H 8300 1000 50  0001 C CNN
	1    8300 1000
	1    0    0    -1  
$EndComp
Wire Wire Line
	8300 850  8800 850 
Wire Wire Line
	8800 850  8800 700 
Wire Wire Line
	8800 850  8800 1000
Connection ~ 8800 850 
Wire Wire Line
	8300 1250 8300 1200
Wire Wire Line
	8500 1200 8300 1200
Connection ~ 8300 1200
Wire Wire Line
	8300 1200 8300 1150
Wire Wire Line
	8150 1100 8150 1200
Wire Wire Line
	8300 1200 8150 1200
Connection ~ 8150 1200
Wire Wire Line
	8150 1200 8150 1250
$Comp
L power:GND #PWR?
U 1 1 5E5E2DD3
P 8300 1550
AR Path="/5E5E2DD3" Ref="#PWR?"  Part="1" 
AR Path="/5E6BD4F2/5E5E2DD3" Ref="#PWR0101"  Part="1" 
F 0 "#PWR0101" H 8300 1300 50  0001 C CNN
F 1 "GND" H 8305 1377 50  0000 C CNN
F 2 "" H 8300 1550 50  0001 C CNN
F 3 "" H 8300 1550 50  0001 C CNN
	1    8300 1550
	1    0    0    -1  
$EndComp
$Comp
L TFG_PCB-rescue:SDT5100LP5-13-SamacSys_Parts D?
U 1 1 5E97A71A
P 8150 4750
AR Path="/5E97A71A" Ref="D?"  Part="1" 
AR Path="/5E6BD4F2/5E97A71A" Ref="D2"  Part="1" 
F 0 "D2" H 8600 5015 50  0000 C CNN
F 1 "SDT5100LP5-13" H 8600 4924 50  0000 C CNN
F 2 "Diode_SMD:D_PowerDI-5" H 8900 4850 50  0001 L CNN
F 3 "https://componentsearchengine.com/Datasheets/1/SDT5100LP5-13.pdf" H 8900 4750 50  0001 L CNN
F 4 "5A TRENCH SCHOTTKY BARRIER RECTIFIER PowerDI5" H 8900 4650 50  0001 L CNN "Description"
F 5 "1" H 8900 4550 50  0001 L CNN "Height"
F 6 "621-SDT5100LP5-13" H 8900 4450 50  0001 L CNN "Mouser Part Number"
F 7 "https://www.mouser.com/Search/Refine.aspx?Keyword=621-SDT5100LP5-13" H 8900 4350 50  0001 L CNN "Mouser Price/Stock"
F 8 "Diodes Inc." H 8900 4250 50  0001 L CNN "Manufacturer_Name"
F 9 "SDT5100LP5-13" H 8900 4150 50  0001 L CNN "Manufacturer_Part_Number"
	1    8150 4750
	1    0    0    -1  
$EndComp
$Comp
L TFG_PCB-rescue:SDT5100LP5-13-SamacSys_Parts D?
U 1 1 5E97A719
P 8150 2550
AR Path="/5E97A719" Ref="D?"  Part="1" 
AR Path="/5E6BD4F2/5E97A719" Ref="D1"  Part="1" 
F 0 "D1" H 8600 2815 50  0000 C CNN
F 1 "SDT5100LP5-13" H 8600 2724 50  0000 C CNN
F 2 "Diode_SMD:D_PowerDI-5" H 8900 2650 50  0001 L CNN
F 3 "https://componentsearchengine.com/Datasheets/1/SDT5100LP5-13.pdf" H 8900 2550 50  0001 L CNN
F 4 "5A TRENCH SCHOTTKY BARRIER RECTIFIER PowerDI5" H 8900 2450 50  0001 L CNN "Description"
F 5 "1" H 8900 2350 50  0001 L CNN "Height"
F 6 "621-SDT5100LP5-13" H 8900 2250 50  0001 L CNN "Mouser Part Number"
F 7 "https://www.mouser.com/Search/Refine.aspx?Keyword=621-SDT5100LP5-13" H 8900 2150 50  0001 L CNN "Mouser Price/Stock"
F 8 "Diodes Inc." H 8900 2050 50  0001 L CNN "Manufacturer_Name"
F 9 "SDT5100LP5-13" H 8900 1950 50  0001 L CNN "Manufacturer_Part_Number"
	1    8150 2550
	1    0    0    -1  
$EndComp
$Comp
L Device:L L?
U 1 1 5E97A71B
P 9300 2550
AR Path="/5E97A71B" Ref="L?"  Part="1" 
AR Path="/5E6BD4F2/5E97A71B" Ref="L1"  Part="1" 
F 0 "L1" V 9490 2550 50  0000 C CNN
F 1 "15u" V 9399 2550 50  0000 C CNN
F 2 "Inductor_SMD:L_7.3x7.3_H3.5" H 9300 2550 50  0001 C CNN
F 3 "~" H 9300 2550 50  0001 C CNN
	1    9300 2550
	0    -1   -1   0   
$EndComp
Wire Wire Line
	9050 2300 9050 2550
Wire Wire Line
	9050 4750 9050 4500
$Comp
L TFG_PCB-rescue:TD7590_2-Regulator_Switching U?
U 1 1 5E97A718
P 9050 4200
AR Path="/5E97A718" Ref="U?"  Part="1" 
AR Path="/5E6BD4F2/5E97A718" Ref="U3"  Part="1" 
F 0 "U3" H 9050 4567 50  0000 C CNN
F 1 "TD7590_2" H 9050 4476 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:TO-263-5_TabPin3" H 9050 3950 50  0001 L CIN
F 3 "http://www.ti.com/lit/ds/symlink/lm2576.pdf" H 9050 4200 50  0001 C CNN
	1    9050 4200
	1    0    0    -1  
$EndComp
Connection ~ 9050 4750
Wire Wire Line
	9050 4750 9150 4750
Wire Wire Line
	9050 2550 9150 2550
Connection ~ 9050 2550
$EndSCHEMATC
