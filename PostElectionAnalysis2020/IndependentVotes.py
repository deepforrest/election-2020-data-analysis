from ContestIndices import *

independent_votes_array = []
independent_votes_cd_ME_array = []
independent_votes_cd_NE_array = []

# Independent Vote Counts (Holistic; Not Candidate Specific):
independent_votes_AL = 24_902
independent_votes_AK = 4_966 + 1_528 + 671 + 521 + 194
independent_votes_AZ = 50_136
independent_votes_AR = 13_039 + 4_071 + 2_947 + 2_784 + 2_132 + 2_097 + 1_706 + 1_459 + 1_366 + 1_317 + 1_306
independent_votes_CA = 142_252 + 62_620 + 44_042 + 37_691
independent_votes_CO = 50_469 + 8_535 + 7_639 + 4_931 + 2_653 + 2_431 + 1_942 + 949 + 737 + 619 + 594 + 550 + 544 + 470 + 360 + 341 + 338 + 187 + 168
independent_votes_CT = 20_173 + 7_668
independent_votes_DC = 1_532 + 1_351 + 655 + 538
independent_votes_DE = 4_977 + 2_135
independent_votes_FL = 70_046 + 14_665 + 5_951 + 5_688 + 3_890
independent_votes_GA = 61_951
independent_votes_HI = 5_525 + 3_814 + 1_181 + 930
independent_votes_ID = 16_401 + 3_632 + 2_808 + 1_884 + 1_491
independent_votes_IL = 59_791 + 26_657 + 8_213 + 7_050
independent_votes_IN = 58_703
independent_votes_IA = 19_571 + 3_204 + 3_074 + 1_706 + 1_081 + 551 + 549
independent_votes_KS = 29_466
independent_votes_KY = 26_217 + 6_478 + 3_598
independent_votes_LA = 21_636 + 4_894 + 2_496 + 1_625 + 1_125 + 986 + 860 + 749 + 668 + 662 + 534
independent_votes_ME = 14_176 + 8_234 + 1_382
independent_votes_MD = 27_508 + 13_188 + 5_077
independent_votes_MA = 45_782 + 18_135
independent_votes_MI = 60_287 + 13_680 + 7_223 + 2_983
independent_votes_MN = 35_009 + 10_052 + 7_962 + 5_693 + 5_623 + 1_253 + 692
independent_votes_MS = 7_309 + 3_364 + 1_347 + 1_174 + 1_169 + 1_064 + 610
independent_votes_MO = 40_932 + 8_219 + 3_894
independent_votes_MT = 15_194
independent_votes_NE = 19_885
independent_votes_NV = 13_894 + 13_376 + 2_949
independent_votes_NH = 13_066
independent_votes_NJ = 24_629 + 11_115 + 2_699 + 2_327 + 2_229 + 2_100
independent_votes_NM = 12_446 + 4_373 + 1_790 + 1_625
independent_votes_NY = 47_879 + 23_311 + 17_679
independent_votes_NC = 47_423 + 11_882 + 7_401
independent_votes_ND = 9_386
independent_votes_OH = 65_069 + 18_032
independent_votes_OK = 24_686 + 5_590 + 3_650 + 2_542
independent_votes_OR = 39_367 + 11_251 + 4_766
independent_votes_PA = 77_664
independent_votes_RI = 4_976 + 906 + 827 + 746
independent_votes_SC = 27_908 + 6_906 + 1_860
independent_votes_SD = 11_095
independent_votes_TN = 29_816 + 10_216 + 5_340 + 4_526 + 2_582 + 2_292 + 1_833
independent_votes_TX = 125_282 + 33_150
independent_votes_UT = 32_597 + 6_067 + 4_956 + 4_242 + 2_215 + 1_921 + 928
independent_votes_VT = 3_573 + 1_303 + 1_266 + 1_156 + 850 + 230 + 213 + 208 + 207 + 171 + 142 + 138 + 123 + 106 + 65 + 62 + 57 + 48 + 31
independent_votes_VA = 63_793
independent_votes_WA = 76_5545 + 17_393 + 4_551 + 2_359
independent_votes_WV = 10_462 + 2_547
independent_votes_WI = 38_415 + 5_253 + 5_206
independent_votes_WY = 5_765 + 2_208

# Congressional Districts (Actual Vote Counts Not Available)
independent_votes_ME_CD1 = 0
independent_votes_ME_CD2 = 0

