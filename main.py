from app.logging_config import setup_logging
from app.orchestrator import run

def main():
    setup_logging()
    run()

if __name__ == "__main__":
    main()
