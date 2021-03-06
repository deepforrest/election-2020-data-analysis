from ContestIndices import *

recount_margin_percentage_states_array = []

# Recount Margins (from Ballotopedia)
# States with a margin of 1 can request a recount at any time.
# States with a margin of 0 do not do recounts.

recount_margin_percentage_AL = 0.005
recount_margin_percentage_AK = 0.005
recount_margin_percentage_AZ = 0.001
recount_margin_percentage_AR = 0.01
recount_margin_percentage_CA = 0.00015
recount_margin_percentage_CO = 0.005
recount_margin_percentage_CT = 0.005
recount_margin_percentage_DC = 0.01  # Assumed
recount_margin_percentage_DE = 0.005
recount_margin_percentage_FL = 0.005
recount_margin_percentage_GA = 0.005
recount_margin_percentage_HI = 0.0025
recount_margin_percentage_ID = 0.001
recount_margin_percentage_IL = 0.05
recount_margin_percentage_IN = 1
recount_margin_percentage_IA = 0.01
recount_margin_percentage_KS = 0.005
recount_margin_percentage_KY = 1
recount_margin_percentage_LA = 1
recount_margin_percentage_ME = 0.015
recount_margin_percentage_MD = 0.001
recount_margin_percentage_MA = 0.005
recount_margin_percentage_MI = 0
recount_margin_percentage_MN = 0.0025
recount_margin_percentage_MS = 0
recount_margin_percentage_MO = 0.01
recount_margin_percentage_MT = 0.005
recount_margin_percentage_NE = 0.01
recount_margin_percentage_NV = 1
recount_margin_percentage_NH = 1
recount_margin_percentage_NJ = 1
recount_margin_percentage_NM = 0.01
recount_margin_percentage_NY = 0.005   #Effective 2021
recount_margin_percentage_NC = 0.005
recount_margin_percentage_ND = 0.005
recount_margin_percentage_OH = 0.0025
recount_margin_percentage_OK = 0.01
recount_margin_percentage_OR = 0.002
recount_margin_percentage_PA = 0.005
recount_margin_percentage_RI = 0.005
recount_margin_percentage_SC = 0
recount_margin_percentage_SD = 0.0025
recount_margin_percentage_TN = 0
recount_margin_percentage_TX = 0.1
recount_margin_percentage_UT = 0.0025
recount_margin_percentage_VT = 0.02
recount_margin_percentage_VA = 0.01
recount_margin_percentage_WA = 0.0025
recount_margin_percentage_WV = 1
recount_margin_percentage_WI = 0.01
recount_margin_percentage_WY = 0.01

# Create an array:
recount_margin_percentage_states_array.insert(array_index_AL, recount_margin_percentage_AL)
recount_margin_percentage_states_array.insert(array_index_AK, recount_margin_percentage_AK)
recount_margin_percentage_states_array.insert(array_index_AZ, recount_margin_percentage_AZ)
recount_margin_percentage_states_array.insert(array_index_AR, recount_margin_percentage_AR)
recount_margin_percentage_states_array.insert(array_index_CA, recount_margin_percentage_CA)
recount_margin_percentage_states_array.insert(array_index_CO, recount_margin_percentage_CO)
recount_margin_percentage_states_array.insert(array_index_CT, recount_margin_percentage_CT)
recount_margin_percentage_states_array.insert(array_index_DE, recount_margin_percentage_DE)
recount_margin_percentage_states_array.insert(array_index_DC, recount_margin_percentage_DC)
recount_margin_percentage_states_array.insert(array_index_FL, recount_margin_percentage_FL)
recount_margin_percentage_states_array.insert(array_index_GA, recount_margin_percentage_GA)
recount_margin_percentage_states_array.insert(array_index_HI, recount_margin_percentage_HI)
recount_margin_percentage_states_array.insert(array_index_ID, recount_margin_percentage_ID)
recount_margin_percentage_states_array.insert(array_index_IL, recount_margin_percentage_IL)
recount_margin_percentage_states_array.insert(array_index_IN, recount_margin_percentage_IN)
recount_margin_percentage_states_array.insert(array_index_IA, recount_margin_percentage_IA)
recount_margin_percentage_states_array.insert(array_index_KS, recount_margin_percentage_KS)
recount_margin_percentage_states_array.insert(array_index_KY, recount_margin_percentage_KY)
recount_margin_percentage_states_array.insert(array_index_LA, recount_margin_percentage_LA)
recount_margin_percentage_states_array.insert(array_index_ME, recount_margin_percentage_ME)
recount_margin_percentage_states_array.insert(array_index_MD, recount_margin_percentage_MD)
recount_margin_percentage_states_array.insert(array_index_MA, recount_margin_percentage_MA)
recount_margin_percentage_states_array.insert(array_index_MI, recount_margin_percentage_MI)
recount_margin_percentage_states_array.insert(array_index_MN, recount_margin_percentage_MN)
recount_margin_percentage_states_array.insert(array_index_MS, recount_margin_percentage_MS)
recount_margin_percentage_states_array.insert(array_index_MO, recount_margin_percentage_MO)
recount_margin_percentage_states_array.insert(array_index_MT, recount_margin_percentage_MT)
recount_margin_percentage_states_array.insert(array_index_NE, recount_margin_percentage_NE)
recount_margin_percentage_states_array.insert(array_index_NV, recount_margin_percentage_NV)
recount_margin_percentage_states_array.insert(array_index_NH, recount_margin_percentage_NH)
recount_margin_percentage_states_array.insert(array_index_NJ, recount_margin_percentage_NJ)
recount_margin_percentage_states_array.insert(array_index_NM, recount_margin_percentage_NM)
recount_margin_percentage_states_array.insert(array_index_NY, recount_margin_percentage_NY)
recount_margin_percentage_states_array.insert(array_index_NC, recount_margin_percentage_NC)
recount_margin_percentage_states_array.insert(array_index_ND, recount_margin_percentage_ND)
recount_margin_percentage_states_array.insert(array_index_OH, recount_margin_percentage_OH)
recount_margin_percentage_states_array.insert(array_index_OK, recount_margin_percentage_OK)
recount_margin_percentage_states_array.insert(array_index_OR, recount_margin_percentage_OR)
recount_margin_percentage_states_array.insert(array_index_PA, recount_margin_percentage_PA)
recount_margin_percentage_states_array.insert(array_index_RI, recount_margin_percentage_RI)
recount_margin_percentage_states_array.insert(array_index_SC, recount_margin_percentage_SC)
recount_margin_percentage_states_array.insert(array_index_SD, recount_margin_percentage_SD)
recount_margin_percentage_states_array.insert(array_index_TN, recount_margin_percentage_TN)
recount_margin_percentage_states_array.insert(array_index_TX, recount_margin_percentage_TX)
recount_margin_percentage_states_array.insert(array_index_UT, recount_margin_percentage_UT)
recount_margin_percentage_states_array.insert(array_index_VT, recount_margin_percentage_VT)
recount_margin_percentage_states_array.insert(array_index_VA, recount_margin_percentage_VA)
recount_margin_percentage_states_array.insert(array_index_WA, recount_margin_percentage_WA)
recount_margin_percentage_states_array.insert(array_index_WV, recount_margin_percentage_WV)
recount_margin_percentage_states_array.insert(array_index_WI, recount_margin_percentage_WI)
recount_margin_percentage_states_array.insert(array_index_WY, recount_margin_percentage_WY)
