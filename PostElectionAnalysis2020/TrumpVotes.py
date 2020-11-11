from ContestIndices import *

trump_votes_array = []
trump_votes_cd_ME_array = []
trump_votes_cd_NE_array = []

# Trump Votes
trump_votes_AL = 1_430_589
trump_votes_AK = 118_844
trump_votes_AZ = 1_630_339
trump_votes_AR = 755_815
trump_votes_CA = 4_842_414
trump_votes_CO = 1_335_253
trump_votes_CT = 711_204
trump_votes_DC = 15_075
trump_votes_DE = 199_829
trump_votes_FL = 5_658_847
trump_votes_GA = 2_456_275
trump_votes_HI = 196_602
trump_votes_ID = 554_019
trump_votes_IL = 2_316_566
trump_votes_IN = 1_725_723
trump_votes_IA = 896_411
trump_votes_KS = 752_903
trump_votes_KY = 1_326_418
trump_votes_LA = 1_255_481
trump_votes_ME = 359_502
trump_votes_MD = 879_026
trump_votes_MA = 1_148_777
trump_votes_MI = 2_644_525
trump_votes_MN = 1_484_885
trump_votes_MS = 677_218
trump_votes_MO = 1_711_848
trump_votes_MT = 341_767
trump_votes_NE = 550_202
trump_votes_NV = 634_158
trump_votes_NH = 365_373
trump_votes_NJ = 1_549_699
trump_votes_NM = 400_095
trump_votes_NY = 2_855_014
trump_votes_NC = 2_734_412
trump_votes_ND = 235_489
trump_votes_OH = 3_074_418
trump_votes_OK = 1_018_870
trump_votes_OR = 928_706
trump_votes_PA = 3_320_459
trump_votes_RI = 197_421
trump_votes_SC = 1_384_852
trump_votes_SD = 261_035
trump_votes_TN = 1_849_211
trump_votes_TX = 5_865_913
trump_votes_UT = 781_358
trump_votes_VT = 112_688
trump_votes_VA = 1_952_834
trump_votes_WA = 1_531_360
trump_votes_WV = 539_610
trump_votes_WI = 1_610_030
trump_votes_WY = 193_454

# Congressional Districts (Actual Vote Counts Not Available)
trump_votes_ME_CD1 = 1
trump_votes_ME_CD2 = 2

trump_votes_NE_CD1 = 2
trump_votes_NE_CD2 = 1
trump_votes_NE_CD3 = 2

# Add each state into the Trump array:
trump_votes_array.insert(array_index_AL, trump_votes_AL)
trump_votes_array.insert(array_index_AK, trump_votes_AK)
trump_votes_array.insert(array_index_AZ, trump_votes_AZ)
trump_votes_array.insert(array_index_AR, trump_votes_AR)
trump_votes_array.insert(array_index_CA, trump_votes_CA)
trump_votes_array.insert(array_index_CO, trump_votes_CO)
trump_votes_array.insert(array_index_CT, trump_votes_CT)
trump_votes_array.insert(array_index_DE, trump_votes_DE)
trump_votes_array.insert(array_index_DC, trump_votes_DC)
trump_votes_array.insert(array_index_FL, trump_votes_FL)
trump_votes_array.insert(array_index_GA, trump_votes_GA)
trump_votes_array.insert(array_index_HI, trump_votes_HI)
trump_votes_array.insert(array_index_ID, trump_votes_ID)
trump_votes_array.insert(array_index_IL, trump_votes_IL)
trump_votes_array.insert(array_index_IN, trump_votes_IN)
trump_votes_array.insert(array_index_IA, trump_votes_IA)
trump_votes_array.insert(array_index_KS, trump_votes_KS)
trump_votes_array.insert(array_index_KY, trump_votes_KY)
trump_votes_array.insert(array_index_LA, trump_votes_LA)
trump_votes_array.insert(array_index_ME, trump_votes_ME)
trump_votes_array.insert(array_index_MD, trump_votes_MD)
trump_votes_array.insert(array_index_MA, trump_votes_MA)
trump_votes_array.insert(array_index_MI, trump_votes_MI)
trump_votes_array.insert(array_index_MN, trump_votes_MN)
trump_votes_array.insert(array_index_MS, trump_votes_MS)
trump_votes_array.insert(array_index_MO, trump_votes_MO)
trump_votes_array.insert(array_index_MT, trump_votes_MT)
trump_votes_array.insert(array_index_NE, trump_votes_NE)
trump_votes_array.insert(array_index_NV, trump_votes_NV)
trump_votes_array.insert(array_index_NH, trump_votes_NH)
trump_votes_array.insert(array_index_NJ, trump_votes_NJ)
trump_votes_array.insert(array_index_NM, trump_votes_NM)
trump_votes_array.insert(array_index_NY, trump_votes_NY)
trump_votes_array.insert(array_index_NC, trump_votes_NC)
trump_votes_array.insert(array_index_ND, trump_votes_ND)
trump_votes_array.insert(array_index_OH, trump_votes_OH)
trump_votes_array.insert(array_index_OK, trump_votes_OK)
trump_votes_array.insert(array_index_OR, trump_votes_OR)
trump_votes_array.insert(array_index_PA, trump_votes_PA)
trump_votes_array.insert(array_index_RI, trump_votes_RI)
trump_votes_array.insert(array_index_SC, trump_votes_SC)
trump_votes_array.insert(array_index_SD, trump_votes_SD)
trump_votes_array.insert(array_index_TN, trump_votes_TN)
trump_votes_array.insert(array_index_TX, trump_votes_TX)
trump_votes_array.insert(array_index_UT, trump_votes_UT)
trump_votes_array.insert(array_index_VT, trump_votes_VT)
trump_votes_array.insert(array_index_VA, trump_votes_VA)
trump_votes_array.insert(array_index_WA, trump_votes_WA)
trump_votes_array.insert(array_index_WV, trump_votes_WV)
trump_votes_array.insert(array_index_WI, trump_votes_WI)
trump_votes_array.insert(array_index_WY, trump_votes_WY)

trump_votes_cd_ME_array.insert(array_index_ME_CD1, trump_votes_ME_CD1)
trump_votes_cd_ME_array.insert(array_index_ME_CD2, trump_votes_ME_CD2)

trump_votes_cd_NE_array.insert(array_index_NE_CD1, trump_votes_NE_CD1)
trump_votes_cd_NE_array.insert(array_index_NE_CD2, trump_votes_NE_CD2)
trump_votes_cd_NE_array.insert(array_index_NE_CD3, trump_votes_NE_CD3)