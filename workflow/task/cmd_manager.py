from celery import Celery
from workflow.computing.engine import ComputingEngine


# command: celery -A cmd_manager worker --loglevel=info
if __name__ == '__main__':
    app = Celery('engine', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
    app.register_task(ComputingEngine())

    @app.task(bind=True, base=ComputingEngine)
    def parse(self, expression: str):
        self.compute(expression)
