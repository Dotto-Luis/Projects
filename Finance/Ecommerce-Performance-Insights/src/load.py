def load(dfs, connection):
    for tabla, df in dfs.items():
        connection.register(tabla, df)

