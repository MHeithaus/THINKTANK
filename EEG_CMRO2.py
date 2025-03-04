# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 12:51:17 2025

@author: mason
"""

def EEG_CMRO2(EEG_Delta, EEG_Med, EEG_Time, CMRO2_Constant=2.016, ElectrodeList = ['Fp1', 'Fp2', 'F3', 'F4', 'T5', 'T6', '01', '02', 'F7', 'F8', 'C3', 'C4', 'T3', 'T4', 'P3', 'P4'], Trials = 9, CMRO2Limits = [2.1, 6.88], EEGLimits = [-20000,25000]):
    TotalCharge = 0
    for TotalSolve in range(len(ElectrodeList)):
        TotalCharge+= abs(EEG_Med[ElectrodeList[TotalSolve]+ ' trial ' +'1' + ' Median'])
    TrialPercent = {}
    
    for medianPercent in range(len(ElectrodeList)):
        TrialPercent[ElectrodeList[medianPercent]] = (abs(EEG_Med[ElectrodeList[medianPercent]+ ' trial ' +'1' + ' Median'])/TotalCharge)*CMRO2_Constant
        
    CMRO2_val = {}
    
    for H in range(len(ElectrodeList)):
        for I in range(Trials):
            CMRO2_val[ElectrodeList[H]+' trial ' + str(I+1)] =[]
            for J in range(len(EEG_Time['Trial ' + str(I+1)])):
                CMRO2_val[ElectrodeList[H]+' trial ' + str(I+1)].append(((EEG_Delta[ElectrodeList[H]+' trial ' + str(I+1)][J]+20000)/45000)*TrialPercent[ElectrodeList[H]]*CMRO2Limits[1]+CMRO2Limits[0])
                #This proportion is 
    
    return CMRO2_val
        
