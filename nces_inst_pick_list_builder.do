set more off
clear all
cls

capture log close
log using "nces_inst_pick_list_builder.txt", text replace

local year = 2017                             // Set parameter.

// Use this code to download the latest higher edcuationdirectory information 
// from the National Center for Education Statistics (NCES).

// Jul/2017  Adam Ross Nelson - Initial build.
// Aug/2019  Adam Ross Nelson - GitHub rebuild.

/*#############################################################################
      Maintained/more information at:
	  https://github.com/adamrossnelson/nces_inst_pick_list_builder
##############################################################################*/

version 13                                    // Enforce version compatibility.
di c(pwd)                                     // Confrim working directory.

copy https://nces.ed.gov/ipeds/datacenter/data/HD`year'_Data_Stata.zip .
unzipfile HD`year'_Data_Stata.zip
import delimited hd`year'_data_stata.csv

tostring(unitid), replace
gen name = instnm + ", " + unitid
sort stabbr name
keep stabbr name sector
sort stabbr sector name

export delimited stabbr name using ///
     "1_nces_inst_pick_listPub_4-yr.csv" ///
     if sector == 1, novarnames replace
	 
export delimited stabbr name using ///
     "2_nces_inst_pick_listPri_not-for-profit_4-yr.csv" ///
	 if sector == 2, novarnames replace
	 
export delimited stabbr name using ///
     "3_nces_inst_pick_listPri_for-profit_4-yr.csv" ///
	 if sector == 3, novarnames replace
	 
export delimited stabbr name using ///
     "4_nces_inst_pick_listPub_2-yr.csv" ///
	 if sector == 4, novarnames replace
	 
export delimited stabbr name using ///
     "5_nces_inst_pick_listPri_not-for-profit_2-yr.csv" ///
	 if sector == 5, novarnames replace
	 
export delimited stabbr name using ///
     "6_nces_inst_pick_listPri_for-profit_2-yr.csv" ///
	 if sector == 6, novarnames replace
	 
export delimited stabbr name using ///
     "7_nces_inst_pick_listPub_less-than_2-yr.csv" ///
	 if sector == 7, novarnames replace
	 
export delimited stabbr name using ///
     "8_nces_inst_pick_listOth_Private_less_than_2-years.csv" ///
	 if sector > 7 & sector < 99, novarnames replace
	 
/*#############################################################################
      Saved pick list files in the current working directory:
##############################################################################*/
