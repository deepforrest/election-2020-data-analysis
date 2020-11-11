from ContestIndices import *

biden_votes_array = []
biden_votes_cd_ME_array = []
biden_votes_cd_NE_array = []


# Biden Vote Counts:
biden_votes_AL = 834_533
biden_votes_AK = 64_246
biden_votes_AZ = 1_645_359
biden_votes_AR = 417_897
biden_votes_CA = 9_343_525
biden_votes_CO = 1_753_416
biden_votes_CT = 1_070_380
biden_votes_DC = 258_625
biden_votes_DE = 295_403
biden_votes_FL = 5_284_453
biden_votes_GA = 2_467_870
biden_votes_HI = 365_802
biden_votes_ID = 286_991
biden_votes_IL = 3_056_219
biden_votes_IN = 1_239_401
biden_votes_IA = 757_905
biden_votes_KS = 551_144
biden_votes_KY = 772_285
biden_votes_LA = 855_597
biden_votes_ME = 420_023
biden_votes_MD = 1_625_505
biden_votes_MA = 2_316_338
biden_votes_MI = 2_790_648
biden_votes_MN = 1_717_935
biden_votes_MS = 440_284
biden_votes_MO = 1_242_851
biden_votes_MT = 243_719
biden_votes_NE = 367_919
biden_votes_NV = 670_344
biden_votes_NH = 423_291
biden_votes_NJ = 2_206_781
biden_votes_NM = 496_826
biden_votes_NY = 3_702_263
biden_votes_NC = 2_659_528
biden_votes_ND = 114_684
biden_votes_OH = 2_603_731
biden_votes_OK = 503_829
biden_votes_OR = 1_304_536
biden_votes_PA = 3_365_798
biden_votes_RI = 300_325
biden_votes_SC = 1_091_348
biden_votes_SD = 150_467
biden_votes_TN = 1_139_666
biden_votes_TX = 5_218_631
biden_votes_UT = 505_250
biden_votes_VT = 242_805
biden_votes_VA = 2_379_830
biden_votes_WA = 2_316_582
biden_votes_WV = 232_502
biden_votes_WI = 1_630_570
biden_votes_WY = 73_445

# Congressional Districts (Based on Relative Numbers - Actual Vote Counts Not Available)
biden_votes_ME_CD1 = 2
biden_votes_ME_CD2 = 1

biden_votes_NE_CD1 = 1
biden_votes_NE_CD2 = 2
biden_votes_NE_CD3 = 1


# Add each individual state into the array:
biden_votes_array.insert(array_index_AL, biden_votes_AL)
biden_votes_array.insert(array_index_AK, biden_votes_AK)
biden_votes_array.insert(array_index_AZ, biden_votes_AZ)
biden_votes_array.insert(array_index_AR, biden_votes_AR)
biden_votes_array.insert(array_index_CA, biden_votes_CA)
biden_votes_array.insert(array_index_CO, biden_votes_CO)
biden_votes_array.insert(array_index_CT, biden_votes_CT)
biden_votes_array.insert(array_index_DE, biden_votes_DE)
biden_votes_array.insert(array_index_DC, biden_votes_DC)
biden_votes_array.insert(array_index_FL, biden_votes_FL)
biden_votes_array.insert(array_index_GA, biden_votes_GA)
biden_votes_array.insert(array_index_HI, biden_votes_HI)
biden_votes_array.insert(array_index_ID, biden_votes_ID)
biden_votes_array.insert(array_index_IL, biden_votes_IL)
biden_votes_array.insert(array_index_IN, biden_votes_IN)
biden_votes_array.insert(array_index_IA, biden_votes_IA)
biden_votes_array.insert(array_index_KS, biden_votes_KS)
biden_votes_array.insert(array_index_KY, biden_votes_KY)
biden_votes_array.insert(array_index_LA, biden_votes_LA)
biden_votes_array.insert(array_index_ME, biden_votes_ME)
biden_votes_array.insert(array_index_MD, biden_votes_MD)
biden_votes_array.insert(array_index_MA, biden_votes_MA)
biden_votes_array.insert(array_index_MI, biden_votes_MI)
biden_votes_array.insert(array_index_MN, biden_votes_MN)
biden_votes_array.insert(array_index_MS, biden_votes_MS)
biden_votes_array.insert(array_index_MO, biden_votes_MO)
biden_votes_array.insert(array_index_MT, biden_votes_MT)
biden_votes_array.insert(array_index_NE, biden_votes_NE)
biden_votes_array.insert(array_index_NV, biden_votes_NV)
biden_votes_array.insert(array_index_NH, biden_votes_NH)
biden_votes_array.insert(array_index_NJ, biden_votes_NJ)
biden_votes_array.insert(array_index_NM, biden_votes_NM)
biden_votes_array.insert(array_index_NY, biden_votes_NY)
biden_votes_array.insert(array_index_NC, biden_votes_NC)
biden_votes_array.insert(array_index_ND, biden_votes_ND)
biden_votes_array.insert(array_index_OH, biden_votes_OH)
biden_votes_array.insert(array_index_OK, biden_votes_OK)
biden_votes_array.insert(array_index_OR, biden_votes_OR)
biden_votes_array.insert(array_index_PA, biden_votes_PA)
biden_votes_array.insert(array_index_RI, biden_votes_RI)
biden_votes_array.insert(array_index_SC, biden_votes_SC)
biden_votes_array.insert(array_index_SD, biden_votes_SD)
biden_votes_array.insert(array_index_TN, biden_votes_TN)
biden_votes_array.insert(array_index_TX, biden_votes_TX)
biden_votes_array.insert(array_index_UT, biden_votes_UT)
biden_votes_array.insert(array_index_VT, biden_votes_VT)
biden_votes_array.insert(array_index_VA, biden_votes_VA)
biden_votes_array.insert(array_index_WA, biden_votes_WA)
biden_votes_array.insert(array_index_WV, biden_votes_WV)
biden_votes_array.insert(array_index_WI, biden_votes_WI)
biden_votes_array.insert(array_index_WY, biden_votes_WY)

biden_votes_cd_ME_array.insert(array_index_ME_CD1, biden_votes_ME_CD1)
biden_votes_cd_ME_array.insert(array_index_ME_CD2, biden_votes_ME_CD2)

biden_votes_cd_NE_array.insert(array_index_NE_CD1, biden_votes_NE_CD1)
biden_votes_cd_NE_array.insert(array_index_NE_CD2, biden_votes_NE_CD2)
biden_votes_cd_NE_array.insert(array_index_NE_CD3, biden_votes_NE_CD3)

