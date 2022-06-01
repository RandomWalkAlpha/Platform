from celery import Celery
from workflow.computing.engine import ComputingEngine

app = Celery('engine', backend='redis://localhost', broker='redis://localhost//6379')

app.register_task(ComputingEngine())


@app.task(bind=True, base=ComputingEngine)
def parse(self, expression: str):
    self.compute()


if __name__ == '__main__':
    exp = 'MA($S_DQ_CLOSE, 30)'
    parse.delay(exp)