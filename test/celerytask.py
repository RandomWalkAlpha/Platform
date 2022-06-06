from celery import Celery
from workflow.computing.engine import ComputingEngine

app = Celery('engine', backend='redis://localhost:6379/0', broker='redis://localhost:6379/0')
app.register_task(ComputingEngine())


@app.task(bind=True, base=ComputingEngine)
def parse(self, expression: str):
    df, _ = self.compute(expression)



if __name__ == '__main__':
    exp = 'MA($S_DQ_CLOSE, 30)'
    parse.delay(exp)