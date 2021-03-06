import matplotlib.pyplot as plt
import os

from Model import runRealData

time_periods = [4, 8] # weeks
num_nurses = [30, 40, 50, 60, 80, 100, 120]

if not os.path.exists("result"):
    os.makedirs("result")

for id_h in [0, 1]:
    for id_first_w in [0, 4]:
        '''SECOND PLOT: FIXED MAX CALCULATION TIME'''
        # fixed maximum time of calculation
        max_time = 60 * 60 # 1h
        for t in time_periods:
            relative_gaps = []
            for n in num_nurses:
                elapsed_time, absolute_gap, relative_gap = runRealData(n, t, max_time, id_h, id_first_w)
                relative_gaps.append(relative_gap*100)

            plt.plot(num_nurses, relative_gaps, label=str(t)+"weeks")

        plt.legend()
        plt.xlabel('Numero di infermieri')
        plt.ylabel('Gap percentuale (%)')
        plt.title("Tempo massimo: {}s".format(max_time))
        # per togliere il float in valori interi delle x
        plt.xticks(num_nurses)
        # per fare exp su server
        plt.savefig(os.path.join("result","Gap_1h-h{}_w{}.png".format(id_h, id_first_w)))
        plt.clf() # per non fare i grafici sempre sulla stessa figura



        '''THIRD PLOT: FIXED MAX CALCULATION TIME (WIDE)'''
        # fixed maximum time of calculation
        max_time = 60 * 60 * 2 # 2h
        for t in time_periods:
            relative_gaps = []
            for n in num_nurses:
                elapsed_time, absolute_gap, relative_gap = runRealData(n, t, max_time, id_h, id_first_w)
                relative_gaps.append(relative_gap*100)

            plt.plot(num_nurses, relative_gaps, label=str(t)+"weeks")

        plt.legend()
        plt.xlabel('Numero di infermieri')
        plt.ylabel('Gap percentuale (%)')
        plt.title("Tempo massimo: {}s".format(max_time))
        # per togliere il float in valori interi delle x
        plt.xticks(num_nurses)
        # per fare exp su server
        plt.savefig(os.path.join("result","Gap_2h-h{}_w{}.png".format(id_h, id_first_w)))
        plt.clf() # per non fare i grafici sempre sulla stessa figura



        '''FIRST PLOT: TIME CALCULATION'''
        # fixed a large time_period
        # decreasing the nurses number
        max_time = 60 * 60 # 1h
        for t in time_periods:
            elapsed_times = []
            for n in num_nurses:
                elapsed_time, absolute_gap, relative_gap = runRealData(n, t, max_time, id_h, id_first_w)
                elapsed_times.append(elapsed_time)

            plt.plot(num_nurses, elapsed_times, label=str(t)+"weeks")

        plt.legend()
        plt.xlabel('Numero di infermieri')
        plt.ylabel('Tempo di calcolo (s)')
        plt.title("Tempo di esecuzione")
        plt.xticks(num_nurses)
        # per fare exp su server
        plt.savefig(os.path.join("result","Time_1h-h{}_w{}.png".format(id_h, id_first_w)))
        plt.clf() # per non fare i grafici sempre sulla stessa figura 