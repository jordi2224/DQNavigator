EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 3
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
F 2 "" H 3700 3450 50  0001 C CNN
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
Entry Wire Line
	9200 2650 9300 2750
Entry Wire Line
	9200 2750 9300 2850
Entry Wire Line
	9200 2950 9300 3050
Entry Wire Line
	9200 3050 9300 3150
Entry Wire Line
	9200 3150 9300 3250
Entry Wire Line
	9200 3250 9300 3350
Entry Wire Line
	9200 3350 9300 3450
Entry Wire Line
	9200 3450 9300 3550
Entry Wire Line
	9200 3550 9300 3650
Entry Wire Line
	9200 3650 9300 3750
Wire Wire Line
	9200 3250 8850 3250
Wire Wire Line
	8850 3350 9200 3350
Wire Wire Line
	8850 3450 9200 3450
Wire Wire Line
	8850 3550 9200 3550
Wire Wire Line
	8850 3650 9200 3650
Text Label 8850 2650 0    50   ~ 0
BAT1_2S
Text Label 8850 2750 0    50   ~ 0
BAT1_1S
Text Label 8850 2850 0    50   ~ 0
BAT2_2S
Text Label 8850 2950 0    50   ~ 0
BAT2_1S
Text Label 8850 3050 0    50   ~ 0
9V_HP
Text Label 8850 3150 0    50   ~ 0
5V_HP
Text HLabel 6700 1900 0    50   Output ~ 0
9V_HP
Wire Wire Line
	7250 2350 7250 1900
Wire Wire Line
	7250 1900 6700 1900
Wire Wire Line
	7750 2650 9200 2650
Wire Wire Line
	7750 2750 9200 2750
Entry Wire Line
	9200 2850 9300 2950
Wire Wire Line
	7750 2850 9200 2850
Wire Wire Line
	7750 2950 9200 2950
Wire Wire Line
	7750 3050 9200 3050
Wire Wire Line
	7750 3150 9200 3150
Text HLabel 10100 2650 2    50   Output ~ 0
ALG_BUS
Wire Bus Line
	9300 2650 10100 2650
Wire Bus Line
	9300 2650 9300 3750
$EndSCHEMATC
