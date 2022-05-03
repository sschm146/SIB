import numpy as np
import random
import pandas as pd

def simulation(x, n_estimates):
    '''
    Main function that simulates the signals with required conditions.
            Parameters:
                    x (list): The means for the signals. Also correspond to rounds. The length
                    of the list is the number of rounds.
                    n_estimates (int): number of estimates in each round. Varies only for 6 or 7 
                    estimates!

            Returns:
                The df in the long format with additional columns for verifying some of the
                conditions.
    '''
    total_rounds = len(x)

    # canvas for saving the data satisfying the conditions
    out = pd.DataFrame({"round":list(),"sender":list(), "estimate":list(), "mean" : list(),"avABC-avEFG":list(),
    "avEF-D":list(),"avDE":list(),"avDF":list()})


    # COUNTERS: AvABC VS AvDEF
    count_avABC_large = 0
    count_avDEF_large = 0
    # COUNTERS: AvEF VS D
    count_avEF_large_ABC_large = 0
    count_avEF_large_DEF_large = 0
    count_D_large_ABC_large = 0
    count_D_large_DEF_large = 0
    # COUNTERS: 2 lowest and highest D,E,F condition
    lowest_DEF = 0
    # COUNTERS: close to avABC or av DEF
    if n_estimates == 7:
        count_closeABC_ABC_large = 0
        count_closeDEF_ABC_large = 0
        count_closeABC_DEF_large = 0
        count_closeDEF_DEF_large = 0

    #current round (rounds mean different "mean" or so called "x")
    n_rounds = 0


    # initialize the data for the first round (afterwards: updated for the next round when current round is finished)
    data = np.random.normal(loc = x[n_rounds], scale = 3, size = 10000).round().astype(int)



    while lowest_DEF<1:
        #10 rounds necessary (with 5 rounds avABC>avDEF and 5 rounds avDEF>avABC)
        while count_avABC_large<total_rounds/2 or count_avDEF_large<total_rounds/2:

            #draw 6(7) signals from "data"
            signals_set = random.sample(set(data),n_estimates)
            names_list = ["A","B","C","D","E","F","signal_7"]
            signals_set = dict(zip([names_list[i] for i in range(n_estimates)],signals_set)) 


            # calculating averages between signals
            # 1. av_ABC vs av_DEF condition
            av_ABC = np.mean([signals_set[key] for key in ['A','B','C']])
            av_DEF = np.mean([signals_set[key] for key in ['D','E','F']])
            # 2. D vs avEF condition
            av_EF = np.mean([signals_set[key] for key in ['E','F']])
            # 3. avDE and avDF
            av_DE = np.mean([signals_set[key] for key in ['D','E']])
            av_DF = np.mean([signals_set[key] for key in ['E','F']])

    
            # CONDITIONS
            # CONDITION 1. 
            cond_avABC_vs_avDEF = av_ABC - av_DEF > 1 and count_avABC_large<total_rounds/2
            cond_avDEF_vs_avABC = av_DEF - av_ABC > 1 and count_avDEF_large<total_rounds/2
            # CONDITION 2.
            cond_avEF_vs_D_ABC_large = av_EF - signals_set["D"] > 6 and count_avEF_large_ABC_large < total_rounds/4
            cond_avEF_vs_D_DEF_large = av_EF - signals_set["D"] > 6 and count_avEF_large_DEF_large < total_rounds/4

            cond_D_vs_avEF_ABC_large = av_EF - signals_set["D"] < -6 and count_D_large_ABC_large < total_rounds/4
            cond_D_vs_avEF_DEF_large = av_EF - signals_set["D"] < -6 and count_D_large_DEF_large < total_rounds/4

            # CONDITION 3.  The averages of D&E and D&F should never be a decimal number.
            cond_avDE_and_avDF = (av_DE).is_integer() and (av_DF).is_integer()

            # CONDITION 5.
            if n_estimates == 7:
                # 5.If AvABC>AvDEF and signal of sender 1 is close to AvABC, then the signal is 
                #i) >AvABC, 
                #ii) exactly AvABC,
                #or iii) marginally smaller than AvABC but 
                #then AvABC>>AvDEF (difference between AvABC and AvDEF should be much larger 
                #than 1 in that case). 
                cond_closeABC_ABC_large = (signals_set["signal_7"]>av_ABC 
                or signals_set["signal_7"]==av_ABC or
                (signals_set["signal_7"] - av_ABC < 0 and signals_set["signal_7"] - av_ABC > -1 and av_ABC-av_DEF > 1)
                ) and count_closeABC_ABC_large < total_rounds/4
                #If AvABC<AvDEF, then the signal is 
                #i) <AvABC , 
                #ii) exactly AvABC, or 
                #iii) marginally larger than AvABC but 
                #then AvDEF>>AvABC (difference between AvABC and AvDEF should be much larger 
                #than 1 in that case).   
                cond_closeABC_DEF_large = (signals_set["signal_7"]<av_ABC 
                or signals_set["signal_7"]==av_ABC or
                (signals_set["signal_7"] - av_ABC > 0 and signals_set["signal_7"] - av_ABC < 1 and av_DEF - av_ABC > 1)
                ) and count_closeABC_DEF_large < total_rounds/4

                cond_closeDEF_ABC_large = (signals_set["signal_7"]<av_DEF 
                or signals_set["signal_7"]==av_DEF or
                (signals_set["signal_7"] - av_DEF > 0 and signals_set["signal_7"] - av_DEF < 1 and av_ABC - av_DEF > 1)
                ) and count_closeDEF_ABC_large < total_rounds/4
        
                cond_closeDEF_DEF_large = (signals_set["signal_7"]>av_DEF 
                or signals_set["signal_7"]==av_DEF or
                (signals_set["signal_7"] - av_DEF < 0 and signals_set["signal_7"] - av_DEF > -1 and av_DEF-av_ABC > 1)
                ) and count_closeDEF_DEF_large < total_rounds/4


            # 1!summing up the conditions for the AvABC>AvDEF case:
            condition1 = cond_avABC_vs_avDEF and (cond_avEF_vs_D_ABC_large or cond_D_vs_avEF_ABC_large) and cond_avDE_and_avDF
            if n_estimates==7:
                condition1 =  condition1 and (cond_closeABC_ABC_large or cond_closeDEF_ABC_large)
            if condition1:
                count_avABC_large += 1
            
                print("avABC > avDEF rounds counted: "+str(count_avABC_large)+". When avABC > avDEF:")
                if cond_avEF_vs_D_ABC_large:
                    count_avEF_large_ABC_large += 1
                    print("avEF > D rounds counted: "+str(count_avEF_large_ABC_large))
                if cond_D_vs_avEF_ABC_large:
                    count_D_large_ABC_large += 1
                    print("D > avEF rounds counted: "+str(count_D_large_ABC_large))
                if n_estimates == 7:
                    if cond_closeABC_ABC_large:
                        count_closeABC_ABC_large += 1
                        print("7th signal close avABC rounds counted: "+str(count_closeABC_ABC_large))
                    if cond_closeDEF_ABC_large:
                        count_closeDEF_ABC_large += 1
                        print("7th signal close avDEF rounds counted: "+str(count_closeDEF_ABC_large))

        
                round_out = signals_set
                # estimates from current round and new data generation
                if n_rounds <= total_rounds - 2:
                    out, n_rounds, data = finish_round(x, n_estimates, total_rounds,round_out,out,n_rounds,av_ABC,av_DEF,av_EF,signals_set['D'],av_DE,av_DF)
                else:
                    out = finish_round(x, n_estimates, total_rounds,round_out,out,n_rounds,av_ABC,av_DEF,av_EF,signals_set['D'],av_DE,av_DF)

        
            # 2!summing up the conditions for the AvDEF>AvDABC case:
            condition2 = cond_avDEF_vs_avABC and (cond_avEF_vs_D_DEF_large or cond_D_vs_avEF_DEF_large) and cond_avDE_and_avDF
            if n_estimates == 7:
                condition2 = condition2 and (cond_closeABC_DEF_large or cond_closeDEF_DEF_large)
            if condition2:
                count_avDEF_large += 1
                print("avDEF > avABC rounds counted: "+str(count_avDEF_large)+". When avDEF > avABC:")
                if cond_avEF_vs_D_DEF_large:
                    count_D_large_DEF_large +=1
                    print("D > avEF rounds counted: "+str(count_D_large_DEF_large))
                if cond_D_vs_avEF_DEF_large:
                    count_avEF_large_DEF_large +=1
                    print("avEF > D rounds counted: "+str(count_avEF_large_DEF_large))
                if n_estimates == 7:
                    if cond_closeABC_DEF_large:
                        count_closeABC_DEF_large += 1
                        print("7th signal close avABC rounds counted: "+str(count_closeABC_DEF_large))
                    if cond_closeDEF_DEF_large:
                        count_closeDEF_DEF_large += 1
                        print("7th signal close avDEF rounds counted: "+str(count_closeDEF_DEF_large))

                round_out = signals_set

                # estimates from current round and new data generation
                if n_rounds <= total_rounds - 2:
                    out, n_rounds, data = finish_round(x, n_estimates, total_rounds,round_out,out,n_rounds,av_ABC,av_DEF,av_EF,signals_set['D'],av_DE,av_DF)
                else:
                    out = finish_round(x, n_estimates, total_rounds,round_out,out,n_rounds,av_ABC,av_DEF,av_EF,signals_set['D'],av_DE,av_DF)



        # after 10 rounds end check 2 lowest VS highest (D,E,F) condition
        temp = out.query("sender == 'D' or sender == 'E' or sender == 'F'")
        av_highest = temp.groupby('mean')['estimate'].max().mean()
        av_lowest = temp.groupby('mean')['estimate'].min().mean()
        av_s_lowest = temp.groupby('mean')['estimate'].nsmallest(2).groupby(level="mean").last().mean() 
        # CONDITION 4. lowest two signals of D, E, and F, should be on average at least 3 
        # lower (preferably a bit more, e.g. 5-6 lower) than the highest of the 3 signals across the 10 rounds
        if (av_lowest - av_highest< -3) and (av_s_lowest - av_highest< -3) :
            lowest_DEF = 1
            #save info to the df to verify condition
            out['lowest-highest_DEF'] = [av_lowest - av_highest for i in range(n_estimates*total_rounds)]
            out['2nd_lowest-highest_DEF'] = [av_s_lowest - av_highest for i in range(n_estimates*total_rounds)]

    return out