independent_votes_NE_CD1 = 0
independent_votes_NE_CD2 = 0
independent_votes_NE_CD3 = 0

# Add each individual state into the array:
independent_votes_array.insert(array_index_AL, independent_votes_AL)
independent_votes_array.insert(array_index_AK, independent_votes_AK)
independent_votes_array.insert(array_index_AZ, independent_votes_AZ)
independent_votes_array.insert(array_index_AR, independent_votes_AR)
independent_votes_array.insert(array_index_CA, independent_votes_CA)
independent_votes_array.insert(array_index_CO, independent_votes_CO)
independent_votes_array.insert(array_index_CT, independent_votes_CT)
independent_votes_array.insert(array_index_DE, independent_votes_DE)
independent_votes_array.insert(array_index_DC, independent_votes_DC)
independent_votes_array.insert(array_index_FL, independent_votes_FL)
independent_votes_array.insert(array_index_GA, independent_votes_GA)
independent_votes_array.insert(array_index_HI, independent_votes_HI)
independent_votes_array.insert(array_index_ID, independent_votes_ID)
independent_votes_array.insert(array_index_IL, independent_votes_IL)
independent_votes_array.insert(array_index_IN, independent_votes_IN)
independent_votes_array.insert(array_index_IA, independent_votes_IA)
independent_votes_array.insert(array_index_KS, independent_votes_KS)
independent_votes_array.insert(array_index_KY, independent_votes_KY)
independent_votes_array.insert(array_index_LA, independent_votes_LA)
independent_votes_array.insert(array_index_ME, independent_votes_ME)
independent_votes_array.insert(array_index_MD, independent_votes_MD)
independent_votes_array.insert(array_index_MA, independent_votes_MA)
independent_votes_array.insert(array_index_MI, independent_votes_MI)
independent_votes_array.insert(array_index_MN, independent_votes_MN)
independent_votes_array.insert(array_index_MS, independent_votes_MS)
independent_votes_array.insert(array_index_MO, independent_votes_MO)
independent_votes_array.insert(array_index_MT, independent_votes_MT)
independent_votes_array.insert(array_index_NE, independent_votes_NE)
independent_votes_array.insert(array_index_NV, independent_votes_NV)
independent_votes_array.insert(array_index_NH, independent_votes_NH)
independent_votes_array.insert(array_index_NJ, independent_votes_NJ)
independent_votes_array.insert(array_index_NM, independent_votes_NM)
independent_votes_array.insert(array_index_NY, independent_votes_NY)
independent_votes_array.insert(array_index_NC, independent_votes_NC)
independent_votes_array.insert(array_index_ND, independent_votes_ND)
independent_votes_array.insert(array_index_OH, independent_votes_OH)
independent_votes_array.insert(array_index_OK, independent_votes_OK)
independent_votes_array.insert(array_index_OR, independent_votes_OR)
independent_votes_array.insert(array_index_PA, independent_votes_PA)
independent_votes_array.insert(array_index_RI, independent_votes_RI)
independent_votes_array.insert(array_index_SC, independent_votes_SC)
independent_votes_array.insert(array_index_SD, independent_votes_SD)
independent_votes_array.insert(array_index_TN, independent_votes_TN)
independent_votes_array.insert(array_index_TX, independent_votes_TX)
independent_votes_array.insert(array_index_UT, independent_votes_UT)
independent_votes_array.insert(array_index_VT, independent_votes_VT)
independent_votes_array.insert(array_index_VA, independent_votes_VA)
independent_votes_array.insert(array_index_WA, independent_votes_WA)
independent_votes_array.insert(array_index_WV, independent_votes_WV)
independent_votes_array.insert(array_index_WI, independent_votes_WI)
independent_votes_array.insert(array_index_WY, independent_votes_WY)

independent_votes_cd_ME_array.insert(array_index_ME_CD1, independent_votes_ME_CD1)
independent_votes_cd_ME_array.insert(array_index_ME_CD2, independent_votes_ME_CD2)

independent_votes_cd_NE_array.insert(array_index_NE_CD1, independent_votes_NE_CD1)
independent_votes_cd_NE_array.insert(array_index_NE_CD2, independent_votes_NE_CD2)
independent_votes_cd_NE_array.insert(array_index_NE_CD3, independent_votes_NE_CD3)