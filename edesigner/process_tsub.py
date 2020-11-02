import pandas as pd


if __name__ == '__main__':
	df = pd.read_csv('bbs/edesigner_bbs_queried.smi', sep=' ')
	#some issues with the name output
	df = df.rename(columns={'a_bromo_ketones':'a_bromo_ketone', 'Name':'ID'})
	df_fgs = pd.read_csv('bbs/queries_4_bb_annotation.csv')
	
	#now need to match up...I am embarassed if you are reading this code
	lilly_mol_cols = df.columns.tolist()


	rename_dict = {}
	for qry in df_fgs['Query'].tolist():
		for lil in lilly_mol_cols:
			if qry.lower() == lil.lower():
				value = df_fgs.loc[df_fgs['Query']==qry]['FG'].values[0]
				rename_dict[lil]=value

	df = df.rename(columns=rename_dict)
	df_smiles = pd.read_csv('bbs/edesigner_bbs.csv')
	df_out = pd.merge(df, df_smiles, left_on='ID', right_on='ID', how='inner')
	df_out.to_csv('bbs/edesigner_bbs_cleaned.csv', index=False)
