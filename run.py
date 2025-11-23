import papermill as pm

# List of notebook names
notebooks = ["google-scrape.ipynb"]

for nb in notebooks:
    print(f"Running: {nb}")
    try:
        output_name = nb.replace(".ipynb", "_output.ipynb")
        pm.execute_notebook(
            nb,
            output_name
        )
        print(f"✔ Finished {nb}")
    except Exception as e:
        print(f"❌ Error running {nb}: {e}")
        continue
