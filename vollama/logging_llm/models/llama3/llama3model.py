from dataclasses import dataclass

@dataclass
class llama3model:
    model:str
    prompt:str
    stream:bool = False
    
    