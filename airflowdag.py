from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Define default arguments for the DAG
default_args = {
    'owner': 'Mahreen-Adeen-Uswa',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 6),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG
dag = DAG(
    'mlops_project',
    default_args=default_args,
    description='End-to-end pipeline for project',
    schedule=timedelta(days=1),
)

# Define the micro services task
Microservices = BashOperator(
    task_id='Microservices',
    bash_command='python3 Microservices_class.py',
    dag=dag,
)

# Define the data preprocessing task
preprocess_data = BashOperator(
    task_id='preprocess_data',
    bash_command='python3 DataPrerocessingClass.py',
    dag=dag,
)

# Define the data cleaning task
clean_data = BashOperator(
    task_id='clean_data',
    bash_command='python3 DataCleaningClass.py',
    dag=dag,
)

# Define the reduction task
reduction = BashOperator(
    task_id='reduction',
    bash_command='python3 DataReductionClass.py',
    dag=dag,
)

# Define the transformation task
transform = BashOperator(
    task_id='transform',
    bash_command='python3 DataTransformationClass.py',
    dag=dag,
)

# Define the ml task
ml = BashOperator(
    task_id='ml',
    bash_command='python3 MachineLearning.py',
    dag=dag,
)

# Define task dependencies
Microservices >> preprocess_data >> clean_data >> reduction >> transform >> ml
