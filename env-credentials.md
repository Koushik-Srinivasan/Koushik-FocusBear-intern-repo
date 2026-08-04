# Using .env to Keep Database Credentials Secret in Jupyter

## Tasks

Installed `python-dotenv` (and `psycopg2-binary` to actually attempt a Postgres connection), created a `.env` file with the PostgreSQL credentials (`DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`), and loaded them into the notebook with `load_dotenv()` and `os.getenv()`. `.env` is listed in `.gitignore` so it never reaches version control; a `.env.example` file with placeholder values is committed instead so anyone cloning the repo knows which variables to set. The full working example is in [env_credentials_demo.ipynb](env_credentials_demo.ipynb).

## Reflection

**Why is it more secure to use a `.env` file for database credentials instead of hardcoding them?**

Hardcoded credentials end up wherever the code goes, in every commit, every clone, every diff, and every place the notebook gets shared, and removing them later doesn't erase them from git history. A `.env` file keeps the actual values out of the codebase entirely, the notebook only ever references variable names, never the credentials themselves, so the notebook can be shared, reviewed, or pushed without exposing anything. Because `.env` is excluded via `.gitignore`, there's also no risk of accidentally committing a real password in a moment of not thinking about it, which is exactly the kind of mistake that's easy to make when credentials are typed directly into a cell.

**How can `python-dotenv` simplify managing environment variables in Jupyter?**

Without it, environment variables would need to be exported manually in the shell before starting the Jupyter kernel, which is easy to forget and doesn't travel with the notebook. `python-dotenv` collapses that into two lines, `load_dotenv()` reads the `.env` file in the project root and populates the process environment, then `os.getenv("DB_HOST")` (etc.) reads each value like any other environment variable. It also makes switching between environments simple, swapping in a different `.env` file (local vs. staging credentials, for example) changes what the notebook connects to without touching a single line of code.