def save_data(x, n_estimates, round_out,out,n_rounds,av_ABC,av_DEF,avEF,D,avDE,avDF):
    '''
    Intermediate function to save the generated data in a current round a special format.
            Parameters:
                    round_out (df): The data from current round.
                    out (df): The data saved from the previous rounds.
                    n_rounds (int): The current round.
                    av_ABC (float): The avABC.
                    av_DEF (float): The avDEF.
                    av_EF (float): The av_EF.
                    av_DE (float): The av_DE.
                    av_DF (float): The av_DF.
                    D (float): The signal D.

            Returns:
                The df for all the realized rounds including the current round.
    '''
    temp = pd.DataFrame({"round":[int(n_rounds+1) for i in range(n_estimates)],
        "sender":list(round_out.keys()),
        "estimate":list(round_out.values()),
        "mean":[x[n_rounds] for i in range(n_estimates)],
        "avABC-avEFG":[av_ABC - av_DEF for i in range(n_estimates)],
        "avEF-D":[avEF-D for i in range(n_estimates)],
        "avDE":[avDE for i in range(n_estimates)],
        "avDF":[avDF for i in range(n_estimates)]})
        
    return pd.concat([out,temp])
    


def finish_round(x, n_estimates, total_rounds,round_out,out,n_rounds,av_ABC,av_DEF,avEF,D,avDE,avDF):
    '''
    Intermediate function to transit to the next round.
            Parameters:
                    round_out (df): The data from current round.
                    out (df): The data saved from the previous rounds.
                    n_rounds (int): The current round.
                    av_ABC (float): The avABC.
                    av_DEF (float): The avDEF.
                    av_EF (float): The av_EF.
                    av_DE (float): The av_DE.
                    av_DF (float): The av_DF.
                    D (float): The signal D.

            Returns:
                In the case of the running rounds: df with all the data on previous rounds,
                 next rounds number and new generated draws data.
                 In the case of the final round: only the df
    '''

    out = save_data(x, n_estimates, round_out,out,n_rounds,av_ABC,av_DEF,avEF,D,avDE,avDF)
    print("FINISHED ROUND NUMBER: "+str(n_rounds+1))

    if n_rounds <= total_rounds-2:
        # new data (mean) for the next round
        n_rounds += 1
        data = np.random.normal(loc = x[n_rounds], scale = 3, size = 10000).round().astype(int)
        return out, n_rounds, data

    else:
        return out