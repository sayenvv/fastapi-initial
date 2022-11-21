
python_sources(
    name="users",
    dependencies=[
        ":users",
        "//:requirements"
    ],
)

pex_binary(
    name="bin",
    entry_point="run.py",
    dependencies=[
        ":users",
        "//:requirements"
    ],
    restartable=True,
)
