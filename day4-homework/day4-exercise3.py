#!/usr/bin/env python3

"""
USAGE: <./03-timecourse.py><samples.csv><~/data/results/stringtie/><Gene1><Gene2>...<GeneN>

Create a timecourse of all transcripts of a given gene name (FBtr0331261) for both genders


"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# pull out the samples with your desired sex





for choices in sys.argv[3:]:
	

	def generalizing_gender(frame, gender, gene):
		soi = frame.loc[:,"sex"] == gender
		df = frame.loc[soi,:]

		fpkm_avg = []
		for index, sample, sex, stage in df.itertuples():
			filename = os.path.join(sys.argv[2], sample, "t_data.ctab")
			ctab_df = pd.read_table(filename, index_col = "t_name")
			roi = ctab_df.loc[:, "gene_name"] == gene
			fpkm = ctab_df.loc[roi,"FPKM"]
			fpkm_avg.append(np.mean(fpkm))

		return fpkm_avg


	df = pd.read_csv(sys.argv[1])
	f_fpkm = generalizing_gender(df, "female", choices)
	m_fpkm = generalizing_gender(df, "male", choices)



	ind = np.arange(8) 
	fig, ax = plt.subplots()
	ax.plot(m_fpkm, color = "blue", label = 'male')
	ax.plot(f_fpkm, color = "red", label = 'female')
	plt.xlabel('developmental stage')
	plt.ylabel('mRNA abundance FPKM')
	plt.xticks(ind,('10', '11', '12', '13', '14A', '14B', '14C', '14D'), rotation = 'vertical')
	plt.title(choices)
	plt.tight_layout()

	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

	# Put a legend to the right of the current axis
	ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon = False)





	fig.savefig(choices)
	plt.close(fig)
