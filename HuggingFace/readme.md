# Learning to use Hugging Face models 

## NLP Training - https://huggingface.co/learn/nlp-course/chapter1/1 
### Setup  
This is all done using Jupyter notebooks running on Linux. It also is using a dedicated Python environment. To use the environment ipykernel needs to be installed  
```bash
pip install ipykernel
```

Download the requirements.txt file to whatever folder is going to be used and run the following commands:
```bash
# create the environment
python3 -m venv ai_training_env
# activate it
source ai_training_env/bin/activate
# install supporting packages
pip install -r requirements.txt
# set it up to be used with Jupyter
python -m ipykernel install --user --name=ai_training_env --display-name "Python (AI Training)"
```

When Jupyter is running you should be able to change the kernel to "Python (AI Training)"
