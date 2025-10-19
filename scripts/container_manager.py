import subprocess

def docker_start():
    try:
        subprocess.run(
            ["make", "docker-up"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении `make docker-up`: {e}")
        print("STDOUT:\n", e.stdout.decode())
        print("STDERR:\n", e.stderr.decode())
        raise

def docker_restart():
    try:
        subprocess.run(
            ["make", "docker-restart"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении `make docker-restart`: {e}")
        print("STDOUT:\n", e.stdout.decode())
        print("STDERR:\n", e.stderr.decode())
        raise

def docker_down():
    try:
        subprocess.run(
            ["make", "docker-down"],
            check=True
        )
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении `make docker-down`: {e}")
        print("STDOUT:\n", e.stdout.decode())
        print("STDERR:\n", e.stderr.decode())
        raise