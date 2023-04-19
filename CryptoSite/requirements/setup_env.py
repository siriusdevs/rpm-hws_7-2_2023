"""Creating .env file."""
env_consts = {
    'PG_HOST': '127.0.0.1',
    'PG_PORT': '5555',
    'PG_USER': 'valun',
    'PG_PASSWORD': '123',
    'PG_DBNAME': 'CRYPTO_DB',
    'BINANCE_KEY': '4d3bfad384msh29d497cb4d54650p10d4b8jsned19079bf66e',
}


def setup_env():
    """Seting up .env file."""
    lines = [f'{const}={equiv}\n' for const, equiv in env_consts.items()]
    with open('./.env', 'w') as env_file:
        env_file.writelines(lines)


if __name__ == '__main__':
    setup_env()
