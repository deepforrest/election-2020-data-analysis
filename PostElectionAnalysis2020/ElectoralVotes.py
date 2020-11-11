from ContestIndices import *

electoral_votes_states_array = []
electoral_votes_cd_ME_array = []
electoral_votes_cd_NE_array = []

# Electoral College By State:
electoral_votes_AL = 9
electoral_votes_AK = 3
electoral_votes_AZ = 11
electoral_votes_AR = 6
electoral_votes_CA = 55
electoral_votes_CO = 9
electoral_votes_CT = 7
electoral_votes_DC = 3
electoral_votes_DE = 3
electoral_votes_FL = 29
electoral_votes_GA = 16
electoral_votes_HI = 4
electoral_votes_ID = 4
electoral_votes_IL = 20
electoral_votes_IN = 11
electoral_votes_IA = 6
electoral_votes_KS = 6
electoral_votes_KY = 8
electoral_votes_LA = 8
electoral_votes_ME = 2
electoral_votes_MD = 10
electoral_votes_MA = 11
electoral_votes_MI = 16
electoral_votes_MN = 10
electoral_votes_MS = 6
electoral_votes_MO = 10
electoral_votes_MT = 3
electoral_votes_NE = 2
electoral_votes_NV = 6
electoral_votes_NH = 4
electoral_votes_NJ = 14
electoral_votes_NM = 5
electoral_votes_NY = 29
electoral_votes_NC = 15
electoral_votes_ND = 3
electoral_votes_OH = 18
electoral_votes_OK = 7
electoral_votes_OR = 7
electoral_votes_PA = 20
electoral_votes_RI = 4
electoral_votes_SC = 9
electoral_votes_SD = 3
electoral_votes_TN = 11
electoral_votes_TX = 38
electoral_votes_UT = 6
electoral_votes_VT = 3
electoral_votes_VA = 13
electoral_votes_WA = 12
electoral_votes_WV = 5
electoral_votes_WI = 10
electoral_votes_WY = 3

# Congressional Districts
electoral_votes_ME_CD1 = 1
electoral_votes_ME_CD2 = 1
electoral_votes_NE_CD1 = 1
electoral_votes_NE_CD2 = 1
electoral_votes_NE_CD3 = 1

# Add each state's electoral college array:
electoral_votes_states_array.insert(array_index_AL, electoral_votes_AL)
electoral_votes_states_array.insert(array_index_AK, electoral_votes_AK)
electoral_votes_states_array.insert(array_index_AZ, electoral_votes_AZ)
electoral_votes_states_array.insert(array_index_AR, electoral_votes_AR)
electoral_votes_states_array.insert(array_index_CA, electoral_votes_CA)
electoral_votes_states_array.insert(array_index_CO, electoral_votes_CO)
electoral_votes_states_array.insert(array_index_CT, electoral_votes_CT)
electoral_votes_states_array.insert(array_index_DE, electoral_votes_DE)
electoral_votes_states_array.insert(array_index_DC, electoral_votes_DC)
electoral_votes_states_array.insert(array_index_FL, electoral_votes_FL)
electoral_votes_states_array.insert(array_index_GA, electoral_votes_GA)
electoral_votes_states_array.insert(array_index_HI, electoral_votes_HI)
electoral_votes_states_array.insert(array_index_ID, electoral_votes_ID)
electoral_votes_states_array.insert(array_index_IL, electoral_votes_IL)
electoral_votes_states_array.insert(array_index_IN, electoral_votes_IN)
electoral_votes_states_array.insert(array_index_IA, electoral_votes_IA)
electoral_votes_states_array.insert(array_index_KS, electoral_votes_KS)
electoral_votes_states_array.insert(array_index_KY, electoral_votes_KY)
electoral_votes_states_array.insert(array_index_LA, electoral_votes_LA)
electoral_votes_states_array.insert(array_index_ME, electoral_votes_ME)
electoral_votes_states_array.insert(array_index_MD, electoral_votes_MD)
electoral_votes_states_array.insert(array_index_MA, electoral_votes_MA)
electoral_votes_states_array.insert(array_index_MI, electoral_votes_MI)
electoral_votes_states_array.insert(array_index_MN, electoral_votes_MN)
electoral_votes_states_array.insert(array_index_MS, electoral_votes_MS)
electoral_votes_states_array.insert(array_index_MO, electoral_votes_MO)
electoral_votes_states_array.insert(array_index_MT, electoral_votes_MT)
electoral_votes_states_array.insert(array_index_NE, electoral_votes_NE)
electoral_votes_states_array.insert(array_index_NV, electoral_votes_NV)
electoral_votes_states_array.insert(array_index_NH, electoral_votes_NH)
electoral_votes_states_array.insert(array_index_NJ, electoral_votes_NJ)
electoral_votes_states_array.insert(array_index_NM, electoral_votes_NM)
electoral_votes_states_array.insert(array_index_NY, electoral_votes_NY)
electoral_votes_states_array.insert(array_index_NC, electoral_votes_NC)
electoral_votes_states_array.insert(array_index_ND, electoral_votes_ND)
electoral_votes_states_array.insert(array_index_OH, electoral_votes_OH)
electoral_votes_states_array.insert(array_index_OK, electoral_votes_OK)
electoral_votes_states_array.insert(array_index_OR, electoral_votes_OR)
electoral_votes_states_array.insert(array_index_PA, electoral_votes_PA)
electoral_votes_states_array.insert(array_index_RI, electoral_votes_RI)
electoral_votes_states_array.insert(array_index_SC, electoral_votes_SC)
electoral_votes_states_array.insert(array_index_SD, electoral_votes_SD)
electoral_votes_states_array.insert(array_index_TN, electoral_votes_TN)
electoral_votes_states_array.insert(array_index_TX, electoral_votes_TX)
electoral_votes_states_array.insert(array_index_UT, electoral_votes_UT)
electoral_votes_states_array.insert(array_index_VT, electoral_votes_VT)
electoral_votes_states_array.insert(array_index_VA, electoral_votes_VA)
electoral_votes_states_array.insert(array_index_WA, electoral_votes_WA)
electoral_votes_states_array.insert(array_index_WV, electoral_votes_WV)
electoral_votes_states_array.insert(array_index_WI, electoral_votes_WI)
electoral_votes_states_array.insert(array_index_WY, electoral_votes_WY)

#
electoral_votes_cd_ME_array.insert(array_index_ME_CD1, electoral_votes_ME_CD1)
electoral_votes_cd_ME_array.insert(array_index_ME_CD2, electoral_votes_ME_CD2)

electoral_votes_cd_NE_array.insert(array_index_NE_CD1, electoral_votes_NE_CD1)
electoral_votes_cd_NE_array.insert(array_index_NE_CD2, electoral_votes_NE_CD2)
electoral_votes_cd_NE_array.insert(array_index_NE_CD3, electoral_votes_NE_CD3)
# For loop to add up the available electoral votes in each state:

from ContestNames import states_array
from ContestNames import congressional_district_ME_array
from ContestNames import congressional_district_NE_array

total_states_electoral_votes = 0
total_cd_electoral_votes = 0

for state in range(len(states_array)):
    total_states_electoral_votes += electoral_votes_states_array[state]

for district in range(len(congressional_district_ME_array)):
    total_cd_electoral_votes += electoral_votes_cd_ME_array[district]

for district in range(len(congressional_district_NE_array)):
    total_cd_electoral_votes += electoral_votes_cd_NE_array[district]

total_electoral_votes = total_states_electoral_votes + total_cd_electoral_votes
