df = df[["ID#","SSN#"]]

pd.options.display.float_format = '{:.0f}'.format
df["SSN#"] = df["SSN#"].astype(str)
df["SSN#"] = df["SSN#"].map(lambda x: x.rstrip('.0'))

df['length'] = df["SSN#"].apply(len)
df_clean = df[df['length'] == 9]
df_dirty = df[df['length'] != 9]

df_dirty.to_csv('dirty_socs.csv')
