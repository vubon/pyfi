from PyFi.utils import command_processor

__all__ = [
    'run_server'
]


def run_server(full_path, port: int):
    command_processor(f"cd {full_path} && python -m http.server {port} ")
